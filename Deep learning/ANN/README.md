# Student Performance Prediction Using ANN

This project predicts student academic performance (Grade) based on lifestyle and academic factors using an Artificial Neural Network (Feedforward MLP) implemented in TensorFlow/Keras.

## Project Structure
- `student_performance_ann.py`: Main Python script for data preprocessing, model training, evaluation, and plotting.
- `student_performance_ann.ipynb`: Jupyter Notebook version of the analysis.
- `Students Performance Dataset.csv`: The dataset file.
- `README.md`: This file.
- `training_curves.png`: Training loss and accuracy plots (generated).
- `confusion_matrix.png`: Confusion matrix visualization (generated).
- `model_architecture.png`: Visualization of the ANN architecture (generated if Graphviz is installed).

## Requirements
- Python 3.x
- TensorFlow
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pydot & Graphviz (optional, for model plotting)

## How to Run
1. Install dependencies:
   ```bash
   pip install tensorflow pandas numpy matplotlib seaborn scikit-learn pydot graphviz
   ```
2. Run the script:
   ```bash
   python student_performance_ann.py
   ```
3. Check the generated PNG files for visualizations and the console output for accuracy metrics.

## Model Architecture
The model is a Feedforward Neural Network (MLP) built with Keras.

```mermaid
graph TD
    Input[Input Layer (22 Features)] --> Hidden1[Dense Layer (64 neurons, ReLU)]
    Hidden1 --> Dropout1[Dropout (0.2)]
    Dropout1 --> Hidden2[Dense Layer (32 neurons, ReLU)]
    Hidden2 --> Dropout2[Dropout (0.1)]
    Dropout2 --> Output[Output Layer (5 neurons, Softmax)]
```

### Layer Details
1. **Input Layer**: Accepts 22 features (after one-hot encoding).
2. **Hidden Layer 1**: 64 neurons, ReLU activation function.
3. **Dropout Layer 1**: 20% dropout rate to prevent overfitting.
4. **Hidden Layer 2**: 32 neurons, ReLU activation function.
5. **Dropout Layer 2**: 10% dropout rate.
6. **Output Layer**: 5 neurons (corresponding to grades A, B, C, D, F), Softmax activation.

## Results & Analysis

### Performance
- **Test Accuracy**: ~60%
- **Loss**: ~0.80

### Classification Report
The dataset (and consequently the model) shows some class imbalance, particularly for grades 'A' and 'F'.

| Grade | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| A     | 0.00      | 0.00   | 0.00     | 5       |
| B     | 0.48      | 0.43   | 0.45     | 134     |
| C     | 0.60      | 0.69   | 0.64     | 450     |
| D     | 0.64      | 0.62   | 0.63     | 358     |
| F     | 0.55      | 0.21   | 0.30     | 53      |

*Note: Grades 'C' and 'D' have the highest support (number of samples) and thus the model performs best on them. 'A' has extremely low representation.*

### Files Generated
- **training_curves.png**: Visualizes the training/validation loss and accuracy over epochs.
- **confusion_matrix.png**: Heatmap showing predicted vs actual grades.

