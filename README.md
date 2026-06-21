# Skripsi - YOLOv11 Object Detection

<p align="center">
  <img src="train/results.png" width="800">
</p>

Sistem deteksi objek berbasis web menggunakan model **YOLOv11** dengan fitur upload gambar dan deteksi real-time melalui kamera.

---

## Hasil Training Model

| Metric | Value |
|--------|-------|
| **Epoch** | 400 |
| **Base Model** | YOLOv11s |
| **Image Size** | 640x640 |
| **Batch Size** | 16 |
| **Precision** | 90.77% |
| **Recall** | 88.34% |
| **mAP@50** | 91.33% |
| **mAP@50-95** | 80.71% |

### Training Configuration

| Parameter | Value |
|-----------|-------|
| Optimizer | Auto |
| Learning Rate | 0.01 |
| Momentum | 0.937 |
| Weight Decay | 0.0005 |
| Warmup Epochs | 3.0 |
| Patience | 100 |
| Box Loss | 7.5 |
| Class Loss | 0.5 |
| DFL Loss | 1.5 |

---

## Hasil Visualisasi Training

### Training & Validation Loss

<p align="center">
  <img src="train/results.png" width="800">
</p>

Grafik di atas menunjukkan proses training selama 400 epoch:
- **Train/Box Loss**: Loss untuk deteksi bounding box
- **Train/CLS Loss**: Loss untuk klasifikasi
- **Train/DFL Loss**: Loss untuk distribution focal loss
- **Metrics**: Precision, Recall, mAP@50, dan mAP@50-95

---

### Confusion Matrix

<p align="center">
  <img src="train/confusion_matrix.png" width="600">
</p>

<p align="center">
  <img src="train/confusion_matrix_normalized.png" width="600">
</p>

Confusion matrix menunjukkan performa model dalam mengklasifikasikan setiap kelas. Nilai diagonal yang tinggi menunjukkan akurasi yang baik.

---

### Label Distribution

<p align="center">
  <img src="train/labels.jpg" width="600">
</p>

Distribusi label pada dataset training dan validasi.

---

### Precision-Recall Curves

<table align="center">
  <tr>
    <td align="center"><b>F1 Curve</b></td>
    <td align="center"><b>PR Curve</b></td>
  </tr>
  <tr>
    <td><img src="train/BoxF1_curve.png" width="400"></td>
    <td><img src="train/BoxPR_curve.png" width="400"></td>
  </tr>
  <tr>
    <td align="center"><b>Precision Curve</b></td>
    <td align="center"><b>Recall Curve</b></td>
  </tr>
  <tr>
    <td><img src="train/BoxP_curve.png" width="400"></td>
    <td><img src="train/BoxR_curve.png" width="400"></td>
  </tr>
</table>

---

### Training Batches

<table align="center">
  <tr>
    <td align="center"><b>Batch 0</b></td>
    <td align="center"><b>Batch 1</b></td>
    <td align="center"><b>Batch 2</b></td>
  </tr>
  <tr>
    <td><img src="train/train_batch0.jpg" width="250"></td>
    <td><img src="train/train_batch1.jpg" width="250"></td>
    <td><img src="train/train_batch2.jpg" width="250"></td>
  </tr>
</table>

---

### Validation Predictions

<table align="center">
  <tr>
    <td align="center"><b>Batch 0 - Labels</b></td>
    <td align="center"><b>Batch 0 - Predictions</b></td>
  </tr>
  <tr>
    <td><img src="train/val_batch0_labels.jpg" width="400"></td>
    <td><img src="train/val_batch0_pred.jpg" width="400"></td>
  </tr>
  <tr>
    <td align="center"><b>Batch 1 - Labels</b></td>
    <td align="center"><b>Batch 1 - Predictions</b></td>
  </tr>
  <tr>
    <td><img src="train/val_batch1_labels.jpg" width="400"></td>
    <td><img src="train/val_batch1_pred.jpg" width="400"></td>
  </tr>
  <tr>
    <td align="center"><b>Batch 2 - Labels</b></td>
    <td align="center"><b>Batch 2 - Predictions</b></td>
  </tr>
  <tr>
    <td><img src="train/val_batch2_labels.jpg" width="400"></td>
    <td><img src="train/val_batch2_pred.jpg" width="400"></td>
  </tr>
</table>

---

## Google Colab

Untuk menjalankan training dan inference di Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Okq_ngEsGPYY2J52cJYwZEmzRCpMuKxE?authuser=2#scrollTo=6OTdNW7YyKvT)

Atau gunakan notebook `.ipynb` yang tersedia di repository ini (`YOLOv11_Training.ipynb`).

---

## Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/MaulanaSandyy/Skripsi-Yolov11.git
cd Skripsi-Yolov11
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi

```bash
python app.py
```

Buka browser dan akses: `http://localhost:5000`

---

## Penggunaan

### Upload Gambar

<p align="center">
  <i>Tab Upload Gambar pada aplikasi web</i>
</p>

1. Klik tab **Upload Gambar**
2. Drag & drop atau klik untuk memilih file gambar
3. Klik tombol **Detect Objek**
4. Hasil deteksi akan menampilkan bounding box, nama objek, dan confidence score

### Kamera Real-time

<p align="center">
  <i>Tab Kamera Realtime pada aplikasi web</i>
</p>

1. Klik tab **Kamera Realtime**
2. Klik tombol **Mulai Kamera**
3. Klik **Deteksi Sekarang** untuk melakukan deteksi pada frame saat ini
4. Klik **Stop** untuk menghentikan kamera

---

## Detection Parameters

| Parameter | Value |
|-----------|-------|
| Confidence Threshold | 0.47 |
| IoU Threshold | 0.45 |
| Image Size | 640x640 |

---

## Struktur Proyek

```
Skripsi-Yolov11/
├── app.py                      # Flask backend
├── my_model.pt                 # Model YOLOv11 yang sudah di-training
├── requirements.txt            # Dependencies
├── data.zip                    # Dataset
├── YOLOv11_Training.ipynb      # Notebook untuk Google Colab
├── templates/
│   └── index.html              # Frontend UI
└── train/
    ├── args.yaml               # Training arguments
    ├── results.csv             # Training metrics per epoch
    ├── results.png             # Grafik training
    ├── confusion_matrix.png    # Confusion matrix
    ├── confusion_matrix_normalized.png
    ├── BoxF1_curve.png         # F1 Curve
    ├── BoxPR_curve.png         # PR Curve
    ├── BoxP_curve.png          # Precision Curve
    ├── BoxR_curve.png          # Recall Curve
    ├── labels.jpg              # Label distribution
    ├── train_batch*.jpg        # Contoh training batch
    ├── val_batch*_labels.jpg   # Validation labels
    ├── val_batch*_pred.jpg     # Validation predictions
    └── weights/
        ├── best.pt             # Bobot terbaik
        └── last.pt             # Bobot terakhir
```

---

## Tech Stack

- **Backend**: Python, Flask
- **Model**: YOLOv11s (Ultralytics)
- **Frontend**: HTML, CSS, JavaScript
- **Camera**: WebRTC (getUserMedia API)

---

## License

MIT License
