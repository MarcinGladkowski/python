cities = ["Vancouver", "Oslo", "Berlin", "Krakow", "Graz", "Belgrade"]

"""
Write a Python code snippet that uses the walrus operator (:=) within an all() function to check whether all
city names contain "o". Print the first city name that doesn’t contain "o". If all city names contain an "o", 
then print "All city names contain 'o'". You shouldn’t define cities yourself.
"""

# using generator expression comprehension
if all("o" in (counterexample := city) for city in cities):
    print("All city names contain 'o'")
else:
    print(counterexample)