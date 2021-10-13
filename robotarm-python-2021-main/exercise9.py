from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = (3)
# Jouw python instructies zet je vanaf hier:
for x in range(1,5):
    for s in range(x):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for a in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()