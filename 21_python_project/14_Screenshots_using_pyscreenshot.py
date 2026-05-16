# # pip install pyscreenshot
# # Fisrt install the required libraries if not already installed.




# # Program to take screenshot

# import pyscreenshot

# # To capture the screen
# image = pyscreenshot.grab()

# # To display the captured screenshot
# image.show()

# # To save the screenshot
# image.save("code_screenshot.png")








# Program for partial screenshot

import pyscreenshot

# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))

# To view the screenshot
image.show()

# To save the screenshot
image.save("GeeksforGeeks.png")