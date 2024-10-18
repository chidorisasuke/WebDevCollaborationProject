# run.py
from app import app

app.secret_key='123456789'

if __name__ == '__main__':
    # Pastikan debug=True saat mode development
    app.run(debug=True)
