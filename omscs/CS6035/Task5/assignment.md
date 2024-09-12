# Assignment 3:  Introduction to Machine Learning
This assignment is to provide a quick overview of popular machine learning concepts such as K-Means clustering, Random Forest clusting, XGBoost, and Logarithmic Regression. These will be completed via Python packages and code.

## Task 1: Placeholder
Placeholder

## Task 1: Placeholder
Placeholder

## Task 1: Placeholder
Placeholder

## Task 1: Placeholder
Placeholder

## Task 5: Random Forest Clustering and XGBoost
`train_model_redacted_return_scores`
Your function will:
* Take in the redacted training and test data csv (note: the `class` column is the target for this dataset)
* Train a model
* Predict on a test set (`class` column will be removed to simulate new files that will be classified by your model)
* Output values from `0` to `1` (values close to `0` being less likely to be `class=1` and closer to `1` being more likely to be `class=1`) for each row

Our autograder will compare your predictions with the correct answers, and to get credit, you will need a ROC AUC score of `0.55` to get `1/4` credit and should not require much hyperparameter tuning for this dataset. Thresholds of `0.75` will give half credit and will likely require parameter tuning. The full creddit threshold is `0.76` which will give full credit and likely require parameter tuning.

This is basically a simulation of how your model would perform on unseen data in a production system using batch inference.

Return predicted probabilities for each row of the test sets as a DataFrame with columns `index` (same as your index from the input test DataFrame) and `prob_class_1` (predicted probabilities).

### Inputs
* `train_df_path`: a filepath which contains the lcoation of the redacted training data (same file you are given in the local testing task5 folder). This file will contain the `class` column for you to train your model
* `test_df_path`: a filepath which contains the location of the redacted test data (unseen data used to test the robustness of your model). This file will **not** contain the `class` column

#### Function Skeleton
```python
def train_model_redacted_return_scores(train_df_path, test_df_path) -> pd.Dataframe:
    test_scores = pd.DataFrame()
    return test_scores
```