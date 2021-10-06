dag = input('Type een dag van de week in: ')
einddag = False
ma = 'maandag'
di = 'dinsdag'
wo = 'woensdag'
do = 'donderdag'
vr = 'vrijdag'
za = 'zaterdag'
zo = 'zondag'

while einddag == False:
    if dag == 'maandag':
        print(ma)
    if dag == 'dinsdag':
        print(ma,di)
    if dag == 'woensdag':
        print(ma,di,wo)
    if dag == 'donderdag':
        print(ma,di,wo,do)
    if dag == 'vrijdag':
        print(ma,di,wo,do,vr)
    if dag == 'zaterdag':
        print(ma,di,wo,do,vr,za)
    if dag == 'zondag':
        print(ma,di,wo,do,vr,za,zo)
    break

