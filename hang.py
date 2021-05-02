import random  
import time
import unidecode
import os 

class Hangman: 
    def __init__(self): 
        print("****************************"+"\n")
        print("Welcome to the Hangman Game")
        print("\n"+"****************************")
        time.sleep(3.6)
        os.system("cls")
        self.win = False
        self.lives = 0
        # self.level = int(input("Please choose a difficulty:\n-1 for easy\n-2 for medium\n-3 for hard\n "))
        # self.setLives(self.level)
        self.word = [i for i in self.load() if i!="\n"]
        self.wordArray = [" - " for i in range(len(self.word)) if i!="\n"]
        self.state =""
        self.state = self.state.join(self.wordArray)

    def setLives(self,i):
        if i == 1:
            self.lives = 30
        elif i == 2:
            self.lives = 15
        else:
            self.lives = 10



    def load(self):
        words = []
        with open("./archivos/data.txt","r", encoding="utf-8") as f:
            for line in f:
                s = unidecode.unidecode(line)
                words.append(s.lower())
        return words[random.randint(0, len(words)-1)]

    def guess(self, a):
        if a in self.word:
            pos = [i for i in range(len(self.word)) if self.word[i]==a]  
            for i in pos:
                self.wordArray[i]=a
                self.state =""
                self.state = self.state.join(self.wordArray)
        self.lives = self.lives - 1

        # if self.lives == 0:
        #     print("YOU LOST")
            
        if " - " not in self.wordArray:
            print("YOU WON YAYYYYYYYYY")
            self.win = True
    
    def play(self):
        while not self.win:
            # print(f'You got {self.lives} lives left')    
            print("Guess the word")
            print()
            print(self.state)
            print("\n")
            a = input("Type a letter: ")
            self.guess(a)
            os.system("cls")
        # print("YOU WON")
    
    


       
    
    def state(self): 
         print("getter method called") 
         return self.state 
       
  
    def state(self, a): 
         print("setter method called") 
         self.state = a
        

def run():
   h = Hangman()
   h.play()

if __name__ == "__main__":
    run()