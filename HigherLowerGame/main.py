import art
import gameData
import random
from replit import clear

def account_details(account):
	return (f"{account['name']}, a {account['description']}, from {account['country']} ")

def compare_followers(user_choice,followerA,followerB):
	if followerA > followerB:
		if user_choice == 'a':
			return True
		else:
			return False
	else:
		if user_choice == 'b':
			return True
		else:
			return False

print(art.logo)
score = 0
compareB = random.choice(gameData.data)
should_continue = True
while should_continue:
	compareA = compareB
	compareB = random.choice(gameData.data)
	while compareA == compareB:
		compareB = random.choice(gameData.data)

	print(f"Compare A: {account_details(compareA)}")
	print(art.vs)
	print(f"Compare B: {account_details(compareB)}")

	user_choice = input("Who has more followers? 'A' or 'B': ").lower()

	followerA = compareA['follower_count']
	followerB = compareB['follower_count']

	clear()
	print(art.logo)

	is_correct = compare_followers(user_choice,followerA,followerB)
	if is_correct:
		score += 1
		print(f"You are Right! Your Current score is {score}")
	else: 
		print(f"You are wrong! Your Final score is {score}")
		should_continue = False






