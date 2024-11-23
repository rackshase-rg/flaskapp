from flask import Flask, render_template
import requests

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    # Заменяем Buzzfeed на другой источник
    cat_gif_url = "https://cataas.com/cat/gif"
    return render_template('index.html', gif_url=cat_gif_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
