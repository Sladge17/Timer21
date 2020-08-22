#!/usr/bin/python

from sys import argv
from datetime import timedelta

def	read_data():
	text = [""] * 7
	with open("timedata", 'r') as file:
		for i in range(7):
			text[i] = file.next()[:-1]
	return text

def	change_data(argv, text):
	try:
		index = int(argv[1])
	except:
		print("First argument must be int")
		exit()
	if index < 1 or index > 7:
		print("First argument must be in the range 1 - 7")
		exit()
	text[index - 1] = argv[2]
	with open("timedata", 'w') as file:
		for i in range(7):
			file.write(text[i])
			file.write("\n")

def	clear_data():
	with open("timedata", 'w') as file:
		file.write("0.00\n0.00\n0.00\n0.00\n0.00\n0.00\n0.00\n")

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

def	write_daytime(day):
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
	# time_target = int(timedelta(hours=50, minutes=0).total_seconds())
	time_target = int(timedelta(hours=40, minutes=0).total_seconds())
	day = fill_daytime(text)
	time_work = def_timework(day)
	time_remain, overflow = def_timeremain(time_target, time_work)
	return (day, time_target, time_work, time_remain, overflow)

def	printing(day, time_target, time_work, time_remain, overflow):
	print
	write_daytime(day)
	print
	write_stats(time_target, time_work, time_remain, overflow)


if len(argv) == 1:
	text = read_data()
	day, time_target, time_work, time_remain, overflow = definding(text)
	printing(day, time_target, time_work, time_remain, overflow)
	exit()

if len(argv) == 2 and argv[1] == "clear":
	clear_data()
	text = read_data()
	day, time_target, time_work, time_remain, overflow = definding(text)
	printing(day, time_target, time_work, time_remain, overflow)
	exit()

if len(argv) == 3:
	text = read_data()
	change_data(argv, text)
	day, time_target, time_work, time_remain, overflow = definding(text)
	printing(day, time_target, time_work, time_remain, overflow)
	exit()

print("Something wrong :(")
