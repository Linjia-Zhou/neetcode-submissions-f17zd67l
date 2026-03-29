from collections import deque, defaultdict
class Twitter:

    def __init__(self):
        self.tweetOrder = deque()
        self.following = defaultdict(set) # using set to make sure no duplicates

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetOrder.appendleft([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        count = 1

        for i in range(len(self.tweetOrder)):
            tweet_user_id, tweet_id = self.tweetOrder[i]

            if userId in self.following: # userId follows someone
                if tweet_user_id in self.following[userId] or tweet_user_id == userId:
                    ans.append(tweet_id)
            else:
                if tweet_user_id == userId:
                    ans.append(tweet_id)

            if len(ans) == 10:
                return ans
        
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)