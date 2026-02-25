# Data Manipulation
import pandas as pd  # for dataframes and CSV handling
import numpy as np   # for numerical operations


# Data Visualization
import matplotlib.pyplot as plt  # plotting
import seaborn as sns            # enhanced visualizations


# Machine Learning
from sklearn.model_selection import train_test_split   # splitting data
from sklearn.linear_model import LogisticRegression   # baseline ML model
from sklearn.ensemble import RandomForestClassifier  # more complex model
from sklearn.metrics import (                       # evaluation metrics
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DATA_PATH = os.path.join(BASE_DIR, "data", "Telco_Cusomer_Churn.csv")


