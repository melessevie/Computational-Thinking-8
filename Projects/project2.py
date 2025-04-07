# Beginning: Create variables 
Chocolate_points = 0
Vanilla_points = 0


answer = input ("Are you A) a Chocolate ice cream person, or B) a Vanilla ice cream person?")
if answer == "A":
      Chocolate_points += 1
elif answer == "B" :
       Vanilla_points   += 1

# Medium: As questions
answer = input ("are you A) a quite person, or B) a loud person?") 
if answer == "A":
      Chocolate_points += 1
elif answer == "B" :
       Vanilla_points   += 1


answer = input ("are you A) a confident person, or B) a shy person?") 
if answer == "A":
      Chocolate_points += 1
elif answer == "B" :  


      answer = input ("are you A) a Vanilla perfume person, or B) a strong sexy perfume person?")
if answer == "A":
      Chocolate_points += 1
elif answer == "B" :


      answer = input ("are you A) a Introverted person, or B) a Extroverted person?")
if answer == "A":
      Chocolate_points += 1
elif answer == "B" :


# End: Determine results
      if Vanilla_points > Chocolate_points:
            print("you are a Vanilla person")
elif Chocolate_points > Vanilla_points:
      print("you are a Chocolate person")
elif Vanilla_points == Chocolate_points:
      print("you are both Vanilla and Chocolate at the same time")