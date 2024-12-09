
# Flask Cat GIF App For Vitalinka

This is a simple Flask web application that displays a random cat GIF. The application is written in Python 3.10 and uses the [Cataas](https://cataas.com/) service as a source for cat animations.

## Features

- Displays a random cat GIF on the main page.
- Uses Flask as the web framework.
- Modernized for Python 3.10 and Flask 2.x.

---

## Requirements

Before running the application, make sure you have the following installed:

- Python 3.10 or higher
- `pip` for dependency management

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rackshase-rg/flaskapp.git
   cd flaskapp
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## File Structure

```
flaskapp/
├── app.py               # Main application script
├── requirements.txt     # Dependencies for the project
├── templates/
│   └── index.html       # HTML template for the app
└── README.md            # Project documentation
```

---

## Example Screenshot

Here's an example of what the app looks like in the browser:

![Cat GIF App Example](https://cataas.com/cat/gif)

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project.
