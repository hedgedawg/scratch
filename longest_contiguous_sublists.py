"""

We have some clickstream data that we gathered on our client's website. 
Using cookies, we collected snippets of users' anonymized URL histories 
while they browsed the site. The histories are in chronological order 
and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and 
returns the longest contiguous sequence of URLs that appears in both.

Sample output:

findContiguousHistory(user0, user1)
  /pink.php
  /register.asp
  /orange.html

findContiguousHistory(user1, user2)
  /green.html
  /blue.html
  /pink.php
  /register.asp

findContiguousHistory(user0, user3)
  (empty)

findContiguousHistory(user2, user3)
  /blue.html

findContiguousHistory(user3, user3)
  /blue.html
  /logout.php
"""

from itertools import combinations

user0 = [ "/start.html", "/pink.php", "/register.asp", "/orange.html", "/red.html" ];
user1 = [ "/start.html", "/green.html", "/blue.html", "/pink.php", "/register.asp", "/orange.html" ]
user2 = [ "/red.html", "/green.html", "/blue.html", "/pink.php", "/register.asp" ]
user3 = [ "/blue.html", "/logout.php" ]

def all_slices(s):
    for start, end in combinations(range(len(s)+1), 2):
        yield s[start:end]
        

def findContiguousHistory(userA, userB):
    if len(userA) < len(userB):
        shortest, longest = userA, userB
    else: 
        shortest, longest = userB, userA
        
    a_slices = sorted(all_slices(shortest), key=len, reverse=True)
    b_slices = sorted(all_slices(longest), key=len, reverse=True)
    
    for item in a_slices: 
        if item in b_slices: 
            print("\n".join(item))
            return item
    print('empty')
    return []

print('findContiguousHistory(user0, user1)')
findContiguousHistory(user0, user1)
#   /pink.php
#   /register.asp
#   /orange.html

print('findContiguousHistory(user1, user2)')
findContiguousHistory(user1, user2)
#   /green.html
#   /blue.html
#   /pink.php
#   /register.asp

print('findContiguousHistory(user0, user3)')
findContiguousHistory(user0, user3)
#   (empty)

print('findContiguousHistory(user2, user3)')
findContiguousHistory(user2, user3)
#   /blue.html

print('findContiguousHistory(user3, user3)')
findContiguousHistory(user3, user3)
#   /blue.html
#   /logout.php
