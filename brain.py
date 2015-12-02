#brain.py
import sys
#array of 30k	

#+ increment - decrement > next cell < prev cell . print ascii val at current cel , read a single input into cell [ if cal at currnet cel is 0, skip to ]. else next
#] if val is 0, skip to next instruction, else move backwards

#if(sys.argv)


def set_search(set, num): #returns whether num is in set or sets within set
	for c in set:
		if num in c:
			return True
	return False

def del_incompat(program):
	counter = 0
	for i in range(0,len(program)):
		if not program[i-counter] in "+-><.,[]":
			program = removeFromString(program,i-counter)
			counter += 1
	return program

def removeFromString(text, index): #simply remove the character at index
	return text[0:index] + text[index+1:]


def pair_brackets(program,pairs):
	#do it recursively: 
	i = 0
	flag = False
	while i < len(program):
		if program[i] == "[" and not set_search(pairs,i):
			tmp = i
			flag = True
		elif program[i] == "]" and not set_search(pairs,i):
			pairs.append((tmp,i))
			i = len(program)
		i+=1
	if flag:
		return pair_brackets(program, pairs)
	else:
		return pairs

def get_cb(pairs,index): #get corresponding bracket, given an index. returns -1 if no such corresponding bracket exists
	for c in pairs:
		if c[0] == index:
			return c[1]
		elif c[1] == index:
			return c[0]
	return -1

def main():
	print("Brainf*** Interpreter v 1.0")
	try:
		zzz=sys.argv[1]
	except IndexError:
		print("Please drag your brainf*** file onto brainf***.bat to be compiled. Alternatively, provide the filepath as 1st arg")
		sys.exit()
	f = open(sys.argv[1],'rt')
	program = f.read()
	pairs = []
	program = del_incompat(program)

	pairs = pair_brackets(program,[])
	p = 0 #pointer in cell of integers
	i = 0 #interpreter pointer
	li = [0]*30000
	while i < len(program):
		if program[i] == "+":
			li[p] += 1
		elif program[i] == "-":
			li[p] -= 1
		elif program[i] == ">":
			p += 1
		elif program[i] == "<":
			p -= 1
		elif program[i] == ".":
			sys.stdout.write(chr(li[p]))
		elif program[i] == ",":
			li[p] = ord(input())
		elif program[i] == "[":
			if li[p] == 0:
				i=get_cb(pairs,i)
		elif program[i] == "]":
			if li[p] != 0:
				i=get_cb(pairs,i)
		i+=1
main()

