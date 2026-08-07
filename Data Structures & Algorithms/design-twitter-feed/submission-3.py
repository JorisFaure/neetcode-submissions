class Twitter:

    def __init__(self):
        self.usersAndFollowee = defaultdict(set)
        self.usersAndTweets = defaultdict(set)
        self.usersTweetList = defaultdict(set)
        self.count = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        print(self.usersTweetList)
        self.usersTweetList[userId].add((self.count, tweetId))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweetFeed = []
        for follows in self.usersAndFollowee[userId] :
            for tweets in self.usersTweetList[follows] :
                allTweetFeed.append(tweets)
        for tweets in self.usersTweetList[userId] :
                allTweetFeed.append(tweets)
        print(allTweetFeed)
        
        heapq.heapify(allTweetFeed)
        last10tweets = heapq.nlargest(10,allTweetFeed)
        res = [id_ for c, id_ in last10tweets]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.usersAndFollowee[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId in self.usersAndFollowee[followerId] :
                self.usersAndFollowee[followerId].remove(followeeId)
        
