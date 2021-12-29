from playsound import playsound
import schedule
import time

def ring():
  playsound('./sounds/bell.mp3')

time = [
"03:00",
"03:10",
"04:10",
"04:40",
"05:40",
"05:45",
"06:30",
"06:40",
"07:25",
"07:35",
"08:20",
"08:30",
"09:15",
"09:25",
"10:10",
"11:10",
"11:30",
"11:35",
"12:20",
"12:30",
"13:15",
"13:25",
"14:10",
"14:20",
"15:05",
"15:15",
"16:00",
"16:30",
"18:00",
"19:00"
]

for t in time:
  schedule.every().day.at(t).do(ring)

while True:
  schedule.run_pending()
  time.sleep(1)
