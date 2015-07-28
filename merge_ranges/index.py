'''
https://www.interviewcake.com/question/merging-ranges
'''

def condense_meeting_times(meetings):
    # first, sort all our meetings
    sorted_meetings = sorted(meetings)

    new_meetings = [meetings[0]]

    for meeting_start, meeting_end in sorted_meetings:
        last_meeting_start, last_meeting_end = new_meetings[-1]

        if (meeting_start <= last_meeting_end):
            new_meetings[-1] = (last_meeting_start, max(meeting_end, last_meeting_end))
        else:
            new_meetings.append((meeting_start, meeting_end))

    return new_meetings

print condense_meeting_times([(0, 1), (4, 8), (10, 12), (9, 10), (3, 5)])

print condense_meeting_times([(1, 10), (2, 6), (3, 5), (7, 9)])
