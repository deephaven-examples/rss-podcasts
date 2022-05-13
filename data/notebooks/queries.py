from deephaven import agg
from deephaven.time import now, to_nanos

url_counts = podcast_feeds.agg_by([agg.count_distinct(cols=["RssFeedUrl"])], by=["RssFeedUrl"]).sum_by()

author = podcast_feeds.where(filters=["Author = `Mike Kendall`"])
tech_keywords = podcast_feeds.where(filters=["RssEntryTitle.contains(`Software`) || RssEntryTitle.contains(`Technology`) || RssEntryTitle.contains(`Computer`) || RssEntryTitle.contains(`Science`)"])

one_day = to_nanos("24:00:00")
recently_published = podcast_feeds.where(filters=["PublishDatetime >= (DateTime)now() - one_day"])

long_podcasts = podcast_feeds.where(filters=["Duration > 3600"])
