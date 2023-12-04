from flask import Flask, jsonify, render_template, request
import joblib
import os

app = Flask(__name__)

# recipe data 
recipe_data = {
    0: 'Desserts',
    1: 'Vegetable Biriyani',
    2: 'Veg Pulav',
    3: 'Health foods main course recommented ',
}

# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(script_dir, 'sample_model.joblib')

# linear regression model 
# In a real-world scenario, you would train a model on a larger dataset.
model = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('ai.html')

@app.route('/get_recommendation')
def get_recommendation():
    age = int(request.args.get('age'))

    # In a real-world scenario, you might want to use a more sophisticated model
    # and a larger dataset for better recommendations.
    # Here, we are using a simple linear model for demonstration purposes.
    predicted_recipe = int(model.predict([[age]])[0])

    # Handle potential KeyError and return a default value
    recipe_name = recipe_data.get(predicted_recipe, 'Unknown Recipe')

    return jsonify({'recipe': recipe_name})

if __name__ == '__main__':
    app.run(debug=True)