import yaml
import argparse
import pandas as pd


def read_params(config_location):
    with open(config_location, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_location):
    config = read_params(config_location)
    data_loc = config["data_source"]["s3_source"]
    df = pd.read_csv(data_loc)
    return df


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', default='params.yaml')
    args = arg_parser.parse_args()
    # print(args.config)
    data = get_data(config_location=args.config)
