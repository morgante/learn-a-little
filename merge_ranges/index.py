'''
https://www.interviewcake.com/question/merging-ranges
'''

def condense_meeting_times(meetings):
    return [(0, 1), (3, 8), (9, 12)]

print condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
