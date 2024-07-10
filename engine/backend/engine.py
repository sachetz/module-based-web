from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__, template_folder='../frontend')

# Tree-like structure for templates
templates = {
    'start': {
        'template': None,
        'next': 'success1',
        'error': 'error1',
    },
    'success1': {
        'template': 'success1.html',
        'next': 'success2',
        'error': 'error1'
    },
    'success2': {
        'template': 'success2.html',
        'next': None,
        'error': 'error2'
    },
    'error1': {
        'template': 'error1.html',
        'next': None,
        'error': None,
    },
    'error2': {
        'template': 'error2.html',
        'next': None,
        'error': None
    }
}

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/fetch_template/<template_key>/<string:status>')
def fetch_template(template_key, status):
    if template_key not in templates:
        return jsonify({'end': True})
    template = templates[template_key]
    next_template_key = template[status]
    if next_template_key is None:
        return jsonify({'end': True})
    next_template = templates[next_template_key]['template']
    return jsonify({'template': render_template(next_template), 'next_key': next_template_key})

@app.route('/static/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(app.root_path, '../frontend/js'), filename)

if __name__ == '__main__':
    app.run(debug=True)