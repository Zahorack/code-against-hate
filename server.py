from flask import Flask, render_template, request, jsonify
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('model')


@app.route('/', methods=['GET'])
def process():
    return render_template('index.html')


@app.route('/api/v1/check', methods=['GET'])
def api_check():
    if 'message' in request.args:
        message = request.args['message']
    else:
        return jsonify({
            'result': -1,
            'msg': 'No message provided. Please specify a message to be checked.'
        }), 422

    # No hate speech = 0 / Hate speech = 1
    result = 1 if model.predict([str(message)]) > 0.5 else 0

    return jsonify({
        'result': result,
        'msg': 'Message is ' + ('' if result == 1 else 'not ') + 'a hate speech.'
    }), 200


if __name__ == '__main__':
    app.run(host='localhost', port=88)
