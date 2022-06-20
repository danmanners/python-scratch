import random
import urllib3

from flask import Flask

app = Flask(__name__)

# def downloadDictionary()

def randomNumber(start=0, end=1000, step=1):
    value = random.randrange(start, end, step)
    return value


@app.route('/random/word')
def randomWord(dictionary='https://github.com/dwyl/english-words/raw/master/words.txt'):

    http = urllib3.PoolManager()
    r = http.request('GET', dictionary)

    if r.status == 200:
        data = (r.data).decode('UTF-8')
        lineCount = len(data.split('\n'))
        lineNumber = randomNumber(start=0, end=lineCount)
        return str(data.split("\n")[lineNumber] + "\n")

    else:
        return f'The dictionary URL was unavailable!'


@app.route('/random/number')
def random_route():
    number = randomNumber()
    return f'{number}\n'
