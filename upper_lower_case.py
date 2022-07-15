
def upperlower(string):

	upper = 0
	lower = 0

	for i in range(len(string)):
		
	
		if (ord(string[i]) >= 97 and
			ord(string[i]) <= 122):
			lower += 1

		# For upper letters
		elif (ord(string[i]) >= 65 and
			ord(string[i]) <= 90):
			upper += 1

	print('Lower case characters = %s\n', (nam)%lower,
		  'Upper case characters = %s',(nam) %upper)

nam = str(input("Enter any number to find factorial: "))
# string = 'GeeksforGeeks is a portal for Geeks'
upperlower(str)
