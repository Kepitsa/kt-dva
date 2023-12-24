import csv
import json

def load_data(books_file, users_file):
    books = []
    users = []

    with open(books_file, newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            books.append(row)

    with open(users_file) as jsonfile:
        users = json.load(jsonfile)

    return users, books

def distribute_books(users, books):
    result = []
    
    count_users = len(users)
    count_books = len(books)

    books_per_user = count_books // count_users
    remainder = count_books % count_users

    for i in range(count_users):
        user = users[i]
        user_books = books[i * books_per_user:(i + 1) * books_per_user]

        if i < remainder:
            extra_book = books[count_users * books_per_user + i]
            user_books.append(extra_book)

        user_data = {
            "name": user['name'],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": user_books
        }

        result.append(user_data)

    return result

def save_to_json(data, output_file):
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

if __name__ == "__main__":
    books_file = "books.csv"
    users_file = "users.json"
    output_file = "result.json"

    users, books = load_data(books_file, users_file)
    result_data = distribute_books(users, books)
    save_to_json(result_data, output_file)
