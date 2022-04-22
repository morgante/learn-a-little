"""
Given a red/blue strip, and a blue strip, find maximum coverage of red squares using the blue strip. You are given a list of intervals where the red/blue strip is red, e.g. {0,2},{4,5} would look like [r][r][r][b][b][r][r], and the length of the blue strip.
Write a solution to solve for the maximum coverage in O(n) time.
"""

def get_covered(red_intervals, blue_length):
  j = -1
  red_window = 0
  covered_red = 0
  max_found = 0
  for current_interval in red_intervals:
    start = current_interval[0]
    if get_length(current_interval) >= blue_length:
      return blue_length

    while True:
      j += 1
      if j >= len(red_intervals):
        break
      other_interval = red_intervals[j]
      if other_interval[1] - start >= blue_length:
        if (other_interval[0] - start) < blue_length:
          covered_red += blue_length - (other_interval[0] - start)
        break
      red_window += get_length(red_intervals[j])
      covered_red = red_window

    max_found = max(max_found, covered_red)

    red_window -= get_length(current_interval)

  return max_found

def get_length(red_interval):
  return red_interval[1] - red_interval[0]
