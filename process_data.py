from common.load_data import load_data
from common.params import args

if __name__ == "__main__":
    df = load_data(args.path / 'data/Training/data/KAKAO_898_15.txt')
    print(df)