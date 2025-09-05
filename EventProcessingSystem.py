import collections
import time
import threading
import uuid


class Event:
    def __init__(self, payload):
        self.id = str(uuid.uuid4())
        self.payload = payload
        self.timestamp = time.time()

    def __repr__(self):
        return f"<Event id={self.id} payload={self.payload}>"


class EventQueue:
    def __init__(self):
        self.queue = collections.deque()
        self.cancelled = set()
        self.condition = threading.Condition()

    def add_event(self, payload):
        ev = Event(payload)
        with self.condition:
            self.queue.append(ev)
            self.condition.notify()  # wake up any waiting processor
        return ev.id

    def process_next(self):
        with self.condition:
            # wait until queue has something
            while not self.queue:
                self.condition.wait()

            while self.queue:
                ev = self.queue.popleft()
                if ev.id in self.cancelled:
                    self.cancelled.remove(ev.id)
                    continue  # skip cancelled
                self._process(ev)
                return ev
            return None  # if only cancelled events were there

    def _process(self, ev):
        print(f"Processing event {ev.id} with payload {ev.payload}")

    def pending_events(self):
        with self.condition:
            return [ev for ev in self.queue if ev.id not in self.cancelled]

    def cancel_event(self, event_id):
        with self.condition:
            # remove directly from queue
            self.queue = collections.deque([ev for ev in self.queue if ev.id != event_id])
            self.cancelled.discard(event_id)

    def process_all(self):
        processed = []
        while True:
            try:
                ev = self.process_next()
                if not ev:
                    break
                processed.append(ev)
            except Exception:
                break
        return processed


# Example usage
if __name__ == "__main__":
    eq = EventQueue()

    id1 = eq.add_event({"type": "A"})
    id2 = eq.add_event({"type": "B"})
    print("Pending:", eq.pending_events())

    eq.cancel_event(id1)

    processed = eq.process_next()
    print("Processed:", processed)

    print("Pending after:", eq.pending_events())
