from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/convertUpperCase', methods=['GET', 'POST'])
def convertUpperCase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        if input_string:
            result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/convertLowerCase', methods=['GET', 'POST'])
def convertLowerCase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        if input_string:
            result = input_string.lower()
    return render_template('tolowercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    result = None
    if request.method == 'POST':
        try:
            input_integer = request.form.get('inputInteger', '')
            if input_integer:
                radius = float(input_integer)
                result = round(3.14159 * radius ** 2, 2)
        except ValueError:
            result = "Please enter a valid number"
    return render_template('areacircle.html', result=result)

@app.route('/areaOftriangle', methods=['GET', 'POST'])
def areaOftriangle():
    result = None
    if request.method == 'POST':
        try:
            input_base = request.form.get('inputBase', '')
            input_height = request.form.get('inputHeight', '')
            if input_base and input_height:
                base = float(input_base)
                height = float(input_height)
                result = round(0.5 * base * height, 2)
        except ValueError:
            result = "Please enter valid numbers"
    return render_template('areatriangle.html', result=result)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')
        
        # Here you would typically handle the form submission
        # For now, we'll just flash a success message
        if name and email and message:
            flash('Thank you for your message! I\'ll get back to you soon.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
