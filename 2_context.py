# Create a function that takes a list or numbers and returns only the even values.
# write a simple Flask app that returns a list or even numbers from a List or numbers
# create a sample List or numbers
# create a list of even numbers from the sample list
# return the list of even

def filter_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_even_numbers(numbers)
    return even_numbers

if __name__ == '__main__':
    app.run()