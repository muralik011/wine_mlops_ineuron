import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from get_data import read_params
import sys
import joblib
import json
import argparse

def train_evaluate(config_location):
    params = read_params(config_location=config_location)
    train_path = params['split_data']['train_path']
    test_path = params['split_data']['test_path']
    target_col = [params['base']['target_col']]
    saved_model_path = params['model_dir']
    random_state = params['base']['random_state']
    alpha = params['estimators']['ElasticNet']['params']['alpha']
    l1_ratio = params['estimators']['ElasticNet']['params']['l1_ratio']

    train = pd.read_csv(train_path, sep=',')
    test = pd.read_csv(test_path, sep=',')

    x_train = train.drop(target_col).copy()
    x_test = test.drop(target_col).copy()

    y_train = train[target_col]
    y_test = test[target_col]

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)

    lr.fit(x_train, y_train)

    predicted = lr.predict(x_test)

    def eval_metrics(y_true, y_pred):
        rmse = np.mean(mean_squared_error(y_true=y_true, y_pred=y_pred))
        r2 = r2_score(y_true=y_true, y_pred=y_pred)
        mae = mean_absolute_error(y_true=y_true, y_pred=y_pred)
        return rmse, r2, mae


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', default='params.yaml')
    args = arg_parser.parse_args()
    train_evaluate(config_location=args.config)

