from deephaven.table_listener import listen

from slack import WebClient

import os

SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN")
SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL")

client = WebClient(token=SLACK_API_TOKEN)

def slack_notification_builder(table, slack_channel, text):
    def slack_notification(update):
        added_iterator = update.added.iterator()
        while added_iterator.hasNext():
            idx = added_iterator.nextLong()
            podcast_title = table.j_object.getColumnSource("RssEntryTitle").get(idx)
            client.chat_postMessage(channel=slack_channel, text=text.format(podcast_title=podcast_title))
    return slack_notification

slack_notification_recently_published = slack_notification_builder(recently_published, SLACK_CHANNEL, "Podcast {podcast_title} found in recently_published table")
recently_published_handler = listen(recently_published, slack_notification_recently_published)

slack_notification_tech_keywords = slack_notification_builder(tech_keywords, SLACK_CHANNEL, "Podcast {podcast_title} found in tech_keywords table")
tech_keywords_handler = listen(tech_keywords, slack_notification_tech_keywords)
