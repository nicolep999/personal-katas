class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


robots = [
    Robot("basic_robot"),
    MedicalRobot("da_vinci"),
    ChefRobot("moley"),
    WarRobot("griffin"),
]
for robot in robots:
    print(robot.sensors_amount())
