import random

def hard_level():
		correct = 0
		for i in range(10):
			  
			  
			  # every quotation will have a random number from 1 to 9 and it will choose randomly from Division or Multiplication.
			  
			  num1 = random.randint(1,9)
			  num2 = random.randint(1,9)
			  operation = random.choice(['*', '/'])
			  if operation == '*' :
			  	answer = num1 * num2
			  if operation == '/' :
			  	answer = round(num1 / num2, 2)
			  	
			  	#here we make a list of falls choices, including the correct one.
			  	
			  choices =[answer]
			  while len(choices) <4 :
			  	incorrect  = random.randint(-5,5)
			  	incorrect_choice = round(answer +incorrect,2)
			  	if incorrect_choice not in choices and incorrect_choice >= 0 :
			  		choices.append(incorrect_choice )
			  		random.shuffle(choices)
			  		answer_index = choices.index(answer)
			  		
			  # here we change the operation "/" to "÷" to facilitate it  to the the user.
			  
			  if operation == "/" :
			  	operation = "÷"
			 
			  print(f" {i +1} what is the answer for {num1}{operation}{num2} ?")
			  print(choices)
			  user_answer = int(input(" "))
			  user_answer -=1
			  if user_answer == answer_index:
			  	correct +=1
			  	print(" correct")
			  else:
			  	print(f" wrong, the correct answer is {answer_index} wich is {answer}")
		if correct >=7:
			print(f" congratulation,  you scored {correct}")
		else:
			print(f" sorry you scored {correct} correct, good luck next time")
			regame = input(" print yes to play the hard level again, and no to exit ")
			if regame == "yes" :
				hard_level()
			else:
				return
def main():
	print("Welcome in the math game")
	print(' ')
	print("This game contain 2 level, the first level is about 5 easy questions, and you have to scour more than 3 questions correct to pass to the next level")
	print(' ')
	print("let's start, good luck ")
	print(" ")
	correct = 0
	#here is the 5 easy questions, it's will start by choosing 2 random number and then will ask the user to answer it then compare the user answer with the correct answers 
	
	for i in range(5):
		num1 = random.randint(1,99)
		num2 = random.randint(1,99)
		correct_answers = num1 + num2
		print (f" {i +1} what is the answer for {num1} + {num2} ?")
		user_answer = int(input(" "))
		 
		if user_answer == correct_answers :
			print (" correct")
			print(" ")
			correct +=1
		else:
			print(f" wrong, the correct answer is ,{correct_answers}")
			print(" ")
	#if the user answered more then 4 questions correct he will pass to the next level
	
	#the next leve is multiple-choice questions 
	#the user will choice the place of the correct answer 
			
	if correct >=4 :
		correct = 0
		print("good job, you passed to the next level")
		print(" ")
		print("Welcome in the hard level")
		print("in this level you will face Divisio Multiplication in form of multiple-choice questions. you have to score more than 7 questions correct to win the game")
		print("good luck")
		hard_level()
		
	else:
		print("sorry you didn't pass to the next level, good luck next time")	  	

if __name__ == "__main__":
    main()