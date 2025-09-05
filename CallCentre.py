from collections import deque

class CallCenterQueue:
    def __init__(self):
        self.queue = deque()

    def addcall(self, customerid, calltime):
        # Adds a new call to the queue
        self.queue.append((customerid, calltime))
        print(f"Call from customer {customerid} at {calltime} added to the queue.")

    def answercall(self):
        # Answers and removes the first call from the queue
        if not self.QueueEmpty():
            customerid, calltime = self.queue.popleft()
            print(f"Call from customer {customerid} at {calltime} answered and removed from the queue.")
        else:
            print("No calls in the queue to answer.")

    def viewqueue(self):
        # Views all calls in the queue without removing them
        if self.QueueEmpty():
            print("No calls in the queue.")
        else:
            print("Current queue:")
            for customerid, calltime in self.queue:
                print(f"Customer ID: {customerid}, Call Time: {calltime}")

    def QueueEmpty(self):
        # Checks if the queue is empty
        return len(self.queue) == 0


# Example usage
call_center = CallCenterQueue()

# Add some calls to the queue
call_center.addcall(101, "10:01 AM")
call_center.addcall(102, "10:02 AM")
call_center.addcall(103, "10:03 AM")

# View the queue
call_center.viewqueue()

# Answer a call
call_center.answercall()

# View the queue after answering one call
call_center.viewqueue()

# Answer the remaining calls
call_center.answercall()
call_center.answercall()

# Check if the queue is empty
print("Is queue empty?", call_center.QueueEmpty())
