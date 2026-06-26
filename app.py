from flask import Flask, render_template, request
import nmap

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    scan_result = None
    if request.method == 'POST':
        target = request.form['target']
        nm = nmap.PortScanner()
        # 1-1024 ports ka scan
        nm.scan(target, '1-1024')
        scan_result = nm[target]['tcp']
    return render_template('index.html', result=scan_result)

if __name__ == '__main__':
    app.run(debug=True)
