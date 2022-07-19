from flask import Flask
from flask import url_for, jsonify, render_template
import os
import signal
import subprocess
import time
import sys

app = Flask(__name__)
proc = ''

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))

def procOff():
    global proc
    if not (proc==''):
        print('PARENT      : Signaling child')
        sys.stdout.flush()
        os.kill(proc.pid, signal.SIGUSR1)
        time.sleep(0.05)
        proc=''

@app.route('/')
def index():
    return render_template('index.html', 
                            last_updated=dir_last_updated('static'))

@app.route('/off', methods=['POST'])
def off():
    procOff()
    print("Lights off")
    #pixels.fill((0,0,0))
    return "Off"
	
@app.route('/magnet', methods=['POST'])
def magnet():
    procOff()
    print("Magnet lights on!")
    #pixels.fill((255,0,0))
    return "Magnet"
	
@app.route('/n2', methods=['POST'])
def n2():
    procOff()
    print("n2tank lights on!")
    #pixels.fill((0,200,200))
    return "n2tank"
	
@app.route('/he', methods=['POST'])
def he():
    procOff()
    print("hetank lights on!")
    #pixels.fill((200,100,200))
    return "hetank"
	
@app.route('/electronics', methods=['POST'])
def electronics():
    procOff()
    print("electronics lights on!")
    #pixels.fill((0,200,0))
    return "electronics"
    
@app.route('/party', methods=['POST'])
def party():
    procOff()
    print("Party lights on!")
    #simpleRainbow()
    #rainbowCycle(pixels)
    return "party"

if __name__ == "__main__":
    app.run(port=8080, debug=True)
