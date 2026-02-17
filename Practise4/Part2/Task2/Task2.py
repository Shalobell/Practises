import os
import datetime
import platform
import pyscreenshot
import pyautogui

def showAndRestoreDesktop():
    system = platform.system()
    if system == "Windows":
        pyautogui.hotkey('win', 'd')
    elif system == "Darwin":
        pyautogui.hotkey('command', 'option', 'd')
    elif system == "Linux":
        pyautogui.hotkey('win', 'd')
    else:
        print("unknown operating system")


def takeDesktopScreenshot(restore=True):
    folder = "desktopScreenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/desktop_{timestamp}.png"

    if restore:
        showAndRestoreDesktop()

    try:
        print("Делаем скриншот...")
        im = pyscreenshot.grab()
        im.save(filename)
        print(f"Скриншот рабочего стола сохранён: {filename}")
    except Exception as e:
        print(f"Ошибка при скриншоте: {e}")
    finally:
        if restore:
            showAndRestoreDesktop()

if __name__ == "__main__":
    takeDesktopScreenshot()