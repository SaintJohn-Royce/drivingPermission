country = input('where are you from? ')

age = input('what is your age? please insert integer numbers: ')

age = int(age)

if country == 'PRC':

	if age >= 18:

		print('you can drive')

	else:

		print('piss off')

elif country == 'USA':

	if age >= 16:

		print('you can drive')

	else:

		print('piss off')

else:

	print('piss off')