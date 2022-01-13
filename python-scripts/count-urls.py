from deephaven import Aggregation as agg, as_list

url_counts = podcast_feeds.aggBy(as_list([agg.AggCountDistinct("RssFeedUrl")]), "RssFeedUrl").sumBy()
