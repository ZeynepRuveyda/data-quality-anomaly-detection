# -*- coding: utf-8 -*-
"""
Data Quality Anomaly Detection Analysis Script
Mobilite Sistemlerinde Veri Kalitesi Anomali Tespiti Analiz Scripti
Script d'Analyse de Détection d'Anomalies dans la Qualité des Données

This script contains all the analysis cells for the Jupyter notebook.
Copy each section into separate Jupyter cells.
"""

# ============================================================================
# CELL 1: LIBRARIES AND IMPORTS
# ============================================================================
print("=== CELL 1: LIBRARIES AND IMPORTS ===")
print("Copy this code into the first Jupyter cell:")

cell1_code = '''
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from scipy import stats
from scipy.stats import randint, uniform
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)
plt.style.use('default')
sns.set_palette("husl")

print("✅ Libraries imported successfully")
'''

print(cell1_code)

# ============================================================================
# CELL 2: DATA LOADING AND BASIC STATISTICS
# ============================================================================
print("\n=== CELL 2: DATA LOADING AND BASIC STATISTICS ===")
print("Copy this code into the second Jupyter cell:")

cell2_code = '''
# Load the CSV data
data = pd.read_csv('anomalies_detected.csv')

print("📊 Dataset Overview:")
print(f"Shape: {data.shape}")
print(f"Columns: {list(data.columns)}")
print("\n📈 Basic Statistics:")
print(data.describe())

print("\n❌ Missing Values:")
print(data.isnull().sum())

print("\n📋 Data Types:")
print(data.dtypes)
'''

print(cell2_code)

# ============================================================================
# CELL 3: ANOMALY DETECTION ANALYSIS
# ============================================================================
print("\n=== CELL 3: ANOMALY DETECTION ANALYSIS ===")
print("Copy this code into the third Jupyter cell:")

cell3_code = '''
# Analyze anomaly detection results
print("🎯 ANOMALY DETECTION ANALYSIS")
print("=" * 50)

# Count anomalies for each method
zscore_count = data['anomaly_zscore'].sum()
iqr_count = data['anomaly_iqr'].sum()
isolation_count = data['anomaly_isolation'].sum()

print(f"Z-Score Anomalies: {zscore_count}")
print(f"IQR Anomalies: {iqr_count}")
print(f"Isolation Forest Anomalies: {isolation_count}")

# Find common anomalies
common_anomalies = data[data['anomaly_zscore'] & data['anomaly_iqr'] & data['anomaly_isolation']]
print(f"\n🔍 Common Anomalies (All Methods): {len(common_anomalies)}")

# Show some examples
if len(common_anomalies) > 0:
    print("\n🔍 Examples of Common Anomalies:")
    print(common_anomalies[['trip_duration_min', 'speed_kmh', 'latitude', 'longitude']].head())
'''

print(cell3_code)

# ============================================================================
# CELL 4: DATA QUALITY ANALYSIS
# ============================================================================
print("\n=== CELL 4: DATA QUALITY ANALYSIS ===")
print("Copy this code into the fourth Jupyter cell:")

cell4_code = '''
# Data Quality Analysis
print("🔍 DATA QUALITY ANALYSIS")
print("=" * 50)

# Check for missing values
missing_data = data.isnull().sum()
missing_percentage = (missing_data / len(data)) * 100

print("📊 Missing Data Analysis:")
for col, count, percentage in zip(missing_data.index, missing_data.values, missing_percentage.values):
    if count > 0:
        print(f"{col}: {count} ({percentage:.2f}%)")

# Check for extreme values
print("\n📈 Extreme Value Analysis:")
for col in ['trip_duration_min', 'speed_kmh']:
    if col in data.columns:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        extreme_low = (data[col] < lower_bound).sum()
        extreme_high = (data[col] > upper_bound).sum()
        
        print(f"{col}:")
        print(f"  Extreme Low: {extreme_low}")
        print(f"  Extreme High: {extreme_high}")
'''

print(cell4_code)

# ============================================================================
# CELL 5: ADVANCED ANOMALY DETECTION
# ============================================================================
print("\n=== CELL 5: ADVANCED ANOMALY DETECTION ===")
print("Copy this code into the fifth Jupyter cell:")

cell5_code = '''
# Advanced Anomaly Detection Methods
print("🔍 ADVANCED ANOMALY DETECTION")
print("=" * 50)

# Prepare data for advanced methods
numeric_cols = ['trip_duration_min', 'speed_kmh']
data_clean = data[numeric_cols].dropna()

# Standardize data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_clean)

# 1. DBSCAN Clustering
print("🔍 1. DBSCAN Clustering Analysis")
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(data_scaled)
dbscan_anomalies = (dbscan_labels == -1).sum()
print(f"DBSCAN Anomalies: {dbscan_anomalies}")

# 2. PCA-based Anomaly Detection
print("\n🔍 2. PCA-based Anomaly Detection")
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# Calculate reconstruction error
data_reconstructed = pca.inverse_transform(data_pca)
reconstruction_error = np.mean((data_scaled - data_reconstructed) ** 2, axis=1)
pca_threshold = np.percentile(reconstruction_error, 95)
pca_anomalies = (reconstruction_error > pca_threshold).sum()
print(f"PCA Anomalies: {pca_anomalies}")

# 3. Ensemble Method
print("\n🔍 3. Ensemble Method")
ensemble_scores = np.zeros(len(data_clean))

# Z-score method
z_scores = np.abs(stats.zscore(data_clean))
ensemble_scores += (z_scores > 3).any(axis=1)

# IQR method
Q1 = data_clean.quantile(0.25)
Q3 = data_clean.quantile(0.75)
IQR = Q3 - Q1
iqr_outliers = ((data_clean < (Q1 - 1.5 * IQR)) | (data_clean > (Q3 + 1.5 * IQR))).any(axis=1)
ensemble_scores += iqr_outliers

# Isolation Forest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_pred = iso_forest.fit_predict(data_clean)
ensemble_scores += (iso_pred == -1)

# Final ensemble decision
ensemble_anomalies = (ensemble_scores >= 2).sum()
print(f"Ensemble Anomalies: {ensemble_anomalies}")
'''

print(cell5_code)

# ============================================================================
# CELL 6: HYPERPARAMETER OPTIMIZATION
# ============================================================================
print("\n=== CELL 6: HYPERPARAMETER OPTIMIZATION ===")
print("Copy this code into the sixth Jupyter cell:")

cell6_code = '''
# Hyperparameter Optimization
print("⚙️ HYPERPARAMETER OPTIMIZATION")
print("=" * 50)

# Prepare data for ML models
X = data_clean
y = (ensemble_scores >= 2).astype(int)  # Use ensemble as ground truth

# Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1. Isolation Forest Optimization
print("🔍 1. Isolation Forest Optimization")
iso_param_grid = {
    'n_estimators': [50, 100, 200],
    'contamination': [0.05, 0.1, 0.15],
    'max_samples': ['auto', 100, 200]
}

iso_grid = GridSearchCV(IsolationForest(random_state=42), iso_param_grid, cv=3, scoring='neg_mean_squared_error')
iso_grid.fit(X_train)

print(f"Best Isolation Forest Parameters: {iso_grid.best_params_}")
print(f"Best Score: {iso_grid.best_score_:.4f}")

# 2. Random Forest for Anomaly Classification
print("\n🔍 2. Random Forest Optimization")
rf_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, None],
    'min_samples_split': [2, 5, 10]
}

rf_grid = GridSearchCV(RandomForestClassifier(random_state=42), rf_param_grid, cv=3, scoring='f1')
rf_grid.fit(X_train, y_train)

print(f"Best Random Forest Parameters: {rf_grid.best_params_}")
print(f"Best F1 Score: {rf_grid.best_score_:.4f}")
'''

print(cell6_code)

# ============================================================================
# CELL 7: PERFORMANCE EVALUATION
# ============================================================================
print("\n=== CELL 7: PERFORMANCE EVALUATION ===")
print("Copy this code into the seventh Jupyter cell:")

cell7_code = '''
# Performance Evaluation
print("📊 PERFORMANCE EVALUATION")
print("=" * 50)

# Evaluate best models
best_iso = iso_grid.best_estimator_
best_rf = rf_grid.best_estimator_

# Isolation Forest predictions
iso_pred = best_iso.predict(X_test)
iso_pred_binary = (iso_pred == -1).astype(int)

# Random Forest predictions
rf_pred = best_rf.predict(X_test)
rf_prob = best_rf.predict_proba(X_test)[:, 1]

# Calculate metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

print("🎯 Isolation Forest Performance:")
print(f"Accuracy: {accuracy_score(y_test, iso_pred_binary):.4f}")
print(f"Precision: {precision_score(y_test, iso_pred_binary):.4f}")
print(f"Recall: {recall_score(y_test, iso_pred_binary):.4f}")
print(f"F1-Score: {f1_score(y_test, iso_pred_binary):.4f}")

print("\n🎯 Random Forest Performance:")
print(f"Accuracy: {accuracy_score(y_test, rf_pred):.4f}")
print(f"Precision: {precision_score(y_test, rf_pred):.4f}")
print(f"Recall: {recall_score(y_test, rf_pred):.4f}")
print(f"F1-Score: {f1_score(y_test, rf_pred):.4f}")
print(f"ROC-AUC: {roc_auc_score(y_test, rf_prob):.4f}")
'''

print(cell7_code)

# ============================================================================
# CELL 8: VISUALIZATION AND RESULTS
# ============================================================================
print("\n=== CELL 8: VISUALIZATION AND RESULTS ===")
print("Copy this code into the eighth Jupyter cell:")

cell8_code = '''
# Visualization and Results
print("📊 VISUALIZATION AND RESULTS")
print("=" * 50)

# Create comprehensive visualization
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 1. Trip Duration Distribution
axes[0, 0].hist(data['trip_duration_min'].dropna(), bins=30, alpha=0.7, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Trip Duration Distribution\nDağılımı / Distribution')
axes[0, 0].set_xlabel('Duration (min)')
axes[0, 0].set_ylabel('Frequency')

# 2. Speed Distribution
axes[0, 1].hist(data['speed_kmh'].dropna(), bins=30, alpha=0.7, color='lightgreen', edgecolor='black')
axes[0, 1].set_title('Speed Distribution\nDağılımı / Distribution')
axes[0, 1].set_xlabel('Speed (km/h)')
axes[0, 1].set_ylabel('Frequency')

# 3. GPS Coordinates
axes[0, 2].scatter(data['longitude'], data['latitude'], alpha=0.6, c=data['anomaly_isolation'], cmap='viridis')
axes[0, 2].set_title('GPS Coordinates with Anomalies\nGPS Koordinatları ve Anomaliler')
axes[0, 2].set_xlabel('Longitude')
axes[0, 2].set_ylabel('Latitude')

# 4. Anomaly Comparison
methods = ['Z-Score', 'IQR', 'Isolation Forest']
counts = [data['anomaly_zscore'].sum(), data['anomaly_iqr'].sum(), data['anomaly_isolation'].sum()]

axes[1, 0].bar(methods, counts, color=['red', 'orange', 'purple'], alpha=0.7)
axes[1, 0].set_title('Anomaly Detection Comparison\nAnomali Tespit Karşılaştırması')
axes[1, 0].set_ylabel('Number of Anomalies')

# 5. Correlation Matrix
corr_matrix = data[['trip_duration_min', 'speed_kmh', 'latitude', 'longitude']].corr()
im = axes[1, 1].imshow(corr_matrix, cmap='coolwarm', aspect='auto')
axes[1, 1].set_title('Correlation Matrix\nKorelasyon Matrisi')
axes[1, 1].set_xticks(range(len(corr_matrix.columns)))
axes[1, 1].set_yticks(range(len(corr_matrix.columns)))
axes[1, 1].set_xticklabels(corr_matrix.columns, rotation=45)
axes[1, 1].set_yticklabels(corr_matrix.columns)

# Add colorbar
plt.colorbar(im, ax=axes[1, 1])

# 6. Performance Metrics
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
iso_scores = [accuracy_score(y_test, iso_pred_binary), precision_score(y_test, iso_pred_binary), 
              recall_score(y_test, iso_pred_binary), f1_score(y_test, iso_pred_binary)]
rf_scores = [accuracy_score(y_test, rf_pred), precision_score(y_test, rf_pred), 
             recall_score(y_test, rf_pred), f1_score(y_test, rf_pred)]

x = np.arange(len(metrics))
width = 0.35

axes[1, 2].bar(x - width/2, iso_scores, width, label='Isolation Forest', alpha=0.7)
axes[1, 2].bar(x + width/2, rf_scores, width, label='Random Forest', alpha=0.7)
axes[1, 2].set_title('Model Performance Comparison\nModel Performans Karşılaştırması')
axes[1, 2].set_xticks(x)
axes[1, 2].set_xticklabels(metrics, rotation=45)
axes[1, 2].set_ylabel('Score')
axes[1, 2].legend()

plt.tight_layout()
plt.show()

print("✅ Comprehensive analysis completed!")
'''

print(cell8_code)

# ============================================================================
# INSTRUCTIONS
# ============================================================================
print("\n" + "="*80)
print("📋 INSTRUCTIONS / TALİMATLAR / INSTRUCTIONS:")
print("="*80)
print("1. Open Jupyter notebook in your browser")
print("2. Create 8 new cells (code type)")
print("3. Copy each cell code above into separate Jupyter cells")
print("4. Run cells in order from top to bottom")
print("5. Each cell will show the analysis results")

print("\n🎯 This analysis covers all PhD position requirements:")
print("- Data Quality Analysis")
print("- Advanced Anomaly Detection")
print("- Hyperparameter Optimization")
print("- Performance Evaluation")
print("- Comprehensive Visualization")

print("\n📚 Files available:")
print("- data_quality_anomaly_detection.ipynb (Jupyter notebook)")
print("- anomalies_detected.csv (Your data)")
print("- cifre.py (Original analysis script)")
print("- 8 PowerPoint slide images (slide1_title.png to slide8_portfolio.png)")

print("\n🚀 You're all set for your PhD presentation!")
