import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# 1. Load Data
try:
    df = pd.read_csv('Students Performance Dataset.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset not found.")
    exit()

# 2. Data Preprocessing
# Drop irrelevant columns
drop_cols = ['Student_ID', 'First_Name', 'Last_Name', 'Email']
df = df.drop(columns=drop_cols)

# Handle Missing Values
# Impute categorical columns with mode
categorical_cols_all = df.select_dtypes(include=['object']).columns
for col in categorical_cols_all:
    if df[col].isnull().sum() > 0:
        print(f"Imputing missing values for {col} with mode.")
        df[col] = df[col].fillna(df[col].mode()[0])

# Impute numerical columns with mean (if any)
numerical_cols_all = df.select_dtypes(include=['number']).columns
for col in numerical_cols_all:
    if df[col].isnull().sum() > 0:
        print(f"Imputing missing values for {col} with mean.")
        df[col] = df[col].fillna(df[col].mean())

# Separate Features and Target
# We predict 'Grade'. We drop 'Total_Score' and 'Final_Score' to avoid data leakage 
# (assuming Grade is derived directly from them).
# Leaving 'Midterm_Score', 'Assignments_Avg', etc. as they are ongoing assessments.
X = df.drop(columns=['Grade', 'Total_Score', 'Final_Score'])
y = df['Grade']

# Encode Categorical Features
categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=['number']).columns

# Use LabelEncoder for categorical features for simplicity in this demo, 
# or OneHotEncoder for better performance with non-ordinal data.
# For ANN, OneHotEncoder is generally preferred for nominal data.
# However, to keep dimensionality manageable for a small dataset, we'll use LabelEncoder for binary/ordinal 
# and OneHot for others if cardinality is low. 
# Let's use get_dummies (One-Hot) for all categorical inputs.
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

# Encode Target (Grade)
le = LabelEncoder()
y = le.fit_transform(y)
num_classes = len(np.unique(y))

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale Numerical Features
scaler = StandardScaler()
# Fit on training data only to avoid leakage
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(f"Training Data Shape: {X_train.shape}")
print(f"Test Data Shape: {X_test.shape}")

# 3. Build ANN Model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2), # Regularization
    Dense(32, activation='relu'),
    Dropout(0.1), # Regularization
    Dense(num_classes, activation='softmax')
])

# 4. Compile Model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# 5. Train Model
history = model.fit(X_train, y_train, 
                    epochs=50, 
                    batch_size=32, 
                    validation_split=0.2, 
                    verbose=1)

# 6. Evaluate Model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTest Accuracy: {accuracy*100:.2f}%")

# 7. Plot Training Curves
plt.figure(figsize=(12, 5))

# Accuracy Plot
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Loss Plot
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.savefig('training_curves.png')
print("Training curves saved as 'training_curves.png'")

# 8. Confusion Matrix
y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('confusion_matrix.png')
print("Confusion matrix saved as 'confusion_matrix.png'")

# Print Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Save Model Architecture Plot (requires pydot/graphviz, skipping if not available)
try:
    from tensorflow.keras.utils import plot_model
    plot_model(model, to_file='model_architecture.png', show_shapes=True, show_layer_names=True)
    print("Model architecture saved as 'model_architecture.png'")
except Exception as e:
    print(f"Could not save model architecture plot: {e}")
