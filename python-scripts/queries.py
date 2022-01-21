from deephaven import Aggregation as agg, as_list
from deephaven.DateTimeUtils import currentTime, convertPeriod

url_counts = podcast_feeds.aggBy(as_list([agg.AggCountDistinct("RssFeedUrl")]), "RssFeedUrl").sumBy()

author = podcast_feeds.where("Author = `Mike Kendall`")
christian_keywords = podcast_feeds.where("RssEntryTitle.contains(`God`) || RssEntryTitle.contains(`Christ`) || RssEntryTitle.contains(`Spirit`)")

one_day = convertPeriod("1D")
recently_published = podcast_feeds.where("PublishDatetime >= currentTime() - one_day")

long_podcasts = podcast_feeds.where("Duration > 3600")
