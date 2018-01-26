import os
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TARGET_PATH = os.path.join(DIR_PATH, 'dont_use.csv')
TEST_TARGETS = pd.read_csv(TARGET_PATH).set_index(['user_id', 'joke_id'])


def score_top_5_percent(predictions):
    """
    For each user, this scoring metric will select the 5% of jokes
    predicted to be most highly rated by that user. It then looks
    at the actual ratings (in the test data) that the user gave
    those jokes. Your score is the average of those ratings.

    Use this metric when reporting the score of your joke recommender.
    """
    joined = predictions.join(TEST_TARGETS,
                              on=['user_id', 'joke_id'],
                              rsuffix='_target')
    if joined.shape[0] != TEST_TARGETS.shape[0] != predictions.shape[0]:
        raise Exception('The predictions cannot join 1:1 with the test ' \
                        'set targets. Check your predictions output file.')
    g = joined.groupby('user_id')
    top_5 = g.rating.transform(
        lambda x: x >= x.quantile(.95)
    )
    return joined.rating_target[top_5==1].mean()


def score_rmse(predictions):
    """
    Computes the root mean squared error of ALL the predicted joke ratings.
    This metric is in stark contrast to the `score_top_5_percent` metric.
    This metric (RMSE) punishes every prediction which deviates from the
    target value, whereas the `score_top_5_percent` metric only cares that
    the top-rated jokes be identified as such for each user.

    Use this metric only for your own curiosity. Don't report this metric.
    """
    joined = predictions.join(TEST_TARGETS,
                              on=['user_id', 'joke_id'],
                              rsuffix='_target')
    if joined.shape[0] != TEST_TARGETS.shape[0] != predictions.shape[0]:
        raise Exception('The predictions cannot join 1:1 with the test ' \
                        'set targets. Check your predictions output file.')
    return np.sqrt(mean_squared_error(joined.rating_target, joined.rating))


if __name__ == '__main__':

    import sys

    if len(sys.argv) != 2:
        print 'Usage: python {} <prediction_csv_file_path>'
        sys.exit()

    predictions = pd.read_csv(sys.argv[1])
    print score_top_5_percent(predictions)
