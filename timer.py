#!/usr/bin/python

from sys import argv
from datetime import timedelta

def	read_data():
	text = [""] * 7
	with open("timedata", 'r') as file:
		for i in range(7):
			text[i] = file.next()[:-1]
	return text

def	change_data(text):
	valid_data(text)
	text[argv[1] - 1] = argv[2]
	with open("timedata", 'w') as file:
		for i in range(7):
			file.write(text[i])
			file.write("\n")

def	valid_data(text):
	try:
		argv[1] = int(argv[1])
	except:
		print("First argument must be int")
		exit()
	if not 0 < argv[1] < 8:
		print("First argument must be in the range: 1 - 7")
		exit()
	try:
		spt = argv[2].index('.')
	except:
		print("String format for fill data must be: [hours].[minutes]")
		exit()
	if spt != argv[2].rindex('.'):
		print("String format for fill data must be: [hours].[minutes]")
		exit()
	try:
		hours = int(argv[2][:spt])
		minutes = int(argv[2][spt + 1:])
	except:
		print("Hours must be in the range: 0 - 24\nMinutes must be in the range: 0 - 59")
		exit()
	if not -1 < hours < 25 or not -1 < minutes < 60:
		print("Hours must be in the range: 0 - 24\nMinutes must be in the range: 0 - 59")
		exit()
	if hours == 24 and not minutes == 0:
		print("If hours equally 24, minutes must be equally 0")
		exit()

def	clear_data():
	with open("timedata", 'w') as file:
		file.write("0.0\n0.0\n0.0\n0.0\n0.0\n0.0\n0.0\n")

def	fill_daytime(text):
	day = [timedelta(hours=0, minutes=0)] * 7
	for i in range(7):
		spt = text[i].index('.')
		day[i] = timedelta(hours=int(text[i][:spt]), minutes=int(text[i][spt + 1:]))
	return day

def	def_timework(day):
	time_work = timedelta(hours=0, minutes=0)
	for i in day:
		time_work += i
	time_work = int(time_work.total_seconds())
	return time_work

def	def_timeremain(time_target, time_work):
	time_remain = time_target - time_work
	overflow = 0
	if time_remain < 0:
		overflow = 1
		time_remain = -time_remain
	return (time_remain, overflow)

def	write_daytime(text, day):
	for i in range(7):
		spt = int(text[i].find('.'))
		print("day {}: {} hours {} minutes".format(i + 1, text[i][:spt], text[i][spt + 1:]))

def	write_stats(time_target, time_work, time_remain, overflow):
	hours = 0
	while time_target >= 3600:
		time_target -= 3600
		hours += 1
	minutes = time_target / 60
	print("Target time:	{} hours {} minutes".format(hours, minutes))
	hours = 0
	while time_work >= 3600:
		time_work -= 3600
		hours += 1
	minutes = time_work / 60
	print("Working time:	{} hours {} minutes".format(hours, minutes))
	hours = 0
	while time_remain >= 3600:
		time_remain -= 3600
		hours += 1
	minutes = time_remain / 60
	if overflow == 0:
		print("\033[31mRemaining time:	{} hours {} minutes".format(hours, minutes))
	else:
		print("\033[32mOverflow time:	{} hours {} minutes".format(hours, minutes))

def	definding(text):
	time_target = int(timedelta(hours=50, minutes=0).total_seconds())
	# time_target = int(timedelta(hours=40, minutes=0).total_seconds())
	day = fill_daytime(text)
	time_work = def_timework(day)
	time_remain, overflow = def_timeremain(time_target, time_work)
	return (day, time_target, time_work, time_remain, overflow)

def	printing(text, day, time_target, time_work, time_remain, overflow):
	print
	write_daytime(text, day)
	print
	write_stats(time_target, time_work, time_remain, overflow)

def	main():
	if not 0 < len(argv) < 4:
		print("Number of arguments must be in the range: 0 - 2")
		exit()

	if len(argv) == 1:
		text = read_data()
		day, time_target, time_work, time_remain, overflow = definding(text)
		printing(text, day, time_target, time_work, time_remain, overflow)
		exit()

	if len(argv) == 2:
		if (argv[1] == "clear"):
			clear_data()
			text = read_data()
			day, time_target, time_work, time_remain, overflow = definding(text)
			printing(text, day, time_target, time_work, time_remain, overflow)
			exit()
		if (argv[1] == "list"):
			text = read_data()
			day, time_target, time_work, time_remain, overflow = definding(text)
			write_daytime(text, day)
			exit()
		if (argv[1] == "stat"):
			text = read_data()
			day, time_target, time_work, time_remain, overflow = definding(text)
			write_stats(time_target, time_work, time_remain, overflow)
			exit()
		print("Unknown command")
		exit()

	if len(argv) == 3:
		text = read_data()
		change_data(text)
		day, time_target, time_work, time_remain, overflow = definding(text)
		printing(text, day, time_target, time_work, time_remain, overflow)
		exit()

	print("Something wrong :(")


if __name__ == '__main__':
	main()
