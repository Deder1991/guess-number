import random
counter = 0
number_min = input("請輸入數字最小值:")
number_max = input("請輸入數字最大值:")
number_min = int(number_min)
number_max = int(number_max)
number = random.randint(number_min,number_max)
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
