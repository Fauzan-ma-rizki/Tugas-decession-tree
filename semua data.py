import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree
import warnings

warnings.filterwarnings('ignore')


df = pd.read_excel('student_lifestyle_dataset.xlsx')


if 'Student_ID' in df.columns:
    df = df.drop(columns=['Student_ID'])

# Split features & target
X = df.drop(columns=['Stress_Level'])
y = df['Stress_Level']

# Train-test split (80:20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Train model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Prediksi & evaluasi
y_pred = rf.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("HASIL EVALUASI MODEL RANDOM FOREST")
print(f"Data Latih (Train) : {len(X_train)} baris")
print(f"Data Uji (Test)    : {len(X_test)} baris")
print(f"Akurasi            : {acc * 100:.2f}%")
print("\nCatatan:")
print("- Akurasi menunjukkan persentase ketepatan model dalam menebak target.")
print("- Classification Report di bawah merincikan seberapa baik model menebak tiap level stres.\n")

print("--- Classification Report ---")
print(classification_report(y_test, y_pred))

# Visualisasi pohon keputusan dari model Random Forest
plt.figure(figsize=(15, 6))

for i in range(10):
    plt.subplot(2, 5, i+1) 
    plot_tree(rf.estimators_[i], 
              feature_names=list(X.columns), 
              class_names=list(map(str, rf.classes_)), 
              filled=True, 
              rounded=True, 
              max_depth=3, 
              fontsize=5)
    plt.title(f'Tree {i+1}', fontsize=9)

plt.tight_layout()
plt.show()
