'''
Goals:
    Making a Quiz program using classes
    Learning how to create and use classes
'''

from QuestionsEngine import quesEngine as QE

class User():
    
    id = "000"
    name = "John Doe"
    score = 0
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
            

    def start(self):
        qe = QE()
        self.score = qe.userScore
        print(f"Score: {self.score}\nPercentage: {(self.score/12)*100}") 
        

        
    
                

user_1 = User("Garry", "012")

user_1.start()