from collections import defaultdict as dd

class Node:
    def __init__(self, userID = None, tweetID = None):
        self.userID = userID
        self.tweetID = tweetID
        self.next = None
        self.prev = None

class Twitter:

    def __init__(self):
        self.dicfriends = dd(set)

        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        node = Node(userId, tweetId)
        
        temp = self.end.prev
        temp.next = self.end.prev = node
        node.next, node.prev = self.end, temp

    def getNewsFeed(self, userId: int) -> List[int]:
        pointer = self.end

        answer = []

        while len(answer) < 10 and pointer is not self.start:

            if userId == pointer.userID or pointer.userID in self.dicfriends[userId]:
                answer.append(pointer.tweetID)

            pointer = pointer.prev
        
        return answer
        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.dicfriends[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.dicfriends[followerId]:
            self.dicfriends[followerId].remove(followeeId)
        
