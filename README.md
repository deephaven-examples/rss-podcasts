# rss-podcasts

This app pulls data from a large amount of podcast RSS feeds, and aggregates the data into Deephaven.

By default, this app only reads from 20 RSS feeds. This is only for testing/demo purposes. A separate file containing over 1 million feeds is included for complete usage.

The RSS feeds were initially taken from https://archive.org/download/podcastindex_dump.

## Components

### General

* [`start.sh`](start.sh) - A helper script to launch the application.
* [`docker-compose.yml`](docker-compose.yml) - The Docker compose file that defines the Deephaven images.
* [`Dockerfile`](Dockerfile) - The Dockerfile for the application. Simply extends Deephaven's base image with dependencies and app-mode scripts.
* [`requirements.txt`](requirements.txt) - The Python dependencies for the app.

### Deephaven Application Mode files

* [`read_rss.py`](app.d/read_rss.py) - Python script that defines the base method for the RSS reader.
* [`read_rss_podcasts.py`](app.d/read_rss_podcasts.py) - An RSS reader that pulls from multiple podcast RSS feeds.
* [`app.app`](app.d/app.app) - The Deephaven App Mode config file.

### Python scripts

* [`queries.py`](python-scripts/queries.py) - A query update that aggregates podcasts based on certain criteria.
* [`slack-listener.py`](python-scripts/slack-listener.py) - An example of using a listener to send notifications to a Slack channel.

## High level overview

This app pulls RSS data from many RSS feeds using Python's [feedparser](https://pypi.org/project/feedparser/) package, and aggregates the data into Deephaven. This app is intended to run at scale, pulling from potentially millions of RSS feeds. A threading option is provided (and highly recommended to use) to improve performance.

Custom methods to extract values from the RSS feed, and to extract the date-time value from the RSS feed, need to be written specifically for the RSS feed. Once the data is stored in Deephaven, further queries can be used to analyze the data to figure out information like the most recently published podcasts, what podcast episodes contain certain keywords, and what podcasts produce the most number of episodes in a given period of time.

This app uses podcast RSS feeds by default, but can be customized to any RSS feeds, so feel free to use this app to aggregate any RSS feeds!

## Launch

To launch the app, run

```
sh start.sh
```
