''' Building blocks with Elephant Robotics robot'''


from elephant_sdk import ElephantSDK

class ElephantTowerBuilder:
    """Class for building tower from blocks."""

    def __init__(self):
        """Initialize height of tower to 0"""
        self.tower_height = 0

    def add_block(self):
        """Add block to tower and icrease it height by 1"""
        self.tower_height += 1
        print(f"+1 block added to tower. Actual height of tower is : {self.tower_height}")

    def remove_block(self):
        """Take block from tower if tower is higher than 0"""
        if self.tower_height > 0:
            self.tower_height -= 1
            print(f"-1 block taken from tower. Actual height of tower is {self.tower_height}")
        else:
            print("Tower is on ground level")

# Testování stavby věže
tower_builder = ElephantTowerBuilder()
tower_builder.add_block()
tower_builder.add_block()
tower_builder.remove_block()
