 N = 6
Baddies = [1, 2, 3, 5, 6, 7]

All_Squad= set(range(1, N + 1))
Input_Squad = set(Baddies)
Missing_Squad = list(All_Squad - Input_Squad)

Missing_Squad.sort()
print("That lost one in the paradise 😅:")
print((Missing_Squad))
