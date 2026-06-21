import os
import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify, Response, send_from_directory
from ultralytics import YOLO
from werkzeug.utils import secure_filename
import base64
import time

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'my_model.pt')
model = YOLO(MODEL_PATH)

CLASS_NAMES = model.names
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'Tidak ada gambar yang diunggah'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Nama file kosong'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    results = model(filepath, conf=0.47, iou=0.45, imgsz=640)
    result = results[0]

    detections = []
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        cls_name = CLASS_NAMES[cls_id]
        detections.append({
            'bbox': [x1, y1, x2, y2],
            'confidence': round(conf, 4),
            'class': cls_name,
            'class_id': cls_id
        })

    annotated = result.plot()
    _, buffer = cv2.imencode('.jpg', annotated)
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    return jsonify({
        'image': img_base64,
        'detections': detections,
        'count': len(detections)
    })

@app.route('/video_feed')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

def generate_frames():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame, conf=0.47, iou=0.45, imgsz=640, verbose=False)
        annotated = results[0].plot()

        _, buffer = cv2.imencode('.jpg', annotated, [cv2.IMWRITE_JPEG_QUALITY, 80])
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

@app.route('/detect_frame', methods=['POST'])
def detect_frame():
    data = request.get_json()
    if 'image' not in data:
        return jsonify({'error': 'Tidak ada data gambar'}), 400

    img_data = data['image'].split(',')[1] if ',' in data['image'] else data['image']
    img_bytes = base64.b64decode(img_data)
    nparr = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if frame is None:
        return jsonify({'error': 'Gagal decode gambar'}), 400

    results = model(frame, conf=0.47, iou=0.45, imgsz=640, verbose=False)
    result = results[0]

    detections = []
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        cls_name = CLASS_NAMES[cls_id]
        detections.append({
            'bbox': [x1, y1, x2, y2],
            'confidence': round(conf, 4),
            'class': cls_name,
            'class_id': cls_id
        })

    annotated = result.plot()
    _, buffer = cv2.imencode('.jpg', annotated)
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    return jsonify({
        'image': img_base64,
        'detections': detections,
        'count': len(detections)
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
