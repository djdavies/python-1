#!/usr/bin/env python

import random

score = 0
while score < 10:
    if score > 0:
        print "----------\n", "Score: ", score, "\n----------"
    target = random.randint(0,1000)
    guess = 
    while guess != target:
        try:
            guess = int(raw_input('Guess a number:\t'))
        except ValueError:
            print "\t\tPlease enter a number."
            continue
        if guess < target:
            print "\t\tToo low!"
        elif guess > target:
            print "\t\tToo high!"
        elif guess == target:
            print "\t\tWooo you got it! SWEET! AMEZZING!"
            score += 1
            
print "Game over."
