from flask import Flask, render_template

app = Flask(__name__)

# all posts array
all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of the post',
        'author' : 'Jane'
    },
    {
        'title': 'Post 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda dolor doloremque velit voluptatibus. Ad, aut consequatur cumque, doloremque eius fugiat fugit iste iusto magnam minima nobis nulla officia perferendis repudiandae.'
    }
]


@app.route('/')
def index():
    return render_template('index.html')

# Displays all posts
@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


@app.route('/home/<string:name>', methods=['GET'])
def home(name):
    return "hello " + name


if __name__ == "__main__":
    app.run(debug=True)
