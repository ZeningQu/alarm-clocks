from playsound import playsound
import schedule
import time

def ring():
  playsound('./sounds/bell.mp3')

schedule.every().day.at("03:00").do(ring) # wake up
schedule.every().day.at("03:30").do(ring) # quiet time
schedule.every().day.at("04:00").do(ring) #
schedule.every().day.at("04:20").do(ring) #
schedule.every().day.at("04:40").do(ring) #
schedule.every().day.at("04:50").do(ring) #
schedule.every().day.at("05:35").do(ring) #
schedule.every().day.at("05:45").do(ring) #
schedule.every().day.at("06:30").do(ring) #
schedule.every().day.at("06:40").do(ring) #
schedule.every().day.at("07:25").do(ring) #
schedule.every().day.at("07:35").do(ring) #
schedule.every().day.at("08:20").do(ring) #
schedule.every().day.at("08:30").do(ring) #
schedule.every().day.at("09:15").do(ring)
schedule.every().day.at("10:15").do(ring)
schedule.every().day.at("11:00").do(ring)
schedule.every().day.at("11:20").do(ring)
schedule.every().day.at("12:05").do(ring)
schedule.every().day.at("12:15").do(ring)
schedule.every().day.at("13:00").do(ring)
schedule.every().day.at("13:10").do(ring)
schedule.every().day.at("13:55").do(ring)
schedule.every().day.at("14:05").do(ring)
schedule.every().day.at("14:50").do(ring)
schedule.every().day.at("15:30").do(ring)
schedule.every().day.at("17:30").do(ring)
schedule.every().day.at("18:15").do(ring)
schedule.every().day.at("19:00").do(ring)

while True:
  schedule.run_pending()
  time.sleep(1)
