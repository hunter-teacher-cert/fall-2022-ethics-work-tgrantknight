Group: Taylor Grant-Knight & Wei Lee

We edited seat_economy() so that it calls on our 2 new methods (stated below)
- Starting from the beginning of the plane, we start out with the max family size and search through each row using find_family_seat() and seat them if there are avaiable rooms
- We call seat_individually() to fill up either families who could not be seated together or families of 1.

We created find_family_seats()
- Given an available seat, checks the adjacent seats to the right for the given family size
- If the entire family can be seated in adjacent seats, returns true. Otherwise, returns false

We created seat_individually()
- This is called when it is impossible to fit the entire family size together
- This will seat each family member individually, like the old version of seat_economy
- If we had time, we could have checked smaller chunks of the family before seating individually
--- Ex: If family size was 3, check for a chunk of 2 and an individual seat of 1

We also edited the ending body of fill_plane()
- For the ending portion of fill_plane, we modified it so that we called the newly modified seat_economy method that seats the max family size first and then worked backwards to family size of 1.