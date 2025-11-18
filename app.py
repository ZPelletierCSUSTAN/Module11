from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime #For dynamic date
from greeting import get_greeting #Import from your module
app = Flask(__name__)

@app.route('/greeting/<name>') # URL: http://127.0.0.1:5000/greeting/YourName
def greeting(name): 
   message = get_greeting(name) 
   current_date = datetime.now().strftime("%Y-%m-%d") 
   return render_template('greeting.html', message=message, current_date=current_date)
# Set a secret key for session management (REQUIRED for using sessions)
app.secret_key = 'a_very_secret_key_for_calc_app' 

# Initialize calculation history list in the session if it doesn't exist
@app.before_request
def initialize_session():
    if 'history' not in session:
        session['history'] = []

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None

    if request.method == 'POST':
        if 'clear' in request.form:
            # Clear the history
            session['history'] = []
            session.modified = True
            return redirect(url_for('calculator'))
        
        try:
            # Get input values from the form
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operator = request.form.get('operator')
            
            # Perform calculation based on the selected operator
            if operator == 'add':
                result = num1 + num2
            elif operator == 'subtract':
                result = num1 - num2
            elif operator == 'multiply':
                result = num1 * num2
            elif operator == 'divide':
                if num2 == 0:
                    error = "Error: Division by zero is not allowed."
                else:
                    result = num1 / num2
            else:
                error = "Invalid operator selected."
                
            # If a result was calculated successfully, store it
            if result is not None:
                # Determine the symbol for display in history
                symbol_map = {'add': '+', 'subtract': '-', 'multiply': '×', 'divide': '÷'}
                symbol = symbol_map.get(operator, '?')
                
                # Format the numbers and result to a reasonable precision
                # You can adjust the formatting as needed
                formatted_result = f"{result:.2f}".rstrip('0').rstrip('.')
                
                # Store the calculation in the session history
                calculation_entry = {
                    'num1': num1,
                    'num2': num2,
                    'operator_symbol': symbol,
                    'result': formatted_result
                }
                session['history'].append(calculation_entry)
                session.modified = True # Tell Flask the session has been updated
                
        except ValueError:
            error = "Invalid input: Please enter valid numeric values."
        except Exception as e:
            error = f"An unexpected error occurred: {e}"

    # Render the template, passing the current result, error, and history
    return render_template('index.html', 
                           result=result, 
                           error=error, 
                           history=session.get('history', []))

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)