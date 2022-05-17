from get_data import read_params, get_data
import argparse


def load_data(config_location):
    df = get_data(config_location)
    df.columns = [col.replace(' ', '_') for col in df.columns]
    raw_data_location = read_params(config_location)['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_location, sep=',', index=False)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', default='params.yaml')
    args = arg_parser.parse_args()
    load_data(config_location=args.config)
