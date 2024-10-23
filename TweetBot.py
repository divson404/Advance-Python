from datetime import datetime, timedelta

class TwitterPost:
    def __init__(self, tweet: str, time: datetime, likes: int, comments: int, reposts: int):
        self.tweet = tweet
        self.time = time 
        self.likes = likes
        self.comments = comments
        self.reposts = reposts

    def recent_tweet(self):
        current_time = datetime.now()
        time_difference = current_time - self.time

        if time_difference < timedelta(minutes=10):
            print(f"Your tweet is recent! Posted just {time_difference.seconds // 60} minutes ago.")
        elif time_difference < timedelta(hours=1):
            print(f"This tweet is still fairly recent, posted {time_difference.seconds // 60} minutes ago.")
        elif time_difference < timedelta(days=1):
            print(f"Looks like this tweet was posted earlier today, about {time_difference.seconds // 3600} hours ago.")
        else:
            days_passed = time_difference.days
            print(f"This tweet was posted {days_passed} day{'s' if days_passed > 1 else ''} ago. It's getting old now.")

    def tweet_summary(self):
        print(f"Summary of your tweet:\n"
              f" - Tweet: \"{self.tweet}\"\n"
              f" - Posted on: {self.time.strftime('%Y-%m-%d %H:%M:%S')}\n"
              f" - Likes: {self.likes}\n"
              f" - Comments: {self.comments}\n"
              f" - Reposts: {self.reposts}")

tweet_time = datetime.now() - timedelta(minutes=5)
tweet = TwitterPost("I just posted something awesome!", tweet_time, likes=120, comments=45, reposts=25)

tweet.recent_tweet()
tweet.tweet_summary()


