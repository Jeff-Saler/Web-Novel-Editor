from flask import Flask
import flask
import pickle
import pandas as pd
import keras
from googletrans import Translator
import numpy as np
from static.test_model import decode_sequence

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/input' ,methods= ['GET','POST'])
def input():
    return flask.render_template('input.html')

@app.route('/text',methods=['POST'])
def text():
    text=str(flask.request.form['text'])
    num_encoder_tokens,num_decoder_tokens,max_encoder_seq_length,max_decoder_seq_length=pickle.load(open('static/pickles/variables.pkl','rb'))

    input_token_index,target_token_index=pickle.load(open('static/pickles/token_indices.pkl','rb'))

    model=keras.models.load_model('static/s2s.h5')
    encoder_model=keras.models.load_model('static/encoder.h5')
    decoder_model=keras.models.load_model('static/decoder.h5')

    reverse_input_char_index,reverse_target_char_index = pickle.load(open('static/pickles/reverse.pkl','rb'))

    translator=Translator()
    input=[]
    text=text.split('。')
    for line in text:
        if len(line)>8:
            input.append(translator.translate(line).text)

    input_data = np.zeros((len(input), max_encoder_seq_length, num_encoder_tokens), dtype='float32')

    for i, input_text in enumerate(input):
        for t, char in enumerate(input_text):
            try:
                input_data[i, t, input_token_index[char]] = 1.
            except:
                KeyError

    decoded_chapter=''
    for line in input_data:
        decoded_chapter+='{}\n'.format(decode_sequence(line[np.newaxis,:],encoder_model,decoder_model,num_decoder_tokens,target_token_index,reverse_target_char_index,max_decoder_seq_length))
    return(decoded_chapter)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
