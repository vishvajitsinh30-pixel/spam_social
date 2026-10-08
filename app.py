from flask import Flask, render_template, request

app = Flask(__name__)

# A simple list of keywords commonly found in spam comments
SPAM_KEYWORDS = ['free', 'win', 'cash', 'prize', 'click here', 'buy now', 'urgent', 'discount', 'subscribe']

def is_this_spam(text):
    text_lower = text.lower()
    # Check if any spam keyword exists in the user's text
    for word in SPAM_KEYWORDS:
        if word in text_lower:
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        # Get the text the user typed in the HTML form
        user_message = request.form['message']
        
        # Check it using our function
        if is_this_spam(user_message):
            result = "🚨 SPAM DETECTED!"
        else:
            result = "✅ Looks Good (Not Spam)"
            
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)