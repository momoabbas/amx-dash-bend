# function to find the longest
# length in the list
# 1=one,

import num2word

n=input(print("enter number"))
for i in n:
	num2word.to_card(n)


def longestLength(n):
	max1 = len(a[0])
	temp = n[0]

	# for loop to traverse the list
	for i in n:
		if(len(i) > max1):

			max1 = len(i)
			temp = i

	print("The word with the longest length is:", temp,
		" and length is ", max1)


# Driver Program
# a = ["one", "two", "third", "four"]
longestLength(a)
