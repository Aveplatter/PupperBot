import os
import praw
import time
import simplejson

def main():

	#logging enabler
	import logging
	handler = logging.StreamHandler()
	handler.setLevel(logging.DEBUG)
	logger = logging.getLogger('prawcore')
	logger.setLevel(logging.DEBUG)
	logger.addHandler(handler)

	#submission tracker
	if not os.path.isfile("posts_replied_to.txt"):
		posts_replied_to = []
	else:
		 with open("posts_replied_to.txt", "r") as f:
			 posts_replied_to = f.read()
			 posts_replied_to = posts_replied_to.split("\n")
			 posts_replied_to = list(filter(None, posts_replied_to))

	bot = praw.Reddit('bot1', user_agent='PupperBot_0')
	subreddit = bot.subreddit('PupperBot')

	submissions = subreddit.stream.submissions()
	posted_comments = 0

	for submission in submissions:
		if submission.id not in posts_replied_to:
			if 'imgur' in submission.url:
				message = "this post is from imgur!"
				postSuccess = False
				while postSuccess == False:
					try:
						submission.reply(message)
						postSuccess = True
					except:
						time.sleep(10)
			elif 'i.redd.it' in submission.url:
				message = "this post is from i.redd.it!"
				postSuccess = False
				while postSuccess == False:
					try:
						submission.reply(message)
						postSuccess = True
					except:
						time.sleep(10)
			print("Bot replying to : ", submission.title)
			posts_replied_to.append(submission.id)
		else:
			print('already commented')
		with open("posts_replied_to.txt", "w") as f:
			for post_id in posts_replied_to:
				f.write(post_id + "\n")

main()










main()
