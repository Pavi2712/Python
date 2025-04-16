year = 2016
event = 'Referendum'
print(f"Result of the year {year} {event}")

yes_votes = 42_572_654
print("yes_votes",yes_votes)
total_votes = 85_705_149
print("total_votes",total_votes)
percentage = yes_votes / total_votes
print("percentage",percentage)
print('Hi{:16}YESvotes{:2.4%}'.format(yes_votes, percentage))

str1 = "Hello"
print("String", str(str1))
print("Representation", repr(str1)) #It will give a string with single quotes

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name , num in table.items():
    print(f'{name:7}==>{num:10d}')

# Representation of = in formatting strings
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

#formatting program'

for x in range(1,11):
    print('{0:2d}{1:3d}{2:4d}'.format(x , x*x , x*x*x))

# The above program manually:

for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
