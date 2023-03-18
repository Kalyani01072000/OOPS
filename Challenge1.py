class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2
# Create a Point object with x=1, y=3, z=5
p = Point(1, 3, 5)

# Call the sqSum() method of the object
sum_of_squares = p.sqSum()

# Print the result
print(sum_of_squares)  # Output: 35
