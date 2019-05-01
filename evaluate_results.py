import click
import pandas as pd
from solution import compare_to_solution

@click.command()
@click.option('--result-loc', type=str, default='summarized_data.csv')
def main(result_loc):
    data = pd.read_csv(result_loc)
    acc = compare_to_solution(data)
    print("Labels are %.1f%% accurate" % (acc * 100))

if __name__ == '__main__':
    main()