import webbrowser
import time

breaktime = 0

while breaktime < 4:
	time.sleep(5)
	webbrowser.open("https://www.youtube.com/watch?v=oh2LWWORoiM")
	breaktime = breaktime + 1
