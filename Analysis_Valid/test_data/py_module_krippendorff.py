#

"""
Examples
    --------
    >>> reliability_data = [[np.nan, np.nan, np.nan, np.nan, np.nan, 3, 4, 1, 2, 1, 1, 3, 3, np.nan, 3],
    ...                     [1, np.nan, 2, 1, 3, 3, 4, 3, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    ...                     [np.nan, np.nan, 2, 1, 3, 4, 4, np.nan, 2, 1, 1, 3, 3, np.nan, 4]]
    >>> print(round(alpha(reliability_data=reliability_data, level_of_measurement='nominal'), 6))
    0.691358
    >>> print(round(alpha(reliability_data=reliability_data, level_of_measurement='interval'), 6))
    0.810845
    >>> value_counts = np.array([[1, 0, 0, 0],
    ...                          [0, 0, 0, 0],
    ...                          [0, 2, 0, 0],
    ...                          [2, 0, 0, 0],
    ...                          [0, 0, 2, 0],
    ...                          [0, 0, 2, 1],
    ...                          [0, 0, 0, 3],
    ...                          [1, 0, 1, 0],
    ...                          [0, 2, 0, 0],
    ...                          [2, 0, 0, 0],
    ...                          [2, 0, 0, 0],
    ...                          [0, 0, 2, 0],
    ...                          [0, 0, 2, 0],
    ...                          [0, 0, 0, 0],
    ...                          [0, 0, 1, 1]])
    >>> print(round(alpha(value_counts=value_counts, level_of_measurement='nominal'), 6))
    0.691358
    >>> # The following examples were extracted from
    >>> # https://www.statisticshowto.datasciencecentral.com/wp-content/uploads/2016/07/fulltext.pdf, page 8.
    >>> reliability_data = [[1, 2, 3, 3, 2, 1, 4, 1, 2, np.nan, np.nan, np.nan],
    ...                     [1, 2, 3, 3, 2, 2, 4, 1, 2, 5, np.nan, 3.],
    ...                     [np.nan, 3, 3, 3, 2, 3, 4, 2, 2, 5, 1, np.nan],
    ...                     [1, 2, 3, 3, 2, 4, 4, 1, 2, 5, 1, np.nan]]
    >>> print(round(alpha(reliability_data, level_of_measurement='ordinal'), 3))
    0.815
    >>> print(round(alpha(reliability_data, level_of_measurement='ratio'), 3))
    0.797
    """

import numpy as np

reliability_data = [
    [np.nan, np.nan, np.nan, np.nan, np.nan, 3, 4, 1, 2, 1, 1, 3, 3, np.nan, 3],
    [1, np.nan, 2, 1, 3, 3, 4, 3, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [np.nan, np.nan, 2, 1, 3, 4, 4, np.nan, 2, 1, 1, 3, 3, np.nan, 4]
    ]
reliability_data_2 = [
    [1, 2, 3, 3, 2, 1, 4, 1, 2, np.nan, np.nan, np.nan],
    [1, 2, 3, 3, 2, 2, 4, 1, 2, 5, np.nan, 3.],
    [np.nan, 3, 3, 3, 2, 3, 4, 2, 2, 5, 1, np.nan],
    [1, 2, 3, 3, 2, 4, 4, 1, 2, 5, 1, np.nan]
]


value_counts = np.array( [ 
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 2, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 2, 1],
    [0, 0, 0, 3],
    [1, 0, 1, 0],
    [0, 2, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 1]
    ]
)

#



