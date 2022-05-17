from get_data import read_params
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(config_location):
    params = read_params(config_location=config_location)
    train_path = params['split_data']['train_path']
    test_path = params['split_data']['test_path']
    test_size = params['split_data']['test_size']
    random_state = params['base']['random_state']
    raw_data = pd.read_csv(params['load_data']['raw_dataset_csv'], sep=',')
    train, test = train_test_split(raw_data, test_size=test_size, random_state=random_state)
    train.to_csv(train_path, index=False, sep=',')
    test.to_csv(test_path, index=False, sep=',')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', default='params.yaml')
    args = arg_parser.parse_args()
    split_data(config_location=args.config)
