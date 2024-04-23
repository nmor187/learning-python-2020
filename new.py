#import lyrics into list
f = open("lyrics.txt", "r")
lyrics = f.read()
lyrics_list = lyrics.split()
total_div = len(lyrics_list)
total_list = []
for i in lyrics_list:
	x = len(i)
	total_list.append(x)
total_sum = sum(total_list)
pr = float(total_sum) / float(total_div)
print(pr)
	
