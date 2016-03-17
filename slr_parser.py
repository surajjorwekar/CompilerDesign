#!/usr/bin/python
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


class Lex:
	delim = [" ",",",";","{","}","(",")","#"]
	operator = ["+","-","/","*","=","&&","||","&","|","!","=="]

	keywords=["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while"]
	lexeme_list = []
	identifier = []
	invalid_identifier = []
	invalid_operator = []
	output = []
	comment = 0
	CURRENT=""
	MAIN_TABLE = {}

	actionTable = [
		['s5','-','-','s4','-','-'],
		['-','s6','-','-','-','acc'],
		['-','r2','s7','-','r2','r2'],
		['-','r4','r4','-','r4','r4'],
		['s5','-','-','s4','-','-'],
		['-','r6','r6','-','r6','r6'],
		['s5','-','-','s4','-','-'],
		['s5','-','-','s4','-','-'],
		['-','s6','-','-','s11','-'],
		['-','r1','s7','-','r1','r1'],
		['-','r3','r3','-','r3','r3'],
		['-','r5','r5','-','r5','r5']
	]

	

	gotoTable = [
		[1,2,3],
		[-1,-1,-1],
		[-1,-1,-1],
		[-1,-1,-1],
		[8,2,3],
		[-1,-1,-1],
		[-1,9,3],
		[-1,-1,10],
		[-1,-1,-1],
		[-1,-1,-1],
		[-1,-1,-1],
		[-1,-1,-1]

	]
	

	def initHash(self):
		k=o=j=0;
		l['id','+','*','(',')','$','E','T','F']

		for i in self.actionTable:
			data = i[j]
			if o == len(l):
				o=0
			self.MAIN_TABLE[k,l[o]]
			o+=1
			k+=1
			j+=1



	def F(self,state,curr):
		self.actionTable[]
		return

	def G(self,state,curr):
		return


	def parser(self,token,STACK):
		CURRENT = token
		Status = self.F(STACK.peek(),CURRENT)

		if "s" in Status:
			Status = Status[1]
			STACK.push(Status)

		elif "r" in Status:
			print "None"
		

		#print STACK.peek(),token

	def isEnd(self,lexeme):
		if lexeme in self.delim or lexeme in self.operator :
			return False
		else:
			return True

	def isKeyword(self,lexeme):
		if lexeme in self.keywords:
			return True
		else:
			return False

	def isIdentifier(self,lexeme):

		if lexeme[0].isdigit():
			return False


		for i in range(len(lexeme)):
			ch = lexeme[i]
			if ch.isalpha() or ch == "_" or ch.isdigit():
				flag = 0
			else:
				flag = 1

		if flag == 0:
			return True
		else:
			return False
		



	def find(self,lexeme):
		if lexeme.isdigit():
			return "Constant"

		if self.isKeyword(lexeme):
			return "Keyword"

		else: 
			if self.isIdentifier(lexeme):
				if lexeme not in self.identifier:
					self.identifier.append(lexeme)
					return "Identfier"
				else:
					return "Identfier"
			else:
				if lexeme not in self.invalid_identifier:
					self.invalid_identifier.append(lexeme)
					
				return "Invalid Operator"



	def splitToken(self,data,S):
		lexeme = ""
		j=0
		length = len(data)
		
		while j != length:
			ch = data[j]
			#print ch



			if ch in self.delim or ch in self.operator: 
				#print "Lex : ",lexeme

				if lexeme != "":
					found = self.find(lexeme)
					if found != "1":
						self.lexeme_list.append(lexeme+" \t "+found)
						final_lexa = lexeme
						self.parser(final_lexa,S)
						final_lexa = ""
				if ch != "" and ch != " ":
					if ch in self.delim:
						self.lexeme_list.append(ch+" \t Delimiter")
						final_lexb = ch
					else:
						if ch+data[j+1] in self.operator:
							self.lexeme_list.append(ch+data[j+1]+" \t Operator")
							final_lexb = ch+data[j+1]
							j+=1
						elif ch in self.operator:
							self.lexeme_list.append(ch+" \t Operator")
							final_lexb = ch
						else:
						    self.invalid_operator.append(ch)
					self.parser(final_lexb,S)
					final_lexb = ""

				lexeme = ""
				

			else:
				lexeme+= ch


			
			j+=1
			
			
L = Lex()

fo = open("example.c","r")

S = Stack()
S.push("0")
while 1:

	data = fo.readline().strip()
	#print "c:",L.comment
	if "/*" in data or L.comment == 1:
		#print data
		L.comment = 1
		if "*/" in data:
			L.comment = 0
	elif "//" in data:
		continue
	else:
		L.splitToken(data,S)
		if data == "":
			break
'''
print "\n\n    -------------------------\n        LEXEME    TOKEN\n    -------------------------"
for ch in L.lexeme_list:		
	print "\t",ch

print "\n\n    -------------------------\n      SYMBOL TABLE\n    -------------------------"

for ch in L.identifier:	
	print "\t",ch

print "\n\n    -------------------------\n      INVALID IDENTIFIER\n    -------------------------"

for ch in L.invalid_identifier:
	print "\t",ch

print "\n\n"
'''
