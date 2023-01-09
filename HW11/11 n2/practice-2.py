import argparse
parser = argparse.ArgumentParser("Getting a list of garde and return its average.")
parser.add_argument("-g", "--grade",dest="grades", help="list of grades", type=float, action="append")
parser.add_argument("-f", "--float", dest="float", help="precision", type=int, default="2")
args = parser.parse_args()
avg = sum(args.grades)/len(args.grades)
print(round(avg, args.float))