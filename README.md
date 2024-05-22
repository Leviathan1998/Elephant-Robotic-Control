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
