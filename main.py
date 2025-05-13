import vgamepad as vg
import time
import getpass

gamepad = vg.VX360Gamepad()
A_BUTTON = vg.XUSB_BUTTON.XUSB_GAMEPAD_A


def click_a():
    gamepad.press_button(button=A_BUTTON)
    gamepad.update()
    time.sleep(.1)

    gamepad.release_button(button=A_BUTTON)
    gamepad.update()

    time.sleep(.5)

def move_dpad(direction):
    match direction.strip().lower():
        case "left":
            side = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
        case "right":
            side = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
        case "up":
            side = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
        case "down":
            side = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN

    gamepad.press_button(button=side)
    gamepad.update()
    time.sleep(.1)

    gamepad.release_button(button=side)
    gamepad.update()
    time.sleep(.1)
    

    time.sleep(.5)

def main():
    items_total = int(input("How many items to open? "))
    pause_time = int(input("How many seconds to wait before starting script? "))
    items_left = items_total
    items_opened = 0

    while pause_time > 0:
        print(f"Program will start in: {pause_time} seconds")
        pause_time-=1
        time.sleep(1)

    while items_left:
        print("Toggling Controller On")
        move_dpad("up")
        print("")

        print("Pressing Open Drop")
        click_a()
        print("")

        print("Confirming Open Drop")
        move_dpad("left")
        click_a()
        print("")

        print("Waiting 9 seconds for animation")
        for i in reversed(range(1, 10)):
            print(i)
            time.sleep(1)
        print("")

        print("Accepting Drop")
        move_dpad("right")
        move_dpad("right")
        time.sleep(1)
        click_a()
        print("\n\n")

        items_opened+=1
        print(f"Drop {items_opened} of {items_total} opened")
        items_left-=1

        if items_left > 0:
            print("Repeating\n\n")
    
    print("All Items Opened!")
    getpass.getpass("Press enter to close...")

if __name__ == "__main__":
    main()