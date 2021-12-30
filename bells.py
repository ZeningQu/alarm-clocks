from playsound import playsound
import schedule
import time

def ring():
  playsound('./sounds/bell.mp3')

bells = [
'03:00',
'03:10',
'04:10',
'04:40',
'05:40',
'05:45',
'06:30',
'06:40',
'07:25',
'07:35',
'08:20',
'08:30',
'09:15',
'10:15',
'10:35',
'10:40',
'11:25',
'11:35',
'12:20',
'12:30',
'13:15',
'13:25',
'14:10',
'14:40',
'16:10',
'17:10',
'17:55',
'18:05',
'18:50'
]

for b in bells:
  schedule.every().day.at(b).do(ring)

while True:
  schedule.run_pending()
  time.sleep(1)
