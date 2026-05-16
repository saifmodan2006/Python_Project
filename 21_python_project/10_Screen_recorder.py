"""Screen recorder utility.

This script captures the screen and writes a video file. It includes:
- duration or max-frames to avoid infinite loops
- optional live preview (can be disabled)
- a `--test` mode that creates a small synthetic video (useful for CI/headless)

Dependencies:
    pip install numpy pyautogui opencv-python

Notes:
 - On headless systems (no display) use `--test` to verify the writer without
   attempting to capture the real screen.
"""

import time
import argparse
import cv2
import numpy as np
import os
from typing import Optional, Tuple

try:
    import pyautogui
except Exception:
    pyautogui = None


def _make_writer(filename: str, codec: str, fps: float, resolution: Tuple[int, int]):
    fourcc = cv2.VideoWriter_fourcc(*codec)
    return cv2.VideoWriter(filename, fourcc, fps, resolution)


def record_simulated(output: str = "simulated.avi", fps: float = 10.0, resolution: Tuple[int, int] = (320, 240), frames: int = 30, codec: str = "XVID", show_preview: bool = False):
    """Create a short synthetic video to test writer and file creation.

    This does not capture the screen and is safe to run in headless/test envs.
    """
    out = _make_writer(output, codec, fps, resolution)
    try:
        for i in range(frames):
            # generate a simple moving gradient frame
            img = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)
            color = (int(255 * (i / max(1, frames - 1))), 50, 255 - int(255 * (i / max(1, frames - 1))))
            cv2.rectangle(img, (0, 0), (resolution[0], resolution[1]), color, -1)
            text = f"Frame {i+1}/{frames}"
            cv2.putText(img, text, (10, resolution[1] // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
            out.write(img)
            if show_preview:
                cv2.imshow("Preview", img)
                if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
                    break
    finally:
        out.release()
        if show_preview:
            cv2.destroyAllWindows()


def record_screen(output: str = "Recording.avi", fps: float = 20.0, resolution: Tuple[int, int] = (1280, 720), region: Optional[Tuple[int, int, int, int]] = None, duration: Optional[float] = None, max_frames: Optional[int] = None, codec: str = "XVID", show_preview: bool = True):
    """Record the screen to a file.

    Parameters:
    - output: output filename
    - fps: frames per second
    - resolution: (width, height) of the output video
    - region: optional (left, top, width, height) to capture a subregion
    - duration: seconds to record (optional)
    - max_frames: alternative to duration; stops after this many frames
    - codec: fourcc codec (default XVID)
    - show_preview: whether to display a live preview window

    Raises RuntimeError if pyautogui is not available when not using test mode.
    """
    if pyautogui is None:
        raise RuntimeError("pyautogui is required for screen capture; install it or run with --test mode")

    if duration is not None and max_frames is None:
        max_frames = int(duration * fps)

    if max_frames is None:
        max_frames = float('inf')

    out = _make_writer(output, codec, fps, resolution)
    start = time.time()
    frame_count = 0
    try:
        if show_preview:
            cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Live", min(480, resolution[0]), min(270, resolution[1]))

        target_frame_time = 1.0 / fps
        while frame_count < max_frames:
            loop_start = time.time()
            if region:
                img = pyautogui.screenshot(region=region)
            else:
                img = pyautogui.screenshot()
            frame = np.array(img)
            # pyautogui returns RGB; OpenCV expects BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            # resize to requested resolution if necessary
            if (frame.shape[1], frame.shape[0]) != resolution:
                frame = cv2.resize(frame, resolution)

            out.write(frame)
            frame_count += 1

            if show_preview:
                try:
                    cv2.imshow('Live', frame)
                except Exception:
                    # Preview not available (headless); ignore
                    show_preview = False

            # Check for 'q' key without blocking too long
            if show_preview and (cv2.waitKey(1) & 0xFF) == ord('q'):
                break

            # Maintain approximate fps
            elapsed = time.time() - loop_start
            sleep_for = target_frame_time - elapsed
            if sleep_for > 0:
                time.sleep(sleep_for)
            # if duration provided, also break when elapsed exceeds it
            if duration is not None and (time.time() - start) >= duration:
                break
    finally:
        out.release()
        if show_preview:
            cv2.destroyAllWindows()


def _parse_region(s: str) -> Optional[Tuple[int, int, int, int]]:
    # expected format: x,y,w,h
    if not s:
        return None
    parts = s.split(',')
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("region must be in format x,y,w,h")
    return tuple(int(p) for p in parts)


def main():
    parser = argparse.ArgumentParser(description="Screen recorder with duration and test mode")
    parser.add_argument("--output", default="Recording.avi", help="Output filename")
    parser.add_argument("--fps", type=float, default=20.0, help="Frames per second")
    parser.add_argument("--width", type=int, default=1280, help="Output width")
    parser.add_argument("--height", type=int, default=720, help="Output height")
    parser.add_argument("--duration", type=float, default=None, help="Duration in seconds")
    parser.add_argument("--max-frames", type=int, default=None, help="Stop after this many frames")
    parser.add_argument("--region", type=_parse_region, default=None, help="Region to capture as x,y,w,h")
    parser.add_argument("--codec", default="XVID", help="FourCC codec string (default XVID)")
    parser.add_argument("--no-preview", action="store_true", help="Disable live preview window")
    parser.add_argument("--test", action="store_true", help="Create a short simulated video instead of screen capture (useful for testing/headless)")
    args = parser.parse_args()

    resolution = (args.width, args.height)
    show_preview = not args.no_preview

    if args.test:
        print("Running in test mode: generating a short simulated video")
        record_simulated(output=args.output, fps=args.fps, resolution=resolution, frames=int(args.fps * (args.duration or 1.0)), codec=args.codec, show_preview=show_preview)
        print(f"Test video written to {args.output}")
        return

    try:
        record_screen(output=args.output, fps=args.fps, resolution=resolution, region=args.region, duration=args.duration, max_frames=args.max_frames, codec=args.codec, show_preview=show_preview)
        print(f"Recording saved to {args.output}")
    except RuntimeError as e:
        print("Error:", e)


if __name__ == '__main__':
    main()
