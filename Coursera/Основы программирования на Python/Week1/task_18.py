time = int(input())
seconds = time % 60
minutes = (time - seconds) // 60 % 60
hours = (time - minutes - seconds) // 3600 % 24
if seconds < 10:
    seconds = '0' + str(seconds)
if minutes < 10:
    minutes = '0' + str(minutes)
print(hours, minutes, seconds, sep=':')
