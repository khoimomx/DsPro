# Student Exam Performance — Machine Learning Regression

Bài tập lớn môn Khoa học dữ liệu.  
Phân tích và dự đoán điểm thi học sinh (`Exam_Score`) dựa trên dataset [Student Exam Performance](https://www.kaggle.com/datasets/grandmaster07/student-exam-performance-dataset-analysis) từ Kaggle.

---

## Cấu trúc project

```
.
├── KHDL_BTL_RANDOMFORESTREGRESSION.ipynb   # Notebook chính
├── DB_connect.py                           # Kết nối SQL Server
├── requirements.txt                        # Danh sách thư viện
└── README.md
```

---

## 🎯 Mục tiêu

Xây dựng và so sánh 3 mô hình hồi quy dự đoán `Exam_Score`:

| # | Mô hình | Loại |
|---|---------|------|
| 1 | Linear Regression | Baseline |
| 2 | Random Forest Regressor | Tự implement + `sklearn` |
| 3 | Gradient Boosting Regressor | Tự implement + `sklearn` |

Đánh giá mô hình theo: **MAE**, **RMSE**, **R²**

---

## Pipeline

```
Dataset (Kaggle)
    │
    ▼
1. EDA + Preprocessing
   ├── Kiểm tra missing values & duplicates
   ├── IQR clipping (xử lý outlier)
   ├── Train/Test split (80/20)
   ├── StandardScaler (numerical)
   ├── OrdinalEncoder (Low/Medium/High, ...)
   └── OneHotEncoder (nominal categoricals)
    │
    ▼
2. Baseline — Linear Regression
    │
    ▼
3. Random Forest Regression
   ├── Tự implement (DecisionTreeRegressor + bagging)
   └── sklearn RandomForestRegressor
    │
    ▼
4. Gradient Boosting Regression
   ├── Tự implement
   └── sklearn GradientBoostingRegressor
    │
    ▼
5. So sánh & Rút ra insight
```

---

## Cài đặt

### Yêu cầu
- Python **3.10+**
- ODBC Driver 18 for SQL Server *(nếu dùng DB_connect.py)*

### Cài thư viện

```bash
pip install -r requirements.txt
```

### Cấu hình Kaggle API

Để download dataset tự động qua `kagglehub`, cần có file `kaggle.json`:

```bash
# Đặt file tại:
# Windows: C:\Users\<user>\.kaggle\kaggle.json
# Linux/Mac: ~/.kaggle/kaggle.json
```

Lấy API key tại: [https://www.kaggle.com/settings](https://www.kaggle.com/settings) → Account → API → Create New Token

### Cấu hình Database *(tuỳ chọn)*

Sửa thông tin kết nối trong `DB_connect.py`:

```python
server   = 'localhost'
database = 'student_db'
username = 'sa'
password = 'your_password'
```

---

## 🚀 Chạy notebook

```bash
jupyter notebook KHDL_BTL_RANDOMFORESTREGRESSION.ipynb
```

---

## 📦 Thư viện sử dụng

| Thư viện | Mục đích |
|----------|----------|
| `pandas` | Xử lý dữ liệu dạng bảng |
| `numpy` | Tính toán số học, ma trận |
| `scikit-learn` | Preprocessing, models, metrics |
| `matplotlib` | Vẽ biểu đồ |
| `kagglehub` | Tải dataset từ Kaggle |
| `sqlalchemy` | ORM kết nối database |
| `pyodbc` | Driver kết nối SQL Server |
