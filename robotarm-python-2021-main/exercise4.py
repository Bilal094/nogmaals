from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = (3)
for x in range(3):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
for x in range(3):
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()