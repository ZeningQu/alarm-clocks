# A pomodoro work/break timer that starts NOW!

from playsound import playsound
import time

def ring():
  playsound('./sounds/bell.mp3')

WORK = 45
BREAK = 10

while True:
  ring()
  time.sleep(WORK*60)

  ring()
  time.sleep(BREAK*60)
