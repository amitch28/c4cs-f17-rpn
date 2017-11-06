#!/usr/bin/env python3

import operator
import colorama
from colorama import init, Fore, Back
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			if result == 13:
				print(Fore.BLUE + "Go Blue")	
			stack.append(result)
		print(Fore.YELLOW)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	colorama.init()

	while True:
		result = calculate(input(Fore.RED + "rpn calc> "))
		print(Fore.GREEN)
		print("Result: ", result)

if __name__ == '__main__':
	main()
	
