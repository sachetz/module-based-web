from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__, template_folder='../frontend')

templates = [
    {'success': 'success1.html', 'error': 'error1.html'},
    {'success': 'success2.html', 'error': 'error2.html'},
]

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/fetch_template/<int:index>/<string:status>')
def fetch_template(index, status):
    if index >= len(templates):
        return jsonify({'end': True})
    template = templates[index][status]
    return jsonify({'template': render_template(template)})

@app.route('/static/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(app.root_path, '../frontend/js'), filename)

if __name__ == '__main__':
    app.run(debug=True)