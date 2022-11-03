The issue with the original algorithm is:
- Only economy plus reserves seats upon purchase
- Regular economy only has randomly assigned seats upon purchase
- Only up to 3 tickets can be purchased in bulk
- Even if purchased in bulk, the seats for these tickets are randomly assigned

Solutions:
- Increase the family size to 5 (this may be too large for the algorithm to function, but we'll try it and see)
  - This is changing the value in line 258
- Change the code of the regular economy assignment to look for blocks of available seats
  - Family blocks should be looked for first
  - Rows are easier to parse than columns, so start with that
  - If there are no blocks available, use a recursive algorithm and split the family block size in half. That way a group of 4 may have two groups of 2 (better than nothing)
  - This would probably mean refactoring the seat_economy method into seat_economy_family and seat_economy