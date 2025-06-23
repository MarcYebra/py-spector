import sys
from pyspector.analyzer import analyze_file
from pyspector.report import print_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.py>")
        sys.exit(1)

    filepath = sys.argv[1]
    results = analyze_file(filepath)
    print_report(results)

if __name__ == "__main__":
    main()
