import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Average of Numbers')
    parser.add_argument('-g', '--grades', action='append', dest='values', default=[],
                        help='Add repeated values to a list')
    parser.add_argument('-f', '--float', action='store', dest='float', default=2, help='Number of fractional part')
    args = parser.parse_args()
    sum = 0
    for i in range(len(args.values)):
        sum += float(args.values[i])
    avg = sum / len(args.values)
    result = round(avg, int(args.float))
    print(f'average is : {result}')
