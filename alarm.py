from playsound import playsound
import schedule
import time

def ring():
  playsound('./sounds/bell.mp3')

schedule.every().day.at("03:00").do(ring) # wake up, tea, breakfast, tea (30 min)
schedule.every().day.at("03:30").do(ring) # quiet time (30 min)
schedule.every().day.at("04:00").do(ring) # pray (20 min)
schedule.every().day.at("04:20").do(ring) # snack, shower, brush, floss, trays (20 min)
schedule.every().day.at("04:40").do(ring) # panda daily (10 min)
schedule.every().day.at("04:50").do(ring) # L1 (45 min)
schedule.every().day.at("05:35").do(ring) # break (10 min)
schedule.every().day.at("05:45").do(ring) # L2 (45 min)
schedule.every().day.at("06:30").do(ring) # break (10 min)
schedule.every().day.at("06:40").do(ring) # L3 (45 min)
schedule.every().day.at("07:25").do(ring) # break (10 min)
schedule.every().day.at("07:35").do(ring) # L4 (45 min)
schedule.every().day.at("08:20").do(ring) # cook, lunch, dishes (1 hr)
schedule.every().day.at("09:20").do(ring) # nap, Bible (45 min)
schedule.every().day.at("10:05").do(ring) # wake up, snack, rinse, brush, floss, trays (20 min)
schedule.every().day.at("10:25").do(ring) # L5 (45 min)
schedule.every().day.at("11:10").do(ring) # break (10 min)
schedule.every().day.at("11:20").do(ring) # L6 (45 min)
schedule.every().day.at("12:05").do(ring) # break (10 min)
schedule.every().day.at("12:15").do(ring) # L7 (45 min)
schedule.every().day.at("13:00").do(ring) # iron, vc, dinner, dishes, brush, floss, trays (40 min)
schedule.every().day.at("13:40").do(ring) # L8 (45 min)
schedule.every().day.at("14:25").do(ring) # break (10 min)
schedule.every().day.at("14:35").do(ring) # L9 (45 min)
schedule.every().day.at("15:20").do(ring) # break (10 min)
schedule.every().day.at("15:30").do(ring) # L10 (45 min)
schedule.every().day.at("16:15").do(ring) # walk (1 hr)
schedule.every().day.at("17:15").do(ring) # shower, cream (45 min)
schedule.every().day.at("18:00").do(ring) # read (1 hr)
schedule.every().day.at("19:00").do(ring) # sleep, Bible (8 hr)

while True:
  schedule.run_pending()
  time.sleep(1)
