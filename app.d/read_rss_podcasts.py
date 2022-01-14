"""
read_rss_podcasts.py

An RSS reader that reads from multiple podcast URLs.

This file is meant to run through Deephaven's Application Mode as part of several Python scripts. Because of this, some
variables may not be defined in here, but instead in helper_functions.py or read_rss.py.
"""
import json

def duration_conversion(strn):
    #This is assuming the duration will be either MM:SS, HH:MM:SS, or just a number of seconds
    if ":" in strn:
        values = strn.split(":")
        if len(values) == 3: #HH:MM:SS
            [hours, minutes, seconds] = values
            return (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
        elif len(values) == 2: #MM:SS
            [minutes, seconds] = values
            return (int(minutes) * 60) + int(seconds)
        else: #Unknown format
            return None
    elif len(strn) > 0:
        return int(strn)
    else:
        return None

def rss_attributes_method_podcasts(entry):
    author = None
    duration = None
    if "author" in entry.keys():
        author = entry["author"]
    if "itunes_duration" in entry.keys():
        duration = duration_conversion(entry["itunes_duration"])
    return (entry["title"], entry["link"], duration, author,
            rss_datetime_converter_podcasts(entry), entry["title_detail"]["base"],
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
    "RssEntryLink",
    "Duration",
    "Author",
    "PublishDatetime",
    "RssFeedUrl",
    "JsonObject",
]
column_types = [
    dht.string,
    dht.string,
    dht.int_,
    dht.string,
    dht.datetime,
    dht.string,
    dht.string,
]

podcast_feeds = read_rss_continual(podcast_feed_urls, sleep_time=300, rss_attributes_method=rss_attributes_method_podcasts,
                                   rss_datetime_converter=rss_datetime_converter_podcasts, column_names=column_names,
                                   column_types=column_types, thread_count=10)
