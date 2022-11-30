## 명령행 인자

import argparse

def print_test(args):
    print(args.epoch)
    print(args.batch_size)
    print(args.lr_initial)
    print(args.name)

def argparser():
    example_text = '''example:
      python argparser1.py --epoch 200 --batch_size 128 --name "My Test" 
      '''

    # 인자값을 받을 수 있는 인스턴스 생성
    parser = argparse.ArgumentParser(description='Argparse Tutorial',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    # 입력받을 인자값 설정 (default 값 설정가능)
    parser.add_argument('--epoch', type=int, default=150)
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--lr_initial', type=float, default=0.1)
    parser.add_argument('--name', type=str, default="None")

    # args 에 위의 내용 저장
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = argparser()
    print_test(args)