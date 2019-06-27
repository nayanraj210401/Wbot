from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    # reply = fetch_reply(msg,phone_no)
    # Create reply
    resp = MessagingResponse()
    if msg == 'hi':
        resp.message('HELLO')
    elif msg == 'Hi':
        resp.message("Hi")
    elif msg == 'kk':
        resp.message("ok")
    elif msg == 'bye' or msg == 'Bye':
        resp.message("bye:)"+"thank you to spend time with me Wbot:)")
    elif msg == 'whatsup':
        resp.message("This is Wbot ")
    else:
        # resp.message(reply)
         resp.message("you Said : {}".format(msg))

    #  resp.message("You said: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)