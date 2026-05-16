"""Small file comparison utility.

Features:
- Compute SHA-256 hashes of two files efficiently (chunked reading).
- Print a clear message whether files are identical.
- CLI: provide two file paths as arguments or run interactively.

This works for PDFs or any binary files. It doesn't parse PDF content; it compares raw bytes.
"""

import argparse
import hashlib
import os
from typing import Tuple


def file_hash(path: str, algo: str = "sha256") -> str:
    """Compute hex digest of a file using the requested algorithm.

    Reads the file in chunks to support large files.
    Raises FileNotFoundError or PermissionError on error.
    """
    h = hashlib.new(algo)
    # read in 64KB chunks
    chunk_size = 65536
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def compare_files(path1: str, path2: str, algo: str = "sha256") -> Tuple[dict, dict, bool]:
    """Compare two files and return (info1, info2, identical).

    info dictionaries include: path, size, hash.
    identical is True when both hashes (and sizes) match.
    """
    if not os.path.exists(path1):
        raise FileNotFoundError(f"File not found: {path1}")
    if not os.path.exists(path2):
        raise FileNotFoundError(f"File not found: {path2}")

    size1 = os.path.getsize(path1)
    size2 = os.path.getsize(path2)
    hash1 = file_hash(path1, algo=algo)
    hash2 = file_hash(path2, algo=algo)

    info1 = {"path": path1, "size": size1, "hash": hash1}
    info2 = {"path": path2, "size": size2, "hash": hash2}
    identical = (size1 == size2) and (hash1 == hash2)
    return info1, info2, identical


def main():
    parser = argparse.ArgumentParser(description="Compare two files using hashes (efficient, chunked).")
    parser.add_argument("file1", nargs="?", help="First file path")
    parser.add_argument("file2", nargs="?", help="Second file path")
    parser.add_argument("--algo", default="sha256", help="Hash algorithm (default: sha256)")
    args = parser.parse_args()

    if not args.file1 or not args.file2:
        # Interactive prompt
        try:
            f1 = input("Enter path to first file: ").strip()
            f2 = input("Enter path to second file: ").strip()
        except KeyboardInterrupt:
            print("\nCancelled by user.")
            return
    else:
        f1, f2 = args.file1, args.file2

    try:
        info1, info2, identical = compare_files(f1, f2, algo=args.algo)
    except FileNotFoundError as e:
        print("Error:", e)
        return
    except PermissionError as e:
        print("Permission error:", e)
        return
    except Exception as e:
        print("Unexpected error:", e)
        return

    print(f"File 1: {info1['path']}  (size={info1['size']} bytes)")
    print(f"  {args.algo} = {info1['hash']}")
    print(f"File 2: {info2['path']}  (size={info2['size']} bytes)")
    print(f"  {args.algo} = {info2['hash']}")
    if identical:
        print("Result: The files are IDENTICAL (same size and hash).")
    else:
        print("Result: The files are DIFFERENT.")


if __name__ == "__main__":
    main()