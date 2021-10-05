from playsound import playsound
import schedule
import time

def ring():
  playsound('./sounds/bell.mp3')

schedule.every().day.at("03:00").do(ring) # wake up
schedule.every().day.at("03:30").do(ring) # quiet time
schedule.every().day.at("04:00").do(ring) # pray
schedule.every().day.at("04:20").do(ring) # snack
schedule.every().day.at("04:40").do(ring) # panda daily
schedule.every().day.at("04:50").do(ring) # L1
schedule.every().day.at("05:35").do(ring) # break
schedule.every().day.at("05:45").do(ring) # L2
schedule.every().day.at("06:30").do(ring) # break
schedule.every().day.at("06:40").do(ring) # L3
schedule.every().day.at("07:25").do(ring) # break
schedule.every().day.at("07:35").do(ring) # L4
schedule.every().day.at("08:20").do(ring) # cook lunch
schedule.every().day.at("09:20").do(ring) # nap, Bible
schedule.every().day.at("10:05").do(ring) # wake up, snack
schedule.every().day.at("10:25").do(ring) # L5
schedule.every().day.at("11:10").do(ring) # break
schedule.every().day.at("11:20").do(ring) # L6
schedule.every().day.at("12:05").do(ring) # break
schedule.every().day.at("12:15").do(ring) # L7
schedule.every().day.at("13:00").do(ring) # iron, vc, dinner
schedule.every().day.at("13:40").do(ring) # L8
schedule.every().day.at("14:25").do(ring) # break
schedule.every().day.at("14:35").do(ring) # L9
schedule.every().day.at("15:20").do(ring) # break
schedule.every().day.at("15:30").do(ring) # L10
schedule.every().day.at("16:15").do(ring) # walk
schedule.every().day.at("17:15").do(ring) # shower
schedule.every().day.at("18:00").do(ring) # read
schedule.every().day.at("19:00").do(ring) # sleep

while True:
  schedule.run_pending()
  time.sleep(1)
