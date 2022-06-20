import random
import urllib3

from flask import Flask

app = Flask(__name__)

dictionaryData = list()


@app.route('/dict/refresh')
# When called, download the dictionary
def downloadDictionary(dictionary='https://github.com/dwyl/english-words/raw/master/words.txt'):
    http = urllib3.PoolManager()
    r = http.request('GET', dictionary)

    if r.status == 200:
        data = (r.data).decode('UTF-8')
        # Update the list GLOBALLY
        global dictionaryData
        dictionaryData = data.splitlines()
        return f'Dictionary refreshed!\n'
    else:
        return f'The dictionary URL was unavailable!'


def randomNumber(start=0, end=1000, step=1):
    value = random.randrange(start, end, step)
    return value


@app.route('/random')
def randomObject():
    selector = randomNumber(start=1, end=3)
    if str(selector) == '1':
        return randomWord()
    if str(selector) == '2':
        randomInt = f'{randomNumber()}\n'
        return randomInt


@app.route('/random/word')
def randomWord():

    lineCount = len(dictionaryData)
    lineNumber = randomNumber(start=0, end=lineCount)
    return str(dictionaryData[lineNumber] + "\n")


@app.route('/random/number')
def random_route():
    number = randomNumber()
    return number


if __name__ == '__main__':
    downloadDictionary()
    app.run(host='0.0.0.0', port=5000)
