import random

number = random.randint(1,100)
print(number)
while True:
	guess_number = input("猜猜數字是多少?")
	guess_number = int(guess_number)
	print(guess_number)
	if guess_number == number:
		print("你猜對了!!")
		break
	else:
		if number > guess_number:
			print("比答案小")
		else:
			print("比答案大")