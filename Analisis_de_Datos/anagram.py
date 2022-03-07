def anagrama(ana1 = '', ana2 = ''):

  dic_ana1 = {}
  dic_ana2 = {}

  ana1 = ana1.lower().replace('á', 'a')
  ana1 = ana1.lower().replace('é', 'e')
  ana1 = ana1.lower().replace('í', 'i')
  ana1 = ana1.lower().replace('ó', 'o')
  ana1 = ana1.lower().replace('ú', 'u')

  ana2 = ana2.lower().replace('á', 'a')
  ana2 = ana2.lower().replace('é', 'e')
  ana2 = ana2.lower().replace('í', 'i')
  ana2 = ana2.lower().replace('ó', 'o')
  ana2 = ana2.lower().replace('ú', 'u')

  for i in ana1.lower().replace(' ', ''):
    if i in dic_ana1:
      dic_ana1[i] += 1
    else:
      dic_ana1[i] = 1

  for i in ana2.lower().replace(' ', ''):
    if i in dic_ana2:
      dic_ana2[i] += 1
    else:
      dic_ana2[i] = 1

  if dic_ana1 == dic_ana2:
    return f'{ana1} - {ana2}: Esto es un anagrama', True
  else:
    return f'{ana1} - {ana2}: Esto no es un anagrama', False


print(anagrama('válóra', 'Álva ro'))
print(anagrama('Para', 'A rpa'))
print(anagrama('Jor gé', 'Jorges'))
print(anagrama('Azúl', 'Zu la'))
