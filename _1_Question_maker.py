######## Quiz Maker #########
#Make an application which takes various questions from a file, picked randomly, and puts together a quiz for students. 
#Each quiz can be different and then reads a key to grade the quizzes.

import random
from random import choice

class Question:
     def __init__(self,prompt,answer):
            self.prompt = prompt
            self.answer = answer
         
            
            
question_prompts =open (r"F:\Vaibhavi DATA\Python certification preperation\Mini_Project-12HR_Drill\_2_Questions.txt") 
content = question_prompts.read()


questions = [
    Question(content[1:145],"a"),
    Question(content[145:265],"b"),
    Question(content[265:383],"c"),
    Question(content[383:527],"d"),
    Question(content[527:640],"b"),
    Question(content[640:775],"a"),
    Question(content[775:924],"b"),
    Question(content[924:1042],"c"),
    Question(content[1042:1168],"a"),
    Question(content[1168:1300],"b"),
    
]                          
random.shuffle(questions)
             

def run_quiz(questions):
    score=0
    for question in questions:
        answer= input(question.prompt)
        if answer == question.answer:
             score += 1
    print("you got", score, "out of", len(questions))
run_quiz(questions)
