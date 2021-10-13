from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = (3)
# Jouw python instructies zet je vanaf hier:
for x in range(9):
    robotArm.moveRight()
for y in range(20):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for q in range(9):
            robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()