# A pomodoro work/break timer that starts NOW!

from playsound import playsound
import time

def ring():
  playsound('./sounds/bell.mp3')

WORK = 45
BREAK = 10

while True:
  print('Focus time!')
  ring()
  time.sleep(WORK*60)

  print('Take a break :)')
  ring()
  time.sleep(BREAK*60)
