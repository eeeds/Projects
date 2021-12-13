from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

books = {
    '1': {
        'isbn': '744586',
        'title': 'Cien años de soledad',
        'description': 'Lorem insup lol.',
        'autor': 'Gabriel Garcia Marquez'
    },
    '2': {
        'isbn': '7894546',
        'title': 'De animales a dioses',
        'description': 'Lorem insup lol.',
        'autor': 'Yuval Noah Harari'
    }
}

def abort_if_book_doesnt_exist(book_id):
    if book_id not in books:
        abort(404, message='El libro con ID {} no existe'.format(book_id))


class BookList(Resource):
    def get(self):
        return jsonify(books)


class Book(Resource):
    def get(self, book_id):
        abort_if_book_doesnt_exist(book_id)
        return make_response( jsonify(books[book_id]), 200 )


class Authors(Resource):
    pass


class Genres(Resource):
    pass


api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<book_id>')
api.add_resource(Authors, '/authors')
api.add_resource(Genres, '/genres')


if __name__ == '__main__':
    app.run(debug=True)