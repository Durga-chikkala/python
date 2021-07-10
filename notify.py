from pynotifier import Notification
def notify(head,matter):
    Notification(title=head,
                 description=matter,
                 duration=20).send()
