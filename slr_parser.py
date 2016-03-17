#!/usr/bin/python

class Lex:
	delim = [" ",",",";","{","}","(",")"]
	operator = ["+","-","/","*","=","&&","||","&","|","!","=="]

	keywords=["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while"]
	lexeme_list = []
	identifier = []
	invalid_identifier = []
	invalid_operator = []
	output = []
	comment = 0

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



	def splitToken(self,data):
		lexeme = ""
		j=0
		length = len(data)
		while j != length:
			ch = data[j]
			#print j,ch



			if ch in self.delim or ch in self.operator: 
				#print "Lex : ",lexeme
				if lexeme != "":
					found = self.find(lexeme)
					if found != "1":
						self.lexeme_list.append(lexeme+" \t "+found)

				if ch != "" and ch != " ":
					if ch in self.delim:
						self.lexeme_list.append(ch+" \t Delimiter")
					else:
						if ch+data[j+1] in self.operator:
							self.lexeme_list.append(ch+data[j+1]+" \t Operator")
							j+=1
						elif ch in self.operator:
							self.lexeme_list.append(ch+" \t Operator")
						else:
						    self.invalid_operator.append(ch)
				lexeme = ""

			else:
				lexeme+= ch

			j+=1
			
			
L = Lex()
fo = open("example.c","r")


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
		L.splitToken(data)
		if data == "}":
			break

print "\n\n    -------------------------\n        LEXEME    TOKEN\n    -------------------------"
for ch in L.lexeme_list:		
	print "\t",ch

print "\n\n    -------------------------\n      SYMBOL TABLE\n    -------------------------"

for ch in L.identifier:	
	print "\t",ch

print "\n\n    -------------------------\n      INVALID IDENTIFIER\n    -------------------------"

for ch in L.invalid_identifier:
	print "\t",ch
'''
print "\n\n    -------------------------\n      INVALID OPERATOR\n    -------------------------"

for ch in L.invalid_operator:
	print "\t",ch
	'''
print "\n\n"
