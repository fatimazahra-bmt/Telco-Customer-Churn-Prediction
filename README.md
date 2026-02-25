#  Customer Churn Prediction using Machine Learning

## Project Overview

Customer churn is one of the biggest challenges in the telecom industry. 
This project aims to predict whether a customer will leave the company (Churn) using Machine Learning models.

The objective is not only to predict churn, but also to:
- Estimate churn probability
- Segment customers by risk level
- Support business decision-making for retention strategies



##  Dataset

Dataset used: **Telco Customer Churn Dataset**

The dataset includes:
- Customer demographics
- Account information
- Services subscribed
- Monthly and total charges
- Churn (Target variable)

Target variable:
- `Churn` (Yes / No)


##  Data Preprocessing

Steps performed:

- Removed unnecessary columns
- Converted categorical variables using One-Hot Encoding
- Split data into training (80%) and testing (20%)
- Ensured feature consistency between training and prediction



##  Machine Learning Models Used

We tested three classification models:

### 1️) Logistic Regression
- Simple and interpretable
- Works well for binary classification
- Provides clear feature importance

### 2) Random Forest
- Ensemble model
- Handles non-linear relationships
- Reduces overfitting

### 3) Gradient Boosting
- Sequential ensemble model
- Focuses on correcting previous errors
- Often provides high predictive performance

---

## Model Performance (AUC Score)

| Model                | AUC Score |
|----------------------|-----------|
| Logistic Regression  | 0.8339    |
| Random Forest        | 0.8196    |
| Gradient Boosting    | 0.8341    |

###  Why AUC instead of Accuracy?

Accuracy can be misleading when classes are imbalanced.

AUC (Area Under ROC Curve):
- Measures model’s ability to distinguish between churn and non-churn
- Better metric for business risk prediction
- More reliable for classification problems



## Customer Risk Segmentation

After predicting churn probability, customers were segmented into 3 risk levels:

- 🔵 Low Risk → Probability < 0.3
- 🟡 Medium Risk → 0.3 – 0.6
- 🔴 High Risk → > 0.6

Example (Gradient Boosting):

Low Risk: 4437 customers  
Medium Risk: 1692 customers  
High Risk: 903 customers  



##  Business Insights

From feature importance analysis:

- Customers with high monthly charges are more likely to churn
- Short contract customers are at higher risk
- Fiber optic internet users show higher churn tendency
- Long-term customers are more stable


## Business Optimization Strategy

Based on segmentation:

🔴 High Risk Customers:
- Offer discounts
- Provide loyalty programs
- Personalized retention campaigns

🟡 Medium Risk Customers:
- Improve customer service engagement
- Offer contract upgrades

🔵 Low Risk Customers:
- Upselling opportunities
- Cross-selling services


##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn



##  Future Improvements

- Hyperparameter tuning
- Cross-validation
- Feature engineering
- Deep Learning comparison
- Deployment using Streamlit or Flask



## Conclusion

Gradient Boosting slightly outperformed other models in AUC score.
However, Logistic Regression remains highly interpretable and business-friendly.

The project successfully demonstrates how Machine Learning can support customer retention strategies by identifying high-risk customers before they leave.



##  Author

Fatimazahra  
Machine Learning & Data Science Enthusiast