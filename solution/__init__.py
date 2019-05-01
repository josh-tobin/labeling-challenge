import pandas as pd
import os
import numpy as np

SOLN_LOC = os.path.join(os.path.dirname(__file__),
                        'ground_truth.csv')

def compare_to_solution(data):
    soln = pd.read_csv(SOLN_LOC)
    n = len(soln)
    c = np.sum(soln['label'] == data[:n]['label'])
    return c / n