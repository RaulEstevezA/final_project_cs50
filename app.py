from flask import Flask, render_template, request, redirect, url_for
import random
from dicto import options_dict_adult, obliged_adult, options_dict_young, obliged_young, options_dict_child, obliged_child

app = Flask(__name__)

# define index route
@app.route('/')
def index():
    return render_template('index.html')


# define adult route
@app.route('/adult', methods=['GET', 'POST'])
def adult():
    if request.method == 'POST':

        # create new dic for the options
        selected_options = {}

        # take random options for age and gender
        selected_options['dicto1'] = random.choice(obliged_adult['age'])
        selected_options['dicto2'] = random.choice(obliged_adult['gender'])

        # take checkbox from adult.html
        selected_personality_options = [key for key in options_dict_adult.keys() if key in request.form]

        # chose the random options from last step
        dicto3_options = {category: random.choice(options) for category, options in obliged_adult.items() if category not in ['age', 'gender']}
        selected_options['dicto3'] = dicto3_options

        # do dicto4 with ineligible categories
        dicto4_options = {category: random.choice(options_dict_adult[category]) for category in selected_personality_options}
        selected_options['dicto4'] = dicto4_options

        # send all to result.html
        return render_template('result.html', selected_options=selected_options)

    return render_template('adult.html', options_dict=options_dict_adult, obliged_dict=obliged_adult)


@app.route('/young', methods=['GET', 'POST'])
def young():
    if request.method == 'POST':

        # create new dic for the options
        selected_options = {}

        # take random options for age and gender
        selected_options['dicto1'] = random.choice(obliged_young['age'])
        selected_options['dicto2'] = random.choice(obliged_young['gender'])

        # take checkbox from young.html
        selected_personality_options = [key for key in options_dict_young.keys() if key in request.form]

        # chose the random options from last step
        dicto3_options = {category: random.choice(options) for category, options in obliged_young.items() if category not in ['age', 'gender']}
        selected_options['dicto3'] = dicto3_options

        # do dicto4 with ineligible categories
        dicto4_options = {category: random.choice(options_dict_young[category]) for category in selected_personality_options}
        selected_options['dicto4'] = dicto4_options

        # send all to result.html
        return render_template('result.html', selected_options=selected_options)

    return render_template('young.html', options_dict=options_dict_young, obliged_dict=obliged_young)


@app.route('/child', methods=['GET', 'POST'])
def child():
    if request.method == 'POST':

        # create new dic for the options
        selected_options = {}

        # take random options for age and gender
        selected_options['dicto1'] = random.choice(obliged_child['age'])
        selected_options['dicto2'] = random.choice(obliged_child['gender'])

        # take checkbox from child.html
        selected_personality_options = [key for key in options_dict_child.keys() if key in request.form]

        # chose the random options from last step
        dicto3_options = {category: random.choice(options) for category, options in obliged_child.items() if category not in ['age', 'gender']}
        selected_options['dicto3'] = dicto3_options

        # do dicto4 with ineligible categories
        dicto4_options = {category: random.choice(options_dict_child[category]) for category in selected_personality_options}
        selected_options['dicto4'] = dicto4_options

        # send all to result.html
        return render_template('result.html', selected_options=selected_options)

    return render_template('child.html', options_dict=options_dict_child, obliged_dict=obliged_child)

@app.route('/result')
def result():

    # build the result page with the data obtained from any previous definition
    selected_options = {key: value for key, value in request.args.items()}
    return render_template('result.html', selected_options=selected_options)


if __name__ == '__main__':
    app.run(debug=True)