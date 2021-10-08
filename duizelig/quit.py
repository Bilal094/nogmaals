i = 0

while i <= 999:
    vraag = input('Wil je doorgaan? ')
    if vraag == 'quit':
        print('Deze vraag is '+ str(i) +' keer gesteld.')
        break
    i=i+1