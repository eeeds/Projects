#Import Flask to initialize the server
from flask import Flask, jsonify, request


#Create an instance of the Flask class
app = Flask(__name__)

#Create a list of dictionaries that contain the data
books = [
    {
        'title':'The Design of EveryDay Things',
        'author':'Don Norman',
        'genre':'Non-Fiction',
    },
    {
        'title':'The Most Human Human',
        'author':'Brian Christian',
        'genre':'Non-Fiction',
    }
]

#Create a route to handle the root of the website
@app.route('/books', methods = ['GET'])
def get_books():
    #Return a list in JSON format
    return jsonify({'books':books})


#Main method
if __name__ == '__main__':
    #debug is a parameter that tells the server to reload itself if it detects a change in the code
    #With port 8000, the server will be available at http://localhost:8000
    app.run(debug=True, port = 8000)