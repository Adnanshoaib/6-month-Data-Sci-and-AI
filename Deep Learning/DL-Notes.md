# What is Deep Learning :-
Deep Learning (DL) is a subset of Machine Learning (ML) that uses Artificial Neural Networks (ANNs) with multiple hidden layers to learn complex patterns from data.

- Inspired by the human brain’s neurons and synapses.
- Works best with large datasets and high computational power.
- Core idea: Forward Propagation (make predictions) + Backward Propagation (learn from errors).

# Difference Between AI, ML, and DL :-

- Artificial Intelligence (AI): Broad field of creating intelligent machines.
- Machine Learning (ML): AI subset that learns from data.
- Deep Learning (DL): ML subset using multi-layered neural networks.

# Basic Workflow of Deep Learning

- Input Data → Images, Text, Audio, or Numerical data.
- Forward Propagation → Data flows through layers, prediction is made.
- Loss Calculation → Compare prediction with actual value.
- Backward Propagation (Backprop) → Error sent backwards to update weights.
- Optimization → Use algorithms like Gradient Descent & Adam Optimizer.
- Repeat (Epochs) until the model converges.

# Key Concepts in Deep Learning
Neuron: Basic unit, takes input, applies weight + bias, passes through activation function.

- Layer Types :-
  - Input Layer: Raw data enters.
  - Hidden Layers: Learn patterns.
  - Output Layer: Gives prediction.
- Activation Functions:
  - Sigmoid, Tanh, ReLU, Softmax.
- Loss Functions:
  - Cross-Entropy, MSE (Mean Squared Error).
- Optimization:
  - Gradient Descent, Adam, RMSprop.

# Types of Neural Networks in Deep Learning

Neural Networks come in many different architectures, each designed to solve a specific type of problem.

- Artificial Neural Network (ANN) :-
  - The most basic type of neural network.
  - Consists of Input Layer → Hidden Layers → Output Layer.
  - Data flows only in one direction (Forward Propagation).
  - Commonly used for tabular/structured data.
    - Applications :-  Customer churn prediction, fraud detection, credit scoring.

- Convolutional Neural Network (CNN) :-
  - Specialized for images and videos.
  - Uses convolutional layers to extract spatial features (edges, shapes, textures).
  - Architecture: Convolution → ReLU → Pooling → Fully Connected Layers.
    -  Applications :- Image classification, object detection, self-driving cars, face recognition.
   
- Recurrent Neural Network (RNN) :-
  - Designed for sequential data (time-series, text, speech).
  - Maintains memory of previous inputs to influence future outputs.
  - Suffers from the Vanishing Gradient Problem → solved by LSTM and GRU.
    -  Applications :- Stock price prediction, text generation, speech recognition.
