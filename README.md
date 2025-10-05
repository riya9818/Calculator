#  Django Scientific Calculator

A sleek and functional **scientific calculator web app** built using **Django**, featuring both basic and advanced mathematical operations — designed for learning, experimentation, and quick computations.

---

##  Features

 **Basic Operations**
- Addition (+)
- Subtraction (−)
- Multiplication (×)
- Division (÷)

 **Scientific Functions**
- Trigonometric: `sin`, `cos`, `tan`
- Power: `xʸ`
- Logarithm: `log`
- Square root: `√`
- Factorial: `!`
- Percentage: `%`
- Absolute value: `abs()`

 **Extras**
- Responsive and modern UI
- Toggleable history sidebar (doesn’t interfere with main calculator)
- Session-based history tracking
- Built using Django backend + pure HTML, CSS, and JavaScript frontend

---

##  Tech Stack

| Component | Technology |
|------------|-------------|
| Framework | Django |
| Language | Python |
| Frontend | HTML, CSS, JavaScript |
| Math Engine | Python `math` module |
| Storage | Django Sessions |

---

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/django-scientific-calculator.git
   cd django-scientific-calculator

2. **Create and activate a virtual environment:**


python -m venv .venv
.venv\Scripts\activate      # for Windows
source .venv/bin/activate   # for Mac/Linux

3. **Install dependencies:**


pip install django

4. **Run the development server:**


python manage.py runserver

5. **Open in your browser:**

http://127.0.0.1:8000/