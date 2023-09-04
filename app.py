from flask import Flask, request, abort, render_template

app = Flask(__name__)

# Sample data for three blog articles (unchanged from the previous example)
blog_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of the first blog post.'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of the second blog post.'
    },
    {
        'title': 'Post 3',
        'content': 'This is the content of the third blog post.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

# New /admin endpoint that checks the X-Forwarded-For header
@app.route('/admin')
def admin():
    # Check if the X-Forwarded-For header is present and has the correct value
    forwarded_for = request.headers.get('X-Forwarded-For')
    if forwarded_for == '192.168.0.1':
        return "Welcome to the admin page!"
    else:
        abort(403)  # Return a Forbidden HTTP status code if the header is not as expected

if __name__ == '__main__':
    app.run(debug=True)
