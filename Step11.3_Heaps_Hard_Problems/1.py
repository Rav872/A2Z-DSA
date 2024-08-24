from collections import defaultdict, deque
import heapq

class Twitter:
    def __init__(self):
        self.tweets = defaultdict(deque)  # Store user tweets
        self.followers = defaultdict(set)  # Store user followees
        self.timestamp = 0  # Global timestamp to order tweets
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet with a timestamp
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1
    
    def getNewsFeed(self, userId: int) -> list:
        # Max heap to get the top 10 tweets by timestamp
        max_heap = []
        # Include the user's own tweets
        users_to_check = self.followers[userId] | {userId}
        
        for user in users_to_check:
            for tweet in self.tweets[user]:
                heapq.heappush(max_heap, tweet)
                # Only keep the 10 most recent tweets in the heap
                if len(max_heap) > 10:
                    heapq.heappop(max_heap)
        
        # Sort tweets by timestamp in descending order
        result = [tweetId for timestamp, tweetId in sorted(max_heap, reverse=True)]
        return result
    
    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followeeId to followerId's follow list
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followeeId from followerId's follow list
        self.followers[followerId].discard(followeeId)

def main() -> None:
    # Example usage:
    twitter = Twitter()
    twitter.postTweet(1, 5) # User 1 posts tweet with id 5
    print(twitter.getNewsFeed(1)) # User 1 should see [5]
    twitter.follow(1, 2) # User 1 follows user 2
    twitter.postTweet(2, 6) # User 2 posts tweet with id 6
    print(twitter.getNewsFeed(1)) # User 1 should see [6, 5]
    twitter.unfollow(1, 2) # User 1 unfollows user 2
    print(twitter.getNewsFeed(1)) # User 1 should see [5]
    pass

if __name__=='__main__':
    main()