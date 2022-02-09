import pandas as pd
pd.set_option('max_rows', 5)
import numpy as np
reviews = pd.read_csv("winemag-data-130k-v2.csv")

print(reviews.points.describe())
print(reviews.taster_name.describe())
print(reviews.points.mean())
print(reviews.taster_name.unique())

# Maps

review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

def remean_points(row):
    row.points = row.points - review_points_mean
    return row


reviews.apply(remean_points, axis='columns')

print(reviews.head(1))
