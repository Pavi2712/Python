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
