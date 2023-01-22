import ezgmail, os
import datetime
import re
import time

os.chdir('/Users/nicolasrobinson/Downloads')
ezgmail.init()

unreadThreads = ezgmail.unread()
unreadThreadsToday = [thread for thread in unreadThreads if thread.messages[0].timestamp.date() == datetime.date.today()]

if len(unreadThreadsToday) == 0:
	print("\n")
	print("No emails today! Relax!", end='\r')
	time.sleep(2)


	countdown = 5
	while countdown != 0:
		leaving_msg = "Logging off in {countdown}...".format(countdown=countdown) + " "*5
		print(leaving_msg, end='\r')
		# add moving dots
		countdown -= 1
		time.sleep(1)
	quit()

print("\n")
print("Emails from these beautiful people:")
print("\n")

i = 0
for thread in unreadThreadsToday:
	i += 1
	rgx = re.compile(r"<(.+?)>")
	e_address = rgx.search(thread.messages[0].sender)
	print(i, e_address.group(1))

print("\n")


if input("Would you like to open any emails this morning? (y/n): ") == "y":
	while(True):
		print(unreadThreadsToday[int(input("Enter the email index: "))-1].messages[0].subject)
		if input("Finished? (y/n): ") == "y":
			break
else:
	if input("Mark as read? (y/n): ") == "y":
		ezgmail.markAsRead(unreadThreadsToday)
		quit()
	else:
		print("Good day. See you tomorrow.")
		quit()






