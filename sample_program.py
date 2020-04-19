from viper import *
from viper_dev import *

Say("Hello")

addition = Add(1,2)
Say(addition)

subtraction = Subtract(3,2)
Say(subtraction)

multiplication = Multiply(1,2)
Say(multiplication)

division = Divide(1,2)
Say(division)

randNum = Random(1,10)
Say(randNum)

NewDrawCanvas()
DrawSquare(10)
Wait(1)
ClearDrawCanvas()
DrawCircle(5)
MovePen(10,-40)
DrawLine(10)
DrawOddStar(6)
ChangeColor("blue")
EndDrawCanvas()

GetSource(Add)