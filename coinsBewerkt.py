# name of student: Bilal Achrifi
# number of student: 99066318
# purpose of program: wisselgeld uitrekenen
# function of program:
# structure of program: inputs, if en elif en while loops

toPay = int(float(input('Amount to pay: '))* 100) # Hier wordt gevraagd hoeveel je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # Hier wordt gevraagd hoeveel je al hebt betaald
change = paid - toPay # Hier wordt de betaalde bedrag en het bedrag dat nog betaald moet worden van elkaar afgetrokken om 'change' een waarde te geven

if change > 0: # Als de wisselgeld groter is dan 0, dan wordt deze if command geactiveerd
  coinValue = 500 # De muntstuk heeft een waarde van 500 cent
  
  while change > 0 and coinValue > 0: # Deze while loopt wordt geactiveerd als de coinvalue en change groter zijn dan 0
    nrCoins = change // coinValue # Hier wordt change en coinvalue door elkaar gedeeld

    if nrCoins > 0: # Als de amount gelijk is aan 0, dan wordt deze if geact
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Hier wordt weergegeven hoeveel je moet geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Hier wordt gevraagd hoeveel je bepaalde muntstukken hebt gegeven
      change -= nrCoinsReturned * coinValue # Hier wordt de wisselgeld berekend

# comment on code below: 
    if coinValue == 500:
      coinValue = 50
    elif coinValue == 300:
      coinValue = 20
    elif coinValue == 200:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # Als je geen muntstukken hebt om te geven, word je hier naartoe geleidt
  print('Change not returned: ', str(change) + ' cents')
else:
  print('Done')