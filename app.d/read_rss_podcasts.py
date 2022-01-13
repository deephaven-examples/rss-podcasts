"""
read_rss_podcasts.py

An RSS reader that reads from multiple podcast URLs.

This file is meant to run through Deephaven's Application Mode as part of several Python scripts. Because of this, some
variables may not be defined in here, but instead in helper_functions.py or read_rss.py.
"""
import json

def rss_attributes_method_podcasts(entry):
    return (entry["title"], rss_datetime_converter_podcasts(entry), entry["title_detail"]["base"],
            json.dumps(entry))

def rss_datetime_converter_podcasts(entry):
    try:
        dt = parser.parse(entry["published"])
        dts = dt.strftime("%Y-%m-%dT%H:%M:%S") + " UTC"
        return convertDateTime(dts)
    except:
        return currentTime()

podcast_feed_urls = []
with open("/app.d/podcast-list.txt") as f:
    for line in f:
        podcast_feed_urls.append(line.rstrip())

column_names = [
    "RssEntryTitle",
    "PublishDatetime",
    "RssFeedUrl",
    "JsonObject",
]
column_types = [
    dht.string,
    dht.datetime,
    dht.string,
    dht.string,
]

podcast_feeds = read_rss_continual(podcast_feed_urls, sleep_time=300, rss_attributes_method=rss_attributes_method_podcasts,
                                   rss_datetime_converter=rss_datetime_converter_podcasts, column_names=column_names,
                                   column_types=column_types, thread_count=10)
