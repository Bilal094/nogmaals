from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = (2)
# Jouw python instructies zet je vanaf hier:
stap = 1
stap2 = 1
for x in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for y in range(stap):
            robotArm.moveRight()
        stap += 1
        robotArm.drop()
        for z in range(stap2):
            robotArm.moveLeft()
            stap2 += 1
    else:
        break
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()