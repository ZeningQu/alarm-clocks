from playsound import playsound
import schedule
import time

def ring():
  playsound('./sounds/bell.mp3')

schedule.every().day.at("22:15").do(ring)

while True:
  schedule.run_pending()
  time.sleep(1)
