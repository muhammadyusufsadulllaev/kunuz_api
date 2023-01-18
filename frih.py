import pyautogui, time

time.sleep(1)
f = ("Muhammad Yusuf, nima gap", "tinch")

while True:
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
