# git-exercise-01.py
import turtle
# TEAM LEADER:
# implement this function so that it returns copy of string_arg reversed
def reverseWord(string_arg):
	reverser = string_arg[::-1]
	return reverser

# TEAM MEMBER:
# implement this function so that it returns the frequency of query in string_arg
def countFreq(string_arg, query):
     for i in string_arg:
         ct = string_arg.count(query)
     return ct

def adding_strings(string_arg):
	new_string = string_arg + 'livingthelife'
	return new_string
 
def main():
	data = 'guidorossumwashere'
	print 'REVERSED ==>', reverseWord(data)
	print 'FREQUENCY OF s IN', data, '==>', countFreq(data, 's')
	print 'NEW STRING ==>', adding_strings(data)
if __name__ == "__main__": 
	main()
