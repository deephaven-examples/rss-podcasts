from deephaven import listen

from slack import WebClient

client = WebClient(token="")

def slack_notification_builder(table, slack_channel):
    def slack_notification(update):
        added_iterator = update.added.iterator()
        while added_iterator.hasNext():
            idx = added_iterator.nextLong()
            podcast_title = table.getColumnSource("RssEntryTitle").get(idx)
            client.chat_postMessage(channel=slack_channel, text=f"Podcast {podcast_title} added")
    return slack_notification

slack_notification = slack_notification_builder(recently_published, "")

handle = listen(recently_published, slack_notification)
