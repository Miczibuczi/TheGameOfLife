#!/usr/bin/env python
# coding: utf-8

import json
class TheGameOfLife:
    def __init__(self):
        try:
            with open("Jawor.txt", "r") as file:
                self.data = json.load(file)
        except:
            self.data = {"best":0, "best_chess":0, "best_spanish":0, "best_juggling":0, "FP":0, "DP":0, "lvl":0, "remained_exp":0}
        
    def chess_training(self):
        chess_training = input("Please enter how many minutes you have practiced chess today\n")
        if not chess_training:
            chess_training = 0
        return int(chess_training)

    def chess_games(self):
        chess_games = input("Please enter how many chess games you have played today\n")
        if not chess_games:
            chess_games = 0
        return int(chess_games)
    
    def spanish_talking(self):
        spanish_talking = input("Please enter how many minutes you have talked in Spanish today\n")
        if not spanish_talking:
            spanish_talking = 0
        self.data["FP"] += int(spanish_talking) // 60
        return int(spanish_talking)
    
    def learning_spanish_words(self):
        learning_spanish_words = input("Please enter how many minutes you have been learning spanish vocabulary today\n")
        if not learning_spanish_words:
            learning_spanish_words = 0
        return int(learning_spanish_words)
    
    def intense_spanish_learning(self):
        intense_spanish_learning = input("Please enter how many minutes you were intensly learning spanish today\n")
        if not intense_spanish_learning:
            intense_spanish_learning = 0
        return int(intense_spanish_learning)
    
    def euros_earned(self):
        euros_earned = input("Please enter how many € you have earned today\n")
        if not euros_earned:
            euros_earned = 0
        return int(euros_earned)
        
    def juggling_training(self):
        juggling_training = input("Please enter how many minutes you were training juggling today\n")
        if not juggling_training:
            juggling_training = 0
        return int(juggling_training)
    
    def books(self):
        books = input("Please enter how many books you have read today\n")
        if not books:
            books = 0
        return int(books)
    
    def running(self):
        running = input("Please enter how many kilometers you have run today\n")
        if not running:
            running = 0
        self.data["DP"] += int(running)//10
        return int(running)
    
    def fasting(self):
        fasting = input("Have you been fasting today?\n").lower()
        positive_answers = ["yes", "ye", "y", "yea"]
        return fasting in positive_answers
    
    def check_correctnes(self):
        self.output_string = f'So, you have practiced chess for {self.results["chess_training"]} minutes today, have played {self.results["chess_games"]} games. When it comes to spanish learning you were talking in spanish for {self.results["spanish_talking"]} minutes today. You also spent {self.results["learning_spanish_words"]} minutes learning vocabulary and {self.results["intense_spanish_learning"]} minutes intensly learning spanish. You also earned {self.results["euros_earned"]}€ and spent {self.results["juggling_training"]} minutes learning juggling. Morover you read {self.results["books"]} books and run for {self.results["running"]}km.'
        if self.results["fasting"]:
            self.output_string += "It was a fasting day as well today."
        else:
            self.output_string += "You weren't fasting today."
        print(self.output_string)
        check_correctnes = input("Is this correct?\n").lower()
        negative_answers = ["no", "n", "nope"]
        if check_correctnes in negative_answers:
            fix_it_method = None
            while fix_it_method not in self.functions:
                fix_it = input("Which data was entered incorrecly? You can write \"chess_training\", \"chess_games\", \"spanish_talking\", \"learning_spanish_words\", \"intense_spanish_learning\", \"euros_earned\", \"juggling_training\", \"books\", \"running\", \"fasting\"")
                fix_it_method = getattr(self, fix_it)
            self.results[fix_it_method.__name__] = fix_it_method()
            self.check_correctnes()
                
    def execute_the_code(self):
        self.functions = [self.chess_training, self.chess_games, self.spanish_talking, self.learning_spanish_words, self.intense_spanish_learning, self.euros_earned, self.juggling_training, self.books, self.running, self.fasting]
        self.results = {}
        for function in self.functions:
            while True:
                try:
                    self.results[function.__name__] = function()
                    break
                except:
                    print("Please enter an intiger value\n")
        self.check_correctnes()
        exp_sum = round(self.results["chess_training"]/10, 1)
        exp_sum += round(self.results["chess_games"], 1)
        exp_sum += round(self.results["spanish_talking"]*5/6, 1)
        exp_sum += round(self.results["learning_spanish_words"]*2/15, 1)
        exp_sum += round(self.results["intense_spanish_learning"]/10, 1)
        exp_sum += round(self.results["euros_earned"], 1)
        exp_sum += round(self.results["juggling_training"]/10, 1)
        exp_sum += round(self.results["books"]*30, 1)
        exp_sum += round(self.results["running"], 1)
        if self.results["fasting"]:
            exp_sum += 10
        self.data["best"] = max(self.data["best"], exp_sum)
        self.data["best_chess"] = max(self.data["best_chess"], round(self.results["chess_training"]/10 + self.results["chess_games"], 1))
        self.data["best_spanish"] = max(self.data["best_spanish"], round(self.results["spanish_talking"]*5/6 + self.results["learning_spanish_words"]*2/15 + self.results["intense_spanish_learning"]/10, 1))
        self.data["best_juggling"] = max(self.data["best_juggling"], round(self.results["euros_earned"] + self.results["juggling_training"]/10, 1))
        self.data["remained_exp"] = round(exp_sum+self.data["remained_exp"], 1)
        while self.data["remained_exp"] > 50*self.data["lvl"]+100:
            self.data["remained_exp"] = round(self.data["remained_exp"] - (50*self.data["lvl"]+100), 1)
            self.data["lvl"] += 1
            print(f'Congratulations, you have reached {self.data["lvl"]}lvl')
        print("Good job bro, your personal stats are as folows:")
        print(f'lvl: {self.data["lvl"]}lvl')
        print(f'exp: {self.data["remained_exp"]}/{50*self.data["lvl"]+100}')
        print(f'Personal best: {self.data["best"]}')
        print(f'Personal best chess: {self.data["best_chess"]}')
        print(f'Personal best spanish: {self.data["best_spanish"]}')
        print(f'Personal best juggling: {self.data["best_juggling"]}')
        print(f'FP: {self.data["FP"]}')
        print(f'DP: {self.data["DP"]}')
        with open("Jawor.txt", "w") as file:
              json.dump(self.data, file)
        input("Press Enter to exit the application.")
