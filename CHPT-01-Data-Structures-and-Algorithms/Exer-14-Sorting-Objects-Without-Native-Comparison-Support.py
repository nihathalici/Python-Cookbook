# Exer-14-Sorting-Objects-Without-Native-Comparison-Support.py

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

print(users)

print(sorted(users, key=attrgetter('user_id')))

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

print(min(users, key=attrgetter('user_id')))

print(max(users, key=attrgetter('user_id')))
