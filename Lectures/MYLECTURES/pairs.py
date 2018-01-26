'''
This script will generate an "optimal" pair programming schedule for as many
days as you need (probably you'll need an 8 weeks schedule).

We define an "optimal" pairing schedule as one that forces every student
to work with every other student over the first n-1 days, where n is the
number of students you have in your cohort.

The n'th day will have the same pairings as the 1st day. Basically this script
generates an optimal n-1 days-worth of parings and then repeats those n-1 days
over the period you need.

This script handles if you have an odd number of students by adding a 'None'
student, then doing the "optimal" schedule as described above, and then yanking
any student paired with 'None' and adding them to a random existing group.

THIS SCRIPT IS RATHER UGLY. DON'T JUDGE ME!
'''

# PUT THE NAMES OF YOUR STUDENTS HERE!
students = [
        "Forest",
        "Jack",
        "Jamie",
        "Katie",
        "Kevin",
        "Lauren",
        "Michael",
        "Randall",
        "Russell",
        "Trevor"
        ]


##############################################################################
# Script logic all below. You /shouldn't/ need to touch anything below.
##############################################################################

import sys
import random
from itertools import izip
from datetime import datetime, timedelta

random.shuffle(students)

if len(students) % 2:
    students.append(None)

has_paired_with = {student: set() for student in students}


def find_pairings(curr_pairings=None, paired=None):
    '''
    This recursive function pairs students for ONE DAY.
    It returns a list of tuples denoting a good way to
    pair the students for just THIS ONE DAY. Or it returns
    `None` if it is no longer possible to pair students
    uniquely.

    This function uses the global `students` list as
    the source of our students.

    This function both reads and writes to the global
    `has_paired_with` dictionary. It reads from it to
    ensure that no pairing on this day match pairings
    on any previous day. And it writes to the dictionary
    the pairings of this day so that no future day uses
    those pairing.
    '''

    if not curr_pairings:
        curr_pairings = []
    if not paired:
        paired = set()

    # Find a student who is not yet paired on this day. Call this student s1.
    for s in students:
        if s not in paired:
            s1 = s
            break
    else:
        return curr_pairings   # <-- Yay! Everyone is paired, so we have a solution!

    # Now find a student (s2) to pair with s1.
    # s1 and s2 cannot be the same student.
    # s2 cannot be paired with someone else already for this day.
    # s1 and s2 must not have worked together on any previous day.
    for s2 in students:
        if s1 == s2 or s2 in paired or s2 in has_paired_with[s1]:
            continue

        # At this point, its possible to pair s1 and s2, since
        # they haven't paired yet. But, we're not really sure if
        # this is a good idea yet. This pairing MIGHT lead to
        # an unsolvable position. So let's just try it.
        curr_pairings.append((s1, s2))
        paired.add(s1)
        paired.add(s2)
        has_paired_with[s1].add(s2)
        has_paired_with[s2].add(s1)
        final_pairings = find_pairings(curr_pairings, paired)
        if final_pairings:
            return final_pairings  # <-- Yay! This pairing worked and we got a final, good solution!

        # If we're here, that means we couldn't find a solution.
        # So we'll roll back because this pair must not be a good
        # idea since we couldn't find a solution.
        curr_pairings.pop()
        paired.discard(s1)
        paired.discard(s2)
        has_paired_with[s1].discard(s2)
        has_paired_with[s2].discard(s1)

    # We couldn't find a pair for s1, so this day is not solvable.
    return None


def handle_nones(pairs):
    '''
    If anyone is paired with None, then yank them out and add them to
    another group.
    '''
    need_yank = [name for pair in pairs
                          for name in pair
                              if None in pair and name is not None]
    pairs = [pair for pair in pairs if None not in pair]
    random.shuffle(pairs)
    for i, name in enumerate(need_yank):
        pairs[i] += (name,)
    return pairs


# There /should/ be n-1 days of unique pairings... let's find those.
schedule = []
while True:
    pairs = find_pairings()
    if not pairs:
        break
    pairs = handle_nones(pairs)
    schedule.append(pairs)

def pair_day_generator(schedule):
    while True:
        for pairs in schedule:
            yield pairs


# Ask the user how many days they need.
if len(sys.argv) != 3:
    start_date = raw_input("Start date (YY-MM-DD):")
    end_date   = raw_input("End date   (YY-MM-DD):")
else:
    start_date = sys.argv[1]
    end_date   = sys.argv[2]

start_date = datetime.strptime(start_date, '%y-%m-%d')
end_date   = datetime.strptime(end_date,   '%y-%m-%d')


# Ref: http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + timedelta(n)

def daterange_weekdays(start_date, end_date):
    for date in daterange(start_date, end_date):
        if date.weekday() < 5:
            yield date

sys.stdout = open('pairs.txt', 'w')

for date, pairs in izip(daterange_weekdays(start_date, end_date),
                        pair_day_generator(schedule)):
    print date.strftime('%y-%m-%d')
    for pair in pairs:
        print pair
    print

