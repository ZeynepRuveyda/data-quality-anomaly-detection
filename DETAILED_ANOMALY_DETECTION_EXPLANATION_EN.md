# 🔍 DETAILED EXPLANATION OF ANOMALY DETECTION METHODS

## 📚 **Overview**
This document provides a comprehensive explanation of the 5 different methods used for anomaly detection in mobility data, the voting system, model evaluation metrics, and model explainability.

---

## 🎯 **DETAILED EXPLANATION OF ANOMALY DETECTION METHODS**

### **1. Z-Score Method**
**How it Works:**
- Calculate mean and standard deviation for each feature
- For each value: `Z = (value - mean) / standard_deviation`
- Values with `|Z| > 3` are considered anomalies

**Example:**
- Trip duration mean: 30 minutes, standard deviation: 7 minutes
- For 120-minute trip: `Z = (120-30)/7 = 12.86`
- Since `|12.86| > 3` → ANOMALY

**Why 3?** In normal distribution, 99.7% of data falls within ±3 standard deviations

**Advantages:**
- Fast computation
- Statistically robust
- Good at catching extreme values

**Disadvantages:**
- Only assumes normal distribution
- Can be slow for very large datasets

### **2. IQR (Interquartile Range) Method**
**How it Works:**
- Calculate Q1 (25th percentile) and Q3 (75th percentile)
- IQR = Q3 - Q1
- Lower bound = Q1 - 1.5×IQR
- Upper bound = Q3 + 1.5×IQR
- Values outside these bounds are anomalies

**Example:**
- Trip duration: Q1=26.5, Q3=33.3, IQR=6.8
- Lower bound = 26.5 - 1.5×6.8 = 16.3 minutes
- Upper bound = 33.3 + 1.5×6.8 = 43.5 minutes
- 1 minute < 16.3 → ANOMALY
- 120 minutes > 43.5 → ANOMALY

**Advantages:**
- Distribution independent
- Robust against outliers
- Easy to understand

**Disadvantages:**
- Can be slow for very large datasets
- Unreliable for very small datasets

### **3. Isolation Forest Method**
**How it Works:**
- Random features are selected
- Random threshold values are determined
- Data points are split in a tree structure
- Normal points are isolated at deeper levels
- Anomalies are isolated at more superficial levels

**Example:**
- Normal trip (30 minutes): isolated after 8-10 splits
- Abnormal trip (120 minutes): isolated after 2-3 splits
- Fewer splits = more anomalous

**Advantages:**
- Fast for large datasets
- Effective for high-dimensional data
- Easy parameter tuning

**Disadvantages:**
- Results can vary due to randomness
- Weak for very small datasets

### **4. PCA (Principal Component Analysis) Method**
**How it Works:**
- Compresses data to 2 dimensions (500×2 → 2×2)
- Reconstructs compressed data back to original dimensions
- Calculates difference between original and reconstructed data
- High difference (reconstruction error) indicates anomalies

**Example:**
- Normal data: low reconstruction error
- Abnormal data: high reconstruction error
- Errors above 95th percentile are considered anomalies

**Advantages:**
- Anomaly detection with dimensionality reduction
- Captures linear relationships
- Robust against noise

**Disadvantages:**
- Only captures linear relationships
- May miss non-linear anomalies

### **5. DBSCAN (Density-Based Spatial Clustering) Method**
**How it Works:**
- For each point, count neighbors within certain radius (eps=0.5)
- Points with fewer than minimum neighbors (min_samples=5) are anomalies
- Points in dense regions are normal, points in sparse regions are anomalies

**Example:**
- Normal point: finds 5+ neighbors
- Abnormal point: finds fewer than 5 neighbors → ANOMALY

**Advantages:**
- Density-based approach
- Doesn't care about cluster shape
- Robust against noise

**Disadvantages:**
- Difficult parameter selection
- Weak for clusters with different densities

---

## 🗳️ **DETAILED EXPLANATION OF 3+ VOTING SYSTEM**

### **Voting System:**
Each method gives 0 or 1 vote:
- **Z-Score**: 1 if anomaly found, 0 if not
- **IQR**: 1 if anomaly found, 0 if not  
- **Isolation Forest**: 1 if anomaly found, 0 if not
- **PCA**: 1 if anomaly found, 0 if not
- **DBSCAN**: 1 if anomaly found, 0 if not

### **Total Vote Distribution:**
- **0 votes**: No method found anomaly → Normal
- **1 vote**: Only 1 method found anomaly → Suspicious
- **2 votes**: 2 methods found anomaly → Probably anomaly
- **3+ votes**: 3+ methods found anomaly → Definite anomaly

### **Example Scenario:**
For a trip data point:
- Z-Score: 0 (within normal range)
- IQR: 1 (outside whiskers)
- Isolation Forest: 1 (isolated)
- PCA: 1 (high reconstruction error)
- DBSCAN: 0 (in dense region)

**Total: 3 votes → ANOMALY**

### **Advantages of Voting System:**
1. **Reliability**: Single method errors are compensated
2. **Comprehensiveness**: Different approaches are combined
3. **Flexibility**: Different anomaly types are captured
4. **Transparency**: Each method's contribution is visible

---

## 📊 **DETAILED EXPLANATION OF MODEL EVALUATION**

### **1. Accuracy**
**What it Measures:** Proportion of all predictions that are correct
**Formula:** `(True Positive + True Negative) / Total`
**Example:** 100 predictions, 90 correct → Accuracy = 90%

**Problem:** Can be misleading with class imbalance
- 95 normal, 5 anomalies
- "All normal" prediction → Accuracy = 95% (but missed all anomalies!)

**When to Use:**
- When classes are balanced
- For general performance assessment
- For quick comparison

### **2. Precision**
**What it Measures:** "Of what I predicted as anomaly, how many were actually anomalies?"
**Formula:** `True Positive / (True Positive + False Positive)`
**Example:** 10 anomaly predictions, 8 are real anomalies → Precision = 80%

**High Precision:** Few false alarms (false positives)

**Practical Meaning:**
- High precision = Few unnecessary warnings
- Low precision = Many false alarms
- Important for costly operations

### **3. Recall**
**What it Measures:** "Of all real anomalies, how many did I catch?"
**Formula:** `True Positive / (True Positive + False Negative)`
**Example:** 20 real anomalies, caught 16 → Recall = 80%

**High Recall:** Few missed anomalies (false negatives)

**Practical Meaning:**
- High recall = Few missed anomalies
- Low recall = Many anomalies missed
- Important for security-critical applications

### **4. F1-Score**
**What it Measures:** Harmonic mean of Precision and Recall
**Formula:** `2 × (Precision × Recall) / (Precision + Recall)`
**Why?** Balances Precision and Recall

**Example:**
- Precision = 0.8, Recall = 0.6
- F1 = 2 × (0.8 × 0.6) / (0.8 + 0.6) = 0.69

**Advantages:**
- Single metric for performance assessment
- Balance between Precision and Recall
- More reliable with class imbalance

### **5. ROC-AUC (Receiver Operating Characteristic - Area Under Curve)**
**What it Measures:** Model's ability to distinguish between classes
**Value Range:** 0.5 (random) - 1.0 (perfect)

**Interpretation:**
- 0.5-0.6: Poor
- 0.6-0.7: Fair
- 0.7-0.8: Good
- 0.8-0.9: Very good
- 0.9-1.0: Excellent

**When to Use:**
- For model comparison
- For general performance assessment
- For threshold selection

### **6. Average Precision (AP)**
**What it Measures:** Area under Precision-Recall curve
**Why Important:** More reliable than ROC-AUC with class imbalance
**Value Range:** 0.0 - 1.0

**Advantages:**
- Reliable with class imbalance
- Shows Precision-Recall balance
- Especially important for anomaly detection

---

## 🧠 **DETAILED EXPLANATION OF MODEL EXPLAINABILITY**

### **1. Permutation Importance**
**What it Measures:** How much a feature contributes to model performance

**How it Works:**
1. Model is trained with normal data
2. One feature is randomly shuffled (permutation)
3. Model performance is measured again
4. Performance drop is calculated
5. This process is repeated 20 times
6. Average performance drop is calculated

**Example:**
- Normal performance: F1 = 0.8
- After shuffling speed feature: F1 = 0.6
- Performance drop: 0.2
- **Result:** Speed feature is very important

**Why Important?** 
- Shows which features are critical for anomaly detection
- Increases confidence in model decisions
- Gives confidence to domain experts

### **2. Partial Dependence Plot (PDP)**
**What it Shows:** How model prediction changes when a feature value changes

**How it Works:**
1. One feature's value is systematically changed
2. Other features are kept constant
3. Model prediction is obtained for each value
4. Graph is plotted

**Example Scenario:**
```
Trip Duration → Anomaly Probability
10 minutes    → 5% (normal)
20 minutes    → 10% (normal)
30 minutes    → 15% (normal)
60 minutes    → 70% (anomaly!)
90 minutes    → 95% (anomaly!)
120 minutes   → 99% (anomaly!)
```

**Interpretation:**
- Up to 30 minutes: Normal
- 60+ minutes: High anomaly risk
- 90+ minutes: Definite anomaly

### **3. Practical Benefits of PDP**
**1. Threshold Determination:**
- What trip duration should be considered anomaly?
- %50 threshold can be determined by looking at PDP

**2. Business Rules:**
- "Trips longer than 60 minutes should be investigated"
- "Trips longer than 90 minutes should be automatically rejected"

**3. Domain Expert Approval:**
- Statistician: "Is this threshold logical?"
- Transportation expert: "Are these durations realistic?"

**4. Risk Assessment:**
- Which values are critical?
- Which ranges are safe?
- Which thresholds should be used?

### **4. PDP vs Permutation Importance**
**Permutation Importance:**
- Which feature is more important?
- Gives numerical value
- Can be compared
- General importance ranking

**PDP:**
- How does the feature affect the outcome?
- Visual analysis
- Threshold determination
- Detailed behavior analysis

---

## 🎯 **PRACTICAL APPLICATION EXAMPLES**

### **Scenario 1: Trip Duration Anomaly**
**Data:** 120-minute trip
**Z-Score:** 1 (anomaly)
**IQR:** 1 (anomaly)  
**Isolation Forest:** 1 (anomaly)
**PCA:** 1 (anomaly)
**DBSCAN:** 0 (normal)

**Total:** 4 votes → **DEFINITE ANOMALY**

**Explanation:** 4/5 methods found anomaly, this trip is truly abnormal

**Practical Application:**
- Automatic warning system
- Marking for manual review
- Route optimization suggestion

### **Scenario 2: Suspicious Speed**
**Data:** 80 km/h speed
**Z-Score:** 0 (normal)
**IQR:** 1 (anomaly)
**Isolation Forest:** 0 (normal)
**PCA:** 0 (normal)
**DBSCAN:** 0 (normal)

**Total:** 1 vote → **SUSPICIOUS**

**Explanation:** Only IQR found anomaly, other methods said normal

**Practical Application:**
- Low priority investigation
- Temporary marking
- Collect more data

### **Scenario 3: Normal Trip**
**Data:** 35-minute trip
**Z-Score:** 0 (normal)
**IQR:** 0 (normal)
**Isolation Forest:** 0 (normal)
**PCA:** 0 (normal)
**DBSCAN:** 0 (normal)

**Total:** 0 votes → **NORMAL**

**Explanation:** No method found anomaly, this trip is normal

**Practical Application:**
- Automatic approval
- Fast processing
- Resource saving

---

## 🔧 **SYSTEM SETUP AND PARAMETER SETTINGS**

### **Z-Score Parameters:**
- **Threshold:** 3 (default), 2.5 (more sensitive), 3.5 (less sensitive)
- **Feature selection:** All numerical features
- **Normalization:** Not required

### **IQR Parameters:**
- **Multiplier:** 1.5 (default), 1.0 (more sensitive), 2.0 (less sensitive)
- **Feature selection:** All numerical features
- **Normalization:** Not required

### **Isolation Forest Parameters:**
- **n_estimators:** 100 (default), range 50-200
- **contamination:** 0.1 (default), range 0.05-0.2
- **max_samples:** 'auto' (default), range 100-200

### **PCA Parameters:**
- **n_components:** 2 (default), range 1-3
- **Threshold:** 95th percentile (default), range 90-99
- **Normalization:** Required

### **DBSCAN Parameters:**
- **eps:** 0.5 (default), range 0.1-1.0
- **min_samples:** 5 (default), range 3-10
- **Normalization:** Required

---

## 📈 **PERFORMANCE OPTIMIZATION**

### **Data Preprocessing:**
1. **Missing Data:** Median imputation
2. **Normalization:** StandardScaler
3. **Feature Selection:** Numerical features
4. **Data Cleaning:** Outlier control

### **Model Selection:**
1. **Isolation Forest:** Fast, general purpose
2. **Random Forest:** Accurate, explainable
3. **Ensemble:** Reliable, comprehensive

### **Hyperparameter Optimization:**
1. **Grid Search:** Systematic search
2. **Cross Validation:** 3-fold CV
3. **Metrics:** F1-score, ROC-AUC
4. **Parallel Processing:** n_jobs=-1

---

## 🚀 **CONCLUSION AND RECOMMENDATIONS**

### **System Advantages:**
1. **Multi-Method:** Different approaches are combined
2. **Reliable:** Ensemble decisions are more robust
3. **Explainable:** Model decisions are understandable
4. **Flexible:** Adaptable to different data types

### **Application Areas:**
1. **Transportation Systems:** Trip anomalies
2. **Finance:** Transaction anomalies
3. **Healthcare:** Medical data anomalies
4. **Manufacturing:** Quality control anomalies

### **Future Developments:**
1. **Deep Learning:** LSTM, Autoencoder
2. **Real-Time:** Streaming data analysis
3. **Automatic Thresholds:** Adaptive parameter tuning
4. **Multi-Dimensional:** Time series analysis

---

## 📚 **RESOURCES AND REFERENCES**

1. **Z-Score:** Standard Score, Normal Distribution
2. **IQR:** Tukey's Method, Box Plot
3. **Isolation Forest:** Liu et al. (2008)
4. **PCA:** Principal Component Analysis, Reconstruction Error
5. **DBSCAN:** Density-Based Clustering, Ester et al. (1996)
6. **Ensemble Methods:** Voting Systems, Majority Decision
7. **Model Evaluation:** Classification Metrics, ROC-AUC
8. **Explainability:** Permutation Importance, Partial Dependence

---

*This document contains the detailed technical explanation of the system developed for anomaly detection in mobility data. Please contact us for any questions.*
