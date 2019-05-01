"""
The main file for this project. Consumes the raw data and produces an output file
called "summarized_data.csv" containing the combined labels for the 
*first 10 columns only*
"""
import pandas as pd

ID_COL = ['Input.attr_id']
ADJ_COLS = ['Input.adj_' + str(i) for i in range(1, 11)]
ANS_COLS = ['Answer.adj_' + str(i) for i in range(1, 11)]

def summarize_labels_baseline(data):
    """
    Baseline approach. Predicts the label by plurality vote of all the labelers.
    """
    cols = ID_COL + ADJ_COLS + ANS_COLS
    answers = [ # Group all of the entries that have a particular q/a combo
                data[cols].groupby(ID_COL + [ADJ_COLS[i]])[ANS_COLS[i]]
                .apply(list)
                .reset_index()
                # Rename so that we have consistent naming for each answer
                .rename(index=str, columns={'Input.attr_id': 'attr_id',
                                            ADJ_COLS[i]: 'adj', 
                                            ANS_COLS[i]: 'label'})
                for i in range(len(ADJ_COLS))
                ]
    # Comine all of the answer-groupings into a single dataframe
    # Result is a dataframe where each row is a question-adjective pair, 
    # and there's a column called 'label' that right now contains a list of 
    # all of the labelers answers
    answers = pd.concat(answers, ignore_index=True)
    # We want to produce a single value for label. Say that the label is True
    # if at least half of labelers think it's true.
    answers['label'] = answers['label'].apply(lambda x: x.count('Yes') > len(x)/2)
    return answers

def summarize_labels(data):
    """
    Your code goes here
    """
    return answers


def main():

    data = pd.read_csv('raw_data.csv')

    # Once you have written your code, comment out this line
    result = summarize_labels_baseline(data)

    # Once you have written your code, uncomment this line
    #result = summarize_labels(data)

    # Save result
    output = pd.DataFrame(result, columns=['attr_id', 'adj', 'label'])
    output = output.sort_values(by=['attr_id', 'adj', 'label'])
    output.to_csv('summarized_data.csv', index=False)

if __name__ == '__main__':
    main()