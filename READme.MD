I have used Django rest_framework to explain the behaviors

Custom_class.py is the class that was asked to create.

Answer 1: By default, Django signals execute synchronously. In my code, I have called the signal post_save and have put a time.sleep() for 2 seconds to explain the behavior.

It waits for every task to complete before sending the response, i.e when the post_save signal is triggered, the main thread waits for the completion of the post_save signal due to which it first prints the line in the post_save signal and then waits for 2 seconds, and then sends the response.
If it had been running asynchronously then it would have just triggered the post_save signal wouldn't have waited for 2 seconds for the signal to complete its execution and would have sent the response just after triggering the post_save signal. 


Answer2: As mentioned in the above answer, it is executed in the same thread, this behavior is possible by default only in case it is executed in the same thread, if it would have been in different threads then to implement this behavior we would have to add an extra line for thread.join to mention the main thread to wait until the other thread completes its execution.
