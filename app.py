from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from Ifasr_new import RequestApi
from config import XFYUN_CONFIG, UPLOAD_CONFIG

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'audio'
# app.config['MAX_CONTENT_LENGTH'] = UPLOAD_CONFIG['max_file_size']

# 确保上传目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in UPLOAD_CONFIG['allowed_extensions']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '没有文件上传'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '未选择文件'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': '不支持的文件格式'}), 400
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            api = RequestApi(
                appid=XFYUN_CONFIG['appid'],
                secret_key=XFYUN_CONFIG['secret_key'],
                upload_file_path=filepath
            )
            result = api.get_result()
            return jsonify({'success': True, 'text': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
# 1