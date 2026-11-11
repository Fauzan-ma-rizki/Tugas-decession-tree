import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import warnings

warnings.filterwarnings('ignore')

# Load data
try:
    df = pd.read_excel('student_lifestyle_dataset.xlsx')
except FileNotFoundError:
    print("File 'student_lifestyle_dataset.xlsx' tidak ditemukan.")
    exit()

if 'Student_ID' in df.columns:
    df = df.drop(columns=['Student_ID'])

# Split data: 10 baris pertama untuk train, baris ke-11 untuk test
train_data = df.iloc[:10]
X_train = train_data.drop(columns=['Stress_Level'])
y_train = train_data['Stress_Level']

test_data = df.iloc[10:11]
X_test = test_data.drop(columns=['Stress_Level'])
y_test = test_data['Stress_Level'].values[0]

# Setup & train model
rf = RandomForestClassifier(n_estimators=5, max_features=1, max_depth=1, random_state=42)
rf.fit(X_train, y_train)

# Prediksi
pred = rf.predict(X_test)

# Print hasil
print("\n--- Hasil Prediksi Data Uji ---")
for col in X_test.columns:
    print(f"{col}: {X_test.iloc[0][col]}")

print(f"\nTarget Aktual : {y_test}")
print(f"Prediksi      : {pred[0]}")

# Visualisasi pohon
plt.figure(figsize=(20, 5))
for i, tree in enumerate(rf.estimators_):
    plt.subplot(1, 5, i+1)
    plot_tree(tree, 
              feature_names=list(X_train.columns), 
              class_names=list(map(str, rf.classes_)), 
              filled=True, 
              rounded=True, 
              fontsize=9)
    plt.title(f'Tree {i+1}')

plt.tight_layout()
plt.show()