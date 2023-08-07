from flask import Flask, render_template, request, jsonify
import openai

# Replace with your OpenAI API key
openai.api_key = " your own openai api key"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rate_and_rewrite', methods=['POST'])
def rate_and_rewrite():
    title = request.form['title']
    description = request.form['description']

    # Rate title
    title_rating_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Rate this Airbnb listing title on Click-worthiness, Appeal, USP: {title}",
        max_tokens=25,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Rate description
    description_rating_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Rate this Airbnb listing description on Click-worthiness, Appeal, USP: {description}",
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Rewrite title
    title_rewrite_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Rewrite this Airbnb listing title, max 15 chars, make sure it is 10/10 on Click-worthiness, Appeal, USP: {title}",
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Rewrite description
    description_rewrite_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Rewrite this Airbnb listing description, max 500 chars and minimum 300 chars, make sure it is 10/10 on Click-worthiness, Appeal, USP: {description}",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    result = {
        'title_rating': title_rating_response.choices[0].text.strip(),
        'description_rating': description_rating_response.choices[0].text.strip(),
        'title_rewrite': title_rewrite_response.choices[0].text.strip(),
        'description_rewrite': description_rewrite_response.choices[0].text.strip(),
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
