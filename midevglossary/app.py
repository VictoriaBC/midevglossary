import os
if os.path.exists("env.py"):
  import env 
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Connection to Database
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = 'mongodb+srv://vpb:ztKQZus3.k9hkMY@myfirstcluster-zzbzp.mongodb.net/task_manager?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_words')
def get_words():
    return render_template("words.html",
                           words=mongo.db.words.find())

@app.route('/add_word')
def add_word():
    return render_template('addword.html',
                           categories=mongo.db.categories.find())

@app.route('/insert_word', methods=['POST'])
def insert_word():
    words =  mongo.db.words
    words.insert_one(request.form.to_dict())
    return redirect(url_for('get_words'))


@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    the_word =  mongo.db.words.find_one({"_id": ObjectId(word_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editword.html', word=the_word,
                           categories=all_categories)

@app.route('/update_word/<word_id>', methods=["POST"])
def update_word(word_id):
    words = mongo.db.words
    words.update( {'_id': ObjectId(word_id)},
    {
        'word_name':request.form.get('word_name'),
        'category_name':request.form.get('category_name'),
        'word_description': request.form.get('word_description'),
    })
    return redirect(url_for('get_words'))


@app.route('/delete_word/<word_id>')
def delete_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return redirect(url_for('get_words'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')

# GET METHOD for Search Bar
@app.route('/get_search')
def get_search():
    """
    Route to accept a GET request to perform
    a search
    """
    query = request.args.get('search')
    results = mongo.db.words.find({"word_name": {"$regex": query, "$options": 'i'}})
    print(query)
    print(results)
    return render_template('search.html', query=list(results))
    

# Function for Individual Letter search
@app.route('/get_letters/<letter>')
def get_letters(letter):
    print(letter)
    results = mongo.db.words.find(
        {"word_name": {"$regex": letter, "$options": 'i'}})
    
    return render_template('searchletter.html', letter=results)
    print(word_name)

if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
