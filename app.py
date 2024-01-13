# -*- coding: utf-8 -*-
# time:2024/1/9 15:33
# file app.py.py
# outhor:czy
# email:1060324818@qq.com

from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        code = request.form.get('code')

        # Save code to a temporary file
        with open("temp_code.py", "w") as f:
            f.write(code)

        # Run the code and capture the output
        process = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True)

        # Get the output from the process
        output = process.stdout + process.stderr

        return render_template('index.html', output=output)
    else:
        return render_template('index.html')

# if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=5002)
if __name__ == '__main__':
    app.run(host='2409:8954:6699:96a0:227:2aff:fe95:9d1a', port=5000)

