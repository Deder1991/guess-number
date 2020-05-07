import random
counter = 0
number = random.randint(1,100)
print(number)
while True:
	counter = counter + 1
	print("這是第", counter, "次猜數字")
	guess_number = input("猜猜數字是多少? ,")
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
