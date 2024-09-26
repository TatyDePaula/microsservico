from backend import app, database
from backend.models import Usuario, Post

if __name__ == '__main__':
    with app.app_context():
        database.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000)  # Altere a porta para 8000


