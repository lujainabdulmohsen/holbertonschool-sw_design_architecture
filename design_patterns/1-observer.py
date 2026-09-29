#!/usr/bin/env python3
"""Observer design pattern example."""


class NewsSubject:
    """Manage and notify news subscribers."""

    def __init__(self):
        """Initialize the subscriber list."""
        self._subscribers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to selected topics."""
        self._subscribers.append((observer, topics))

    def unsubscribe(self, observer):
        """Unsubscribe an observer."""
        self._subscribers = [
            subscription
            for subscription in self._subscribers
            if subscription[0] is not observer
        ]

    def notify(self, topic, data):
        """Notify subscribed observers."""
        for observer, topics in list(self._subscribers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Log news events."""

    def update(self, topic, data):
        """Print a log notification."""
        print(f"log:{topic}={data}")


class EmailObserver:
    """Email news events."""

    def update(self, topic, data):
        """Print an email notification."""
        print(f"email:{topic}={data}")


class SmsObserver:
    """Send SMS news events."""

    def update(self, topic, data):
        """Print an SMS notification."""
        print(f"sms:{topic}={data}")


def main():
    """Run the observer example."""
    subject = NewsSubject()

    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    subject.subscribe(
        log_observer,
        topics={"sports", "breaking"}
    )
    subject.subscribe(email_observer)
    subject.subscribe(
        sms_observer,
        topics={"breaking"}
    )

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
