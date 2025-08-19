# 📚 GUIDANCE DOCUMENT - Data Quality & Anomaly Detection Project

## 🎯 **Project Overview**
This document provides comprehensive guidance for understanding and using the advanced anomaly detection system developed for mobility data analysis.

---

## 📋 **Table of Contents**
1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Code Execution Guide](#code-execution-guide)
4. [Methodology Explanation](#methodology-explanation)
5. [Results Interpretation](#results-interpretation)
6. [Troubleshooting](#troubleshooting)

---

## 🏗️ **Project Structure**

### **Core Files:**
- `cifre.py` - Original data generation script
- `data_quality_anomaly_detection_advanced.ipynb` - Main analysis notebook
- `anomalies_detected.csv` - Generated dataset

### **Documentation:**
- `ANOMALI_TESPIT_DETAYLI_ACIKLAMA_TR.md` - Turkish detailed explanations
- `DETAILED_ANOMALY_DETECTION_EXPLANATION_EN.md` - English detailed explanations
- `Guidance.md` - This guidance document

---

## 🚀 **Getting Started**

### **Prerequisites:**
```bash
pip install -r requirements.txt
```

### **Required Libraries:**
- numpy, pandas, matplotlib, seaborn
- scikit-learn (IsolationForest, RandomForestClassifier, GridSearchCV)
- scipy.stats

### **Data Generation:**
```bash
python cifre.py
```
This creates `anomalies_detected.csv` with 500 synthetic trip records.

---

## 💻 **Code Execution Guide**

### **Cell 1: Libraries & Setup**
**Purpose:** Initialize all required libraries and set random seed for reproducibility.

**What it does:**
- Imports scientific computing libraries
- Sets random seed (42) for consistent results
- Configures plotting styles

**Expected output:** "Libraries ready / Bibliothèques prêtes"

### **Cell 2: Data Loading & Quality Overview**
**Purpose:** Load data and perform initial quality assessment.

**What it does:**
- Loads CSV file
- Reports data shape and columns
- Identifies missing values
- Calculates basic statistics and IQR

**Expected output:** Data summary with shape, missing values, and IQR thresholds

### **Cell 3: Data Preprocessing & Baseline Detection**
**Purpose:** Clean data and apply traditional anomaly detection methods.

**What it does:**
- Imputes missing values using median
- Standardizes features
- Applies Z-Score (|Z| > 3)
- Applies IQR method (1.5 × IQR rule)
- Applies Isolation Forest

**Expected output:** Counts of anomalies detected by each method

### **Cell 4: Advanced Detection Methods**
**Purpose:** Apply machine learning-based anomaly detection.

**What it does:**
- PCA reconstruction error (95th percentile threshold)
- DBSCAN density-based clustering
- Ensemble voting system (5 methods)

**Expected output:** PCA outliers, DBSCAN outliers, and strong anomalies (votes ≥ 3)

### **Cell 5: Hyperparameter Optimization**
**Purpose:** Automatically tune model parameters for best performance.

**What it does:**
- Grid search for Isolation Forest parameters
- Grid search for Random Forest parameters
- 3-fold cross-validation

**Expected output:** Best parameters for both models

### **Cell 6: Model Evaluation**
**Purpose:** Assess model performance using multiple metrics.

**What it does:**
- Calculates accuracy, precision, recall, F1-score
- Generates ROC curves
- Generates Precision-Recall curves

**Expected output:** Performance metrics and visualization plots

### **Cell 7: Model Explainability**
**Purpose:** Understand how models make decisions.

**What it does:**
- Permutation importance analysis
- Partial dependence plots
- Feature contribution analysis

**Expected output:** Feature importance rankings and PDP visualizations

### **Cell 8: Comprehensive Visualization**
**Purpose:** Create dashboard of all results.

**What it does:**
- Distribution histograms
- Correlation matrix
- Geographic anomaly map
- Method comparison charts
- Voting distribution

**Expected output:** Multi-panel visualization dashboard

---

## 🔬 **Methodology Explanation**

### **1. Z-Score Method**
- **Principle:** Statistical outlier detection based on standard deviations
- **Threshold:** |Z| > 3 (covers 99.7% of normal data)
- **Use case:** Normally distributed features

### **2. IQR Method**
- **Principle:** Non-parametric outlier detection using quartiles
- **Threshold:** Beyond 1.5 × IQR from Q1/Q3
- **Use case:** Distribution-independent detection

### **3. Isolation Forest**
- **Principle:** Machine learning approach using random partitioning
- **Concept:** Anomalies are easier to isolate than normal points
- **Use case:** High-dimensional data

### **4. PCA Reconstruction Error**
- **Principle:** Dimensionality reduction with reconstruction error
- **Threshold:** 95th percentile of error distribution
- **Use case:** Linear relationship detection

### **5. DBSCAN**
- **Principle:** Density-based spatial clustering
- **Concept:** Points in sparse regions are anomalies
- **Use case:** Spatial clustering and density analysis

### **6. Ensemble Voting**
- **Principle:** Combine multiple methods for robust detection
- **Threshold:** 3+ votes indicate strong anomalies
- **Benefit:** Reduces false positives and false negatives

---

## 📊 **Results Interpretation**

### **Voting System:**
- **0 votes:** Normal data point
- **1 vote:** Suspicious (single method detected)
- **2 votes:** Probably anomalous
- **3+ votes:** Strong anomaly (multiple methods agree)

### **Performance Metrics:**
- **Accuracy:** Overall correctness (can be misleading with imbalanced data)
- **Precision:** Of detected anomalies, how many are real?
- **Recall:** Of real anomalies, how many were detected?
- **F1-Score:** Harmonic mean of precision and recall
- **ROC-AUC:** Model's ability to distinguish classes
- **Average Precision:** Area under PR curve (better for imbalanced data)

### **Visualization Guide:**
- **Histograms:** Show distribution shape and identify extreme values
- **Correlation Matrix:** Reveal relationships between features
- **Geographic Map:** Spatial clustering of anomalies
- **ROC/PR Curves:** Model performance comparison
- **Feature Importance:** Which variables matter most

---

## 🛠️ **Troubleshooting**

### **Common Issues:**

#### **1. Missing Data Errors**
```python
# Check for missing values
print(data.isnull().sum())

# Use median imputation
imputer = SimpleImputer(strategy='median')
```

#### **2. Memory Issues with Large Datasets**
```python
# Reduce sample size for testing
data_sample = data.sample(n=1000, random_state=42)
```

#### **3. Convergence Issues with DBSCAN**
```python
# Adjust parameters
dbscan = DBSCAN(eps=0.1, min_samples=3)
```

#### **4. Poor Model Performance**
```python
# Check class balance
print(y.value_counts())

# Adjust contamination parameter
iso = IsolationForest(contamination=0.05)
```

### **Performance Optimization:**
- Use `n_jobs=-1` for parallel processing
- Reduce cross-validation folds for faster execution
- Limit parameter grid size in GridSearchCV

---

## 🔧 **Customization Guide**

### **Adding New Detection Methods:**
```python
def custom_anomaly_detector(data):
    # Your custom logic here
    return anomaly_flags

# Add to ensemble
votes = (z_flags.astype(int) + 
         iqr_flags.astype(int) + 
         iso_flags.astype(int) + 
         custom_flags.astype(int))
```

### **Modifying Thresholds:**
```python
# Z-Score threshold
z_threshold = 2.5  # More sensitive

# IQR multiplier
iqr_multiplier = 2.0  # Less sensitive

# PCA percentile
pca_percentile = 90  # More sensitive
```

### **Adding New Features:**
```python
# Include new columns in analysis
numeric_cols = ['trip_duration_min', 'speed_kmh', 'new_feature']
```

---

## 📈 **Advanced Usage**

### **Real-time Anomaly Detection:**
```python
# Stream processing setup
def process_new_data(new_point):
    # Preprocess
    new_point_scaled = scaler.transform([new_point])
    
    # Get predictions from all methods
    z_score = abs(stats.zscore(new_point_scaled))
    iso_score = iso.decision_function(new_point_scaled)
    
    # Ensemble decision
    votes = sum([z_score > 3, iso_score < threshold])
    return votes >= 3
```

### **Batch Processing:**
```python
# Process data in chunks
chunk_size = 1000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    results = detect_anomalies(chunk)
    # Process results
```

---

## 📚 **Further Reading**

### **Academic Papers:**
1. Liu, F. T., et al. "Isolation Forest." ICDM 2008
2. Ester, M., et al. "A density-based algorithm for discovering clusters." KDD 1996
3. Breunig, M. M., et al. "LOF: Identifying density-based local outliers." SIGMOD 2000

### **Online Resources:**
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Anomaly Detection Tutorials](https://scikit-learn.org/stable/modules/outlier_detection.html)
- [Ensemble Methods Guide](https://scikit-learn.org/stable/modules/ensemble.html)

---

## 🤝 **Support & Contact**

### **For Technical Issues:**
- Check the troubleshooting section above
- Review error messages and logs
- Ensure all dependencies are installed

### **For Methodology Questions:**
- Refer to the detailed explanation documents
- Review academic papers in the references
- Check scikit-learn documentation

### **Repository Access:**
- **GitHub:** https://github.com/ZeynepRuveyda/data-quality-anomaly-detection
- **Issues:** Use GitHub Issues for bug reports
- **Discussions:** Use GitHub Discussions for questions

---

## 📝 **Version History**

- **v1.0** - Initial release with basic anomaly detection
- **v1.1** - Added ensemble voting system
- **v1.2** - Enhanced visualization dashboard
- **v1.3** - Added hyperparameter optimization
- **v1.4** - Improved model explainability
- **v1.5** - Comprehensive documentation and guidance

---

*This guidance document is part of the Data Quality & Anomaly Detection project developed for COSYS/GRETTIA, Université Gustave Eiffel. For questions or contributions, please refer to the repository or contact the development team.*
