###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("summer")
q1 = codesters.Square(100,100,200,'pink')
q2 = codesters.Square(-100,100,200,'white')
q3 = codesters.Square(-100,-100,200,'pink')
q4 = codesters.Square(100,-100,200, 'white')
s1 = codesters.Sprite("cross.webp", 100, 100)
s1.set_size(0.2)
s2 = codesters.Sprite("flower2.gif", -100, -100)
s2 .set_size(0.7)
s3 = codesters.Sprite("cool_dog.png", 100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("cardinal", -100, 100)
s4.set_size(0.4)
message1 = codesters.Text("Ephrata Dereje Melesse",0,220,"red")
s4.set_size(0.4)
message2 = codesters.Text("Live,Love,Laugh",0,-200,"black")