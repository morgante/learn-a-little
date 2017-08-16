'''
https://www.interviewcake.com/question/python/inflight-entertainment
'''

def find_combo_flight(flight_length, movie_lengths):
    seen_lengths = set()

    for length in movie_lengths:
        looking_for = flight_length - length

        if looking_for in seen_lengths:
            return (length, looking_for)

        seen_lengths.add(length)

    return None

movies = [3, 9, 11, 9]

print('false', 30, find_combo_flight(30, movies))
print('false', 11, find_combo_flight(11, movies))
print('true', 18, find_combo_flight(18, movies))
print('false', 6, find_combo_flight(6, movies))
print('true', 12, find_combo_flight(12, movies))
