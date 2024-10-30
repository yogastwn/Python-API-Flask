from config import app, db
from routes.Book_bp import book_bp
from routes.Category_bp import category_bp

app.register_blueprint(book_bp)
app.register_blueprint(category_bp)


if __name__ == "__main__":
  db.create_all()
  app.run(debug=True)