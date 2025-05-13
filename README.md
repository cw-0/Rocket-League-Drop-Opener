# Rocket League Drop Opener

This script automates the opening of drops using the `vgamepad` library to simulate gamepad button presses.

## Features
- Automates process of opening drops
- Controls the D-pad to navigate between options
- Allows user to select how many items to open

## Installation

1. **Clone the Repository**:
   Start by cloning the repository to your local machine. Open a terminal or command prompt and run the following command:
   
   ```bash
   git clone https://github.com/cw-0/Rocket-League-Drop-Opener

2. **Install Dependencies**:
    Ensure you have Python 3.x installed. If not, you can download it from the official Python website: https://www.python.org/downloads/.

    Install the required Python libraries by running:

    ```bash
    pip install -r requirements.txt

3. **Connect Your Gamepad (Optional|May Be Needed on Some Systems)**:
    Make sure that your gamepad is connected to your Windows machine and is recognized by the system.

## Usage

1. Open Rocket League, go to the drop you want to open. (You should see the rarities available and "Open Drop" in the bottom left) 

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script as administrator/root:

    ```bash
    python main.py

4. You will be prompted to enter:

* The total number of drops to open. (How many of that drop you have)
* The time (in seconds) to wait before starting the automation. (This gives you time to get in game)

5. The script will automatically start simulating gamepad input to open items, press buttons, and move the D-pad.

## Example Output
    ```bash
    How many items to open? 5
    How many seconds to wait before starting script? 10
    Program will start in: 10 seconds
    Program will start in: 9 seconds
    ...
    Toggling Controller On
    Pressing Open Drop
    Confirming Open Drop
    Waiting 9 seconds for animation
    Accepting Drop

    Case 1 of 5 opened
    Repeating

    ...
    All Items Opened!
    Press enter to close...

