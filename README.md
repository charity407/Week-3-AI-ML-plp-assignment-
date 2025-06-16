# 🧠 Mastering the AI Toolkit: AI Tools and Applications

## Overview
This repository contains our group assignment for the **AI Tools and Applications** course, under the theme _"Mastering the AI Toolkit"_. The project showcases our theoretical understanding and practical implementation of modern AI tools using TensorFlow, spaCy, and fairness evaluation libraries.

---

## 📁 Project Structure

├── mnist_cnn_notebook.ipynb # CNN for MNIST classification with training/evaluation
├── task_3_spacy.ipynb # spaCy-based rule logic for prediction diagnostics
├── Bias_Analysis_Report.pdf # Final report (bias analysis, fairness, and bug fix summary)
├── video_presentation.mp4 # 3-minute group explanation (not included in repo)
└── README.md # This documentation


---

## 🧪 Assignment Components

### ✅ 1. Theoretical Understanding
- Analysis of bias in CNN image classifiers.
- Concepts like class imbalance, augmentation-induced skew, and confidence bias.
- Grouped digits into **Simple (0, 1, 8)** and **Complex (5, 6, 9)** categories for subgroup fairness.

### 🛠️ 2. Practical Implementation
- Developed a CNN using TensorFlow and Keras to classify MNIST digits.
- Improved model using dropout, max-pooling, and training history plots.
- Implemented TensorFlow Fairness Indicators and custom subgroup metrics.

### ⚖️ 3. Ethics & Optimization
- Applied fairness evaluation techniques despite MNIST lacking explicit sensitive attributes.
- Used spaCy-style rule-based logic to flag ambiguous predictions (e.g., low confidence or common confusions).
- Addressed code bugs:
  - Corrected label encoding (`to_categorical`)
  - Fixed image shape for CNN input
  - Added validation data

---

## 📊 Tools & Frameworks Used

- **Frameworks**: TensorFlow, Keras, spaCy
- **Platforms**: Google Colab, Jupyter Notebook
- **Libraries**: Seaborn, Scikit-learn (confusion matrix), Matplotlib
- **Dataset**: [MNIST](http://yann.lecun.com/exdb/mnist/)

---

## 🎯 Project Highlights

- 🔍 **Bias Detection**: Identified class and confidence imbalances using metrics and visualizations.
- ⚙️ **Model Improvements**: Added dropout layers and architecture tuning for better generalization.
- 📉 **Evaluation**: Used confusion matrix and class-level metrics to avoid misleading accuracy.
- 📜 **Fairness**: Applied TFMA & Fairness Indicators to evaluate model equity across digit groups.
- 🧾 **Rule-Based Filters**: Flagged high-risk predictions post-inference using spaCy-inspired heuristics.

---

## 📽️ Presentation
A 3-minute group video presentation is available on the LMS Community platform, explaining:
- Project goal and methodology
- Model development process
- Bias detection and mitigation
- Ethical considerations

---

## 🧠 Key Learnings

- Practical exposure to TensorFlow-based model training and evaluation
- Hands-on experience with fairness in AI
- Debugging, optimization, and performance tracking
- Teamwork in collaborative AI development

---

## 🚀 How to Run

```bash
# Open notebook and run cells in order:
1. mnist_cnn_notebook.ipynb – Full model pipeline
2. task_3_spacy.ipynb – Rule-based error analysis

📌 Submission Summary

Code: ✅ Fully commented and functional Jupyter Notebooks

Report: ✅ Included as Bias_Analysis_Report.pdf

Video: ✅ Uploaded on LMS

Teamwork: ✅ All members contributed to code, report, and video

🤝 Group Members

    Denis Omwoyo 
