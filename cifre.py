# -*- coding: utf-8 -*-
"""
Data Quality Anomaly Detection in Mobility Systems
Detections anomalies in trip data, speed, GPS coordinates, and missing/inconsistent data

Détection d'anomalies dans la qualité des données des systèmes de mobilité
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns


# ==================== Veri Simülasyonu / Simulation des données ====================
np.random.seed(42)
n_samples = 500

# Trip duration (dk) / durée trajet (min)
trip_duration = np.random.normal(loc=30, scale=5, size=n_samples)
# Bazı anomaliler ekle / Ajouter des anomalies
trip_duration[[10, 50, 200]] = [120, 1, 90]

# Speed (km/h) / vitesse (km/h)
speed = np.random.normal(loc=40, scale=8, size=n_samples)
speed[[20, 70, 300]] = [200, 0, -10]

# GPS coordinates / coordonnées GPS
latitude = np.random.normal(loc=48.8566, scale=0.01, size=n_samples) # Paris approx
longitude = np.random.normal(loc=2.3522, scale=0.01, size=n_samples)
latitude[[5, 100]] = [50.0, 10.0]
longitude[[5, 100]] = [5.0, 100.0]

# Missing and inconsistent data / données manquantes et incohérentes
trip_duration[[15, 80]] = np.nan
speed[[25]] = np.nan

# Create DataFrame / Création du DataFrame
data = pd.DataFrame({
    'trip_duration_min': trip_duration,
    'speed_kmh': speed,
    'latitude': latitude,
    'longitude': longitude
})

# ==================== Anomali Tespiti / Détection des anomalies ====================

# Z-score method / Méthode Z-score
from scipy import stats
z_scores = np.abs(stats.zscore(data[['trip_duration_min', 'speed_kmh']].fillna(0)))
z_anomalies = (z_scores > 3).any(axis=1)

# IQR method / Méthode IQR
Q1 = data[['trip_duration_min', 'speed_kmh']].quantile(0.25)
Q3 = data[['trip_duration_min', 'speed_kmh']].quantile(0.75)
IQR = Q3 - Q1
iqr_anomalies = ((data[['trip_duration_min', 'speed_kmh']] < (Q1 - 1.5 * IQR)) | 
                 (data[['trip_duration_min', 'speed_kmh']] > (Q3 + 1.5 * IQR))).any(axis=1)

# Isolation Forest / Forêt d'isolation
clf = IsolationForest(random_state=42)
clf.fit(data[['trip_duration_min', 'speed_kmh']].fillna(0))
iso_pred = clf.predict(data[['trip_duration_min', 'speed_kmh']].fillna(0))
iso_anomalies = iso_pred == -1

# Combine anomalies / Combiner les anomalies
data['anomaly_zscore'] = z_anomalies
data['anomaly_iqr'] = iqr_anomalies
data['anomaly_isolation'] = iso_anomalies

# ==================== Sonuçların Görselleştirilmesi / Visualisation ====================

# Trip Duration Plot / Graphique durée trajet
plt.figure(figsize=(10,4))
sns.scatterplot(x=data.index, y='trip_duration_min', hue='anomaly_isolation', palette={True:'red', False:'blue'}, data=data)
plt.title('Seyahat Süresi Anomalileri / Anomalies de durée de trajet')
plt.xlabel('Index')
plt.ylabel('Trip Duration (min) / Durée trajet (min)')
plt.legend(title='Anomaly / Anomalie')
plt.show()

# Speed Plot / Graphique vitesse
plt.figure(figsize=(10,4))
sns.scatterplot(x=data.index, y='speed_kmh', hue='anomaly_isolation', palette={True:'red', False:'blue'}, data=data)
plt.title('Hız Anomalileri / Anomalies de vitesse')
plt.xlabel('Index')
plt.ylabel('Speed (km/h) / Vitesse (km/h)')
plt.legend(title='Anomaly / Anomalie')
plt.show()

# GPS Plot / Graphique GPS
plt.figure(figsize=(6,6))
sns.scatterplot(x='longitude', y='latitude', hue='anomaly_isolation', palette={True:'red', False:'blue'}, data=data)
plt.title('GPS Anomalileri / Anomalies GPS')
plt.xlabel('Longitude / Longitude')
plt.ylabel('Latitude / Latitude')
plt.legend(title='Anomaly / Anomalie')
plt.show()

# ==================== CSV Raporu ====================
data.to_csv('anomalies_detected.csv', index=False, encoding='utf-8-sig')
print("Rapor kaydedildi: anomalies_detected.csv / Rapport sauvegardé")
