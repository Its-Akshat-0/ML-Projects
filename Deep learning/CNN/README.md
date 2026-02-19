# Image Classification - Real World Object Detection (Fashion MNIST)

## Problem Statement
The goal of this project is to build a Convolutional Neural Network (CNN) to classify images into one of 10 fashion categories using the **Fashion MNIST** dataset.

## Dataset
**Fashion-MNIST Test Dataset (Provided)**
- **Source**: `fashion-mnist_test.csv`
- **Total Samples**: 10,000 images
- **Format**: CSV file where each row is a sample. The first column is the label, and the remaining 784 columns are pixel values (28x28 grayscale).
- **Classes**:
  0. T-shirt/top
  1. Trouser
  2. Pullover
  3. Dress
  4. Coat
  5. Sandal
  6. Shirt
  7. Sneaker
  8. Bag
  9. Ankle boot

Since only the test dataset file was provided, we will split this 10,000-sample dataset into:
- **Training Set**: 8,000 samples (80%)
- **Test Set**: 2,000 samples (20%)

## Project Structure
- `Image_Classification_CNN.ipynb`: The main Jupyter Notebook containing the entire pipeline.
- `fashion-mnist_test.csv`: The provided dataset.
- `README.md`: Project documentation.
- `requirement.txt`: List of dependencies.

## Requirements
To run this notebook, you need the following libraries installed:
- `tensorflow`
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

You can install them using pip:
```bash
pip install tensorflow numpy pandas matplotlib seaborn scikit-learn
```

## Tasks Implemented
1. **Data Preprocessing**: 
   - Loading data from CSV.
   - Reshaping flat vectors (784) into 2D images (28x28x1).
   - Normalization of pixel values.
   - Splitting into Train/Test sets.
2. **CNN Architecture**: A custom CNN with Convolutional, Pooling, and Fully Connected layers.
3. **Training & Evaluation**: Training the model and plotting Accuracy/Loss curves.
4. **Visualization**:
   - Visualizing Feature Maps.
   - Analyzing Misclassified Images.
5. **Model Improvement**:
   - **Dropout**: To prevent overfitting.
   - **Data Augmentation**: Random rotations and zooms to improve generalization.

## Results
The notebook demonstrates the effectiveness of CNNs on the Fashion MNIST dataset, even with a smaller subset of training data.
