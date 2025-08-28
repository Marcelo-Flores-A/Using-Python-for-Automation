years = [1925, 1943, 1968, 1937, 1975, 1912, 1989, 1954, 1920, 1996]
# years.reverse() # Triggers the assert error (error handling) 
years.sort()
print(years)
assert years[0] <= years[-1], "First element is greater than last element."