import time
timestamp=time.strftime('%H')
hour=int(timestamp)
if hour < 12:
    print("good morning mam")
elif hour < 17:
    print("good afternoon mam")
elif hour <  20:
    print("good evening mam")
else:
    print("good night mam")           