from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = (3)
# Jouw python instructies zet je vanaf hier:
stap = 9

for x in range(1,6):
    robotArm.grab()
    for x in range(stap):
        robotArm.moveRight()
    stap -= 1
    robotArm.drop()
    for y in range(stap):
        robotArm.moveLeft()
    stap -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()