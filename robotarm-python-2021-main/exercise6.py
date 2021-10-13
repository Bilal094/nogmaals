from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = (3)
for x in range(9):
    robotArm.moveRight()

for x in range(8):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()