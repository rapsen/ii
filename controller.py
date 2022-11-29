from model import model as m

class Controller():
    def __init__(self) -> None:
        
        self.robots = self.getAllRobot()
        self.id = self.robots[0]
                
    def getAllRobot(self) -> list:
        
        robots = []
        response = m.getAllDeviceId()
        for robot in response:
            robots.append(robot['deviceId'])
            
        return robots
        
# Create istance of the controller
controller = Controller()
