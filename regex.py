import argparse
import match

def main():
  parser = argparse.ArgumentParser(description='Matching string against regular expression.')
  parser.add_argument('regex', type=str, help='A regular expression')
  parser.add_argument('filename', type=str, help='A file name containing strings')

  args = parser.parse_args()
  exec(args.regex, args.filename)

def exec(regex, filename):
  f = open(filename, "r")

  for line in f:
    print(line.strip())
    print(match.match(regex, line.strip()))
    print()

if __name__ == '__main__':
    main()