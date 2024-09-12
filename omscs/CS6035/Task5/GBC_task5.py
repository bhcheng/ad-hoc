from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd


def train_model_redacted_return_scores(train_df_path, test_df_path) -> pd.DataFrame:
    train_data = pd.read_csv(train_df_path)

    # GradientBoostingClassifier source: https://stackoverflow.com/questions/54709600/gradientboostingclassifier-implementation
    predictors = train_data.drop(['class'], axis = 1)
    target = train_data['class']
    x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size = 0.2, random_state = 42)

    gbc = GradientBoostingClassifier()
    gbc.fit(x_train, y_train)



if __name__ == '__main__':
    file_name = 'redacted_train.csv'
    train_model_redacted_return_scores(file_name, file_name)