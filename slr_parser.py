#!/usr/bin/python
import sys
class Stack:
	def __init__(self):
	 self.items = []
	 return

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

	def printStack(self):
		for i in range(len(self.items)):
			sys.stdout.write(str(self.items[i])+" ")
		return ""




class Lex:
	delim = [" ",",",";","{","}","(",")","$"]
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

	STATES = 35
	COLUMN = 21

	ACTION = "None"
	SYMBOLS = []
	
	NO_SYM = [2,2,1,1,4,7,3,3,3,1,3,3,1,3,1]
	TOKENS = ['id',';','=','{','}','(',')','relop','if','+','-','*','/','$','S','A','I','C','E','T','F']
	RULES = ["S->AS","S->IS","S->A","S->I","A->id=E;","I->if(C){S}","C->id relop id","E->E+T","E->E-T","E->T","T->T*F","T->T/F","T->F","F->(E)","F->id"]
    
	'''
	TOKENS = ['id','+','*','(',')','$','E','T','F']
	RULES = ['E->E+T','E->T','T->T*F','T->F','F->(E)','F->id']
	NO_SYM = [3,1,3,1,3,1]
	'''


	'''
	actionTable = [
		['s5','-','-','s4','-','-',1,2,3],
		['-','s6','-','-','-','acc',-1,-1,-1],
		['-','r2','s7','-','r2','r2',-1,-1,-1],
		['-','r4','r4','-','r4','r4',-1,-1,-1],
		['s5','-','-','s4','-','-',8,2,3],
		['-','r6','r6','-','r6','r6',-1,-1,-1],
		['s5','-','-','s4','-','-',-1,9,3],
		['s5','-','-','s4','-','-',-1,-1,10],
		['-','s6','-','-','s11','-',-1,-1,-1],
		['-','r1','s7','-','r1','r1',-1,-1,-1],
		['-','r3','r3','-','r3','r3',-1,-1,-1],
		['-','r5','r5','-','r5','r5',-1,-1,-1]
	]

	'''
	actionTable = [

		['s4','0','0','0','0','s9','0','0','s5','0','0','0','0','0','1','2','3','0','6','7','8'],
		['0','0','0','0','0','0','0','0','0','0','0','0','0','acc','0','0','0','0','0','0','0'],
		['s11','0','0','0','r3','0','0','0','s5','0','0','0','0','r3','10','2','3','0','0','0','0'],
		['s11','0','0','0','r4','0','0','0','s5','0','0','0','0','r4','12','2','3','0','0','0','0'],
		['0','r15','s13','0','0','0','r15','s14','0','r15','r15','r15','r15','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','s15','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','0','0','s16','s17','0','0','0','0','0','0','0','0','0','0'],
		['0','r10','0','0','0','0','r10','0','0','r10','r10','s18','s19','0','0','0','0','0','0','0','0'],
		['0','r13','0','0','0','0','r13','0','0','r13','r13','r13','r13','0','0','0','0','0','0','0','0'],
		['s21','0','0','0','0','s9','0','0','0','0','0','0','0','0','0','0','0','0','20','7','8'],
		['0','0','0','0','r1','0','0','0','0','0','0','0','0','r1','0','0','0','0','0','0','0'],
		['0','0','s13','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','r2','0','0','0','0','0','0','0','0','r2','0','0','0','0','0','0','0'],
		['s21','0','0','0','0','s9','0','0','0','0','0','0','0','0','0','0','0','0','22','7','8'],
		['s23','0','0','0','0','0','r7','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['s25','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','24','0','0','0'],
		['s21','0','0','0','0','s9','0','0','0','0','0','0','0','0','0','0','0','0','0','26','8'],
		['s21','0','0','0','0','s9','0','0','0','0','0','0','0','0','0','0','0','0','0','27','8'],
		['s21','0','0','0','0','s9','0','0','0','0','0','0','0','0','0','0','0','0','0','0','28'],
		['s21','0','0','0','0','s9','0','0','0','0','0','0','0','0','0','0','0','0','0','0','29'],
		['0','0','0','0','0','0','s30','0','0','s16','s17','0','0','0','0','0','0','0','0','0','0'],
		['0','r15','0','0','0','0','r15','0','0','r15','r15','r15','r15','0','0','0','0','0','0','0','0'],
		['0','s31','0','0','0','0','0','0','0','s16','s17','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','r7','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','s32','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','0','0','0','0','0','0','s14','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['0','r8','0','0','0','0','r8','0','0','r8','r8','s18','s19','0','0','0','0','0','0','0','0'],
		['0','r9','0','0','0','0','r9','0','0','r9','r9','s18','s19','0','0','0','0','0','0','0','0'],
		['0','r11','0','0','0','0','r11','0','0','r11','r11','r11','r11','0','0','0','0','0','0','0','0'],
		['0','r12','0','0','0','0','r12','0','0','r12','r12','r12','r12','0','0','0','0','0','0','0','0'],
		['0','r14','0','0','0','0','r14','0','0','r14','r14','r14','r14','0','0','0','0','0','0','0','0'],
		['r5','0','0','0','r5','0','0','0','r5','0','0','0','0','r5','0','0','0','0','0','0','0'],
		['0','0','0','s33','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['s11','0','0','0','0','0','0','0','s5','0','0','0','0','0','34','2','3','0','0','0','0'],
		['0','0','0','0','s35','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
		['r6','0','0','0','r6','0','0','0','r6','0','0','0','0','r6','0','0','0','0','0','0','0']

	]
	




	def printSymbols(self):
		for i in range(len(self.SYMBOLS)):
			sys.stdout.write(str(self.SYMBOLS[i]))
		return ""


	def initHash(self):
		k=0
		for i in range(self.STATES+1):
			for j in self.TOKENS:
				if k%self.COLUMN == 0:
					k=0
				#print k,i,j," : ",self.actionTable[i][k]
				self.MAIN_TABLE[i,j] = self.actionTable[i][k]
				k+=1



	def F(self,state,curr):
		#print state,curr,self.MAIN_TABLE[state,curr]
		return self.MAIN_TABLE[state,curr]


	def REDUCE(self,symbol,STACK):
		Status = self.F(STACK.peek(),symbol)
		STACK.push(int(Status))
		return

	def actionOn(self,STACK):
		#print "PARSER : ",self.CURRENT
		Status = self.F(STACK.peek(),self.CURRENT)
		if  Status == "acc":
			print "\t\tACTION :  ACCEPT\n\t---------------------------------------\n\n"

		if "s" in Status:
			self.ACTION = "shift"
			print "\t\tACTION : ",self.ACTION,"\n\t---------------------------------------\n\n"
			#print "F : ",self.CURRENT
			STACK.push(int(Status[1:]))
			
			#print "PRINTING STACK : "
			#STACK.printStack()
			#print " \n\n"
			print "\n\t---------------------------------------\n\t\tSYMBOL : ",self.CURRENT,"\n\t\tSTACK  :  ",S.printStack()
		elif "r" in Status:

			#print "R : ",self.CURRENT
			#print "Reduce : ",Status[1]
			prod = self.RULES[int(Status[1:])-1]
			self.ACTION = "reduce by "+prod
			print "\t\tACTION : ",self.ACTION,"\n\t---------------------------------------\n\n"
			
			prod = prod.split('->')
			RHS = prod[0]
			LHS = prod[1]
			#print "Prod : ",LHS,len(LHS)
			
			for i in range(self.NO_SYM[int(Status[1:])-1]):
				STACK.pop()

			#print "\t",S.printStack(),"\t\t",L.printSymbols(),"\t\t",L.ACTION
			#print "STACK BEFORE REDUCE: "
			#STACK.printStack()
			self.REDUCE(RHS,STACK)
			#print "\nSTACK AFTER REDUCE : "
			#STACK.printStack()
			#print " \n\n"
			#print "\t",S.printStack(),"\t\t\t",self.ACTION
			print "\n\t---------------------------------------\n\t\tSYMBOL : ",self.CURRENT,"\n\t\tSTACK  :  ",S.printStack()
			self.actionOn(STACK)
		

		

		


	def parser(self,token,STACK):
		#print token
		#if token in self.identifier:
			
		self.SYMBOLS.append(token)
		self.CURRENT = token
		self.actionOn(STACK)


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
			



			if ch in self.delim or ch in self.operator: 
				#print "Lex : ",lexeme

				if lexeme != "":
					found = self.find(lexeme)
					if found != "1":
						self.lexeme_list.append(lexeme+" \t "+found)
						final_lexa = lexeme
						#print "LexA : ",final_lexa
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
					#print "LexB : ",final_lexb
					self.parser(final_lexb,S)
					final_lexb = ""

				lexeme = ""
				

			else:
				lexeme+= ch


			
			j+=1
			
			
L = Lex()

fo = open("example.c","r")

S = Stack()
S.push(0)
L.initHash()
'''
L.parser('id',S)
print S.peek()
L.F(S.peek(),'id')
'''

print "\n\t---------------------------------------\n\t\tSYMBOL : ",L.CURRENT,"\n\t\tSTACK  :  ",S.printStack()
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
