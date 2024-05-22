# Elephant-Robotic-Control
This Repository contains code for controling robotic arm from Elephant Robotics inc. 
![image](https://github.com/Leviathan1998/Elephant-Robotic-Control/assets/96702807/9c160d09-e887-465b-92ce-4c5ada195838)

Preview of robot representation




**accurracy_of_robot.py**

### Explanation of the Code (English and Slovak)

#### English

1. **MyRobot Class**:
    - Inherits from the `Robot` class provided by Elephant Robotics SDK.
    - `__init__`: Connects to the robot using its IP address.
    - `move_to`: Moves the robot to the target coordinates. The `move_absolute` function might be different based on the SDK documentation.
    - `get_position`: Returns the current position of the robot in the format `{ 'x': x_value, 'y': y_value, ... }`.

2. **calculate_distance**: Calculates the distance between two points in 2D space.

3. **test_robot_accuracy**:
    - Moves the robot to the target position multiple times (defined by the `repetitions` parameter).
    - Records the positions after each move.
    - Calculates the average position (to estimate accuracy).
    - Calculates accuracy as the distance between the average position and the target position.
    - Calculates repeatability as the average distance between each recorded position and the average position.

4. **Main Part of the Program**:
    - Creates an instance of the robot and connects to it.
    - Sets the target position and the number of repetitions.
    - Calls the function to test accuracy and repeatability.
    - Prints the results.

Make sure to adjust the code according to the specific SDK documentation provided by Elephant Robotics, including the correct method for connecting to the robot and commands for movement and position retrieval.

#### Slovak

1. **Trieda MyRobot**:
    - Dedi z triedy `Robot` poskytovanej Elephant Robotics SDK.
    - `__init__`: Pripojí sa k robotu pomocou IP adresy.
    - `move_to`: Presunie robota na cieľové súradnice. Funkcia `move_absolute` môže byť iná podľa dokumentácie SDK.
    - `get_position`: Vráti aktuálnu pozíciu robota vo formáte `{ 'x': x_value, 'y': y_value, ... }`.

2. **calculate_distance**: Vypočíta vzdialenosť medzi dvoma bodmi v 2D priestore.

3. **test_robot_accuracy**:
    - Robot sa pohne na cieľovú pozíciu viackrát (definované parametrom `repetitions`).
    - Zaznamenáva pozície po každom pohybe.
    - Vypočíta priemernú pozíciu (pre odhad presnosti).
    - Vypočíta presnosť ako vzdialenosť medzi priemernou pozíciou a cieľovou pozíciou.
    - Vypočíta opakovateľnosť ako priemernú vzdialenosť medzi každou zaznamenanou pozíciou a priemernou pozíciou.

4. **Hlavná časť programu**:
    - Vytvorí inštanciu robota a pripojí sa k nemu.
    - Nastaví cieľovú pozíciu a počet opakovaní.
    - Zavolá funkciu pre testovanie presnosti a opakovateľnosti.
    - Vytlačí výsledky.

Nezabudnite prispôsobiť kód podľa špecifickej dokumentácie SDK od Elephant Robotics, vrátane správneho spôsobu pripojenia k robotu a príkazov pre pohyb a čítanie pozícií.


**building.py**



1. **Connecting to the Robot**:
    - The `__init__` method now takes `robot_ip` as a parameter to initialize the connection to the robot using its IP address.
    - `self.robot.connect()`: This line assumes there is a method to connect to the robot. Adjust this according to the actual SDK documentation.

2. **Adding a Block**:
    - `self.robot.pick_block()`: Assumes there is a method in the SDK to pick up a block.
    - `self.robot.place_block_on_tower(self.tower_height)`: Assumes there is a method to place a block on top of the current tower height.

3. **Removing a Block**:
    - `self.robot.remove_block_from_tower(self.tower_height - 1)`: Assumes there is a method to remove the top block from the tower.

### Assumptions

This code assumes the existence of certain methods in the Elephant Robotics SDK (`pick_block`, `place_block_on_tower`, `remove_block_from_tower`). You'll need to refer to the actual SDK documentation and replace these with the correct method names and parameters provided by Elephant Robotics.

If you provide specific details from the SDK documentation or example methods, I can further tailor the code to match the actual API calls and capabilities of the Elephant Robotics system.



**control_keaboard.py**


1. **Movement Methods**:
    - Added `move_left` and `move_right` methods to handle lateral movements of the robot.

2. **Keyboard Control Method**:
    - `control_with_keyboard`: This method continuously checks for key presses. When a WASD key is pressed, the corresponding movement method is called. The `distance` variable defines the distance moved per key press.

3. **Main Control Loop**:
    - The control loop continuously listens for key presses using `keyboard.is_pressed` and executes the corresponding movement methods.
    - Pressing 'q' exits the control loop and stops the program.

### Requirements

- Ensure you have the `keyboard` module installed. You can install it using pip:
  ```bash
  pip install keyboard
  ```
- The actual SDK methods for moving the robot (`move_forward`, `move_backward`, `move_left`, `move_right`) should be defined in the `ElephantSDK` class. Adjust the method names and parameters according to the actual SDK documentation if necessary. 

This setup allows you to control the robot in real-time using the keyboard, making it interactive and suitable for quick testing and adjustments.




**mapping.py**

1. **Robot Initialization**:
   - Added `robot_ip` to the constructor to initialize the connection to the robot.
   - `self.robot.connect()`: Connect to the robot using the IP address.

2. **Update Map**:
   - Updated to use `cv2.circle` for marking the robot position and obstacles for better visualization.

3. **Detect Obstacles**:
   - Fixed the tuple extraction from contours for obstacle detection.

4. **Move Robot**:
   - Updated to include `self.robot.move_to(new_position[0], new_position[1])`, assuming `move_to` is the correct method from the SDK for moving the robot to specified coordinates.
   - Adjusted `move_robot` to ensure proper movement commands to the robot.

5. **Camera Handling**:
   - Added `cap.release()` to release the camera resource when the loop ends.

### Assumptions

- The `ElephantSDK` class from the SDK has methods such as `connect` and `move_to` for robot control.
- The `move_to` method correctly interprets the coordinates provided for robot movement.

Ensure to replace the method names and functionalities with the correct ones as per the actual Elephant Robotics SDK documentation. If there are specific commands or functions for movement and connection, adjust the code accordingly.
