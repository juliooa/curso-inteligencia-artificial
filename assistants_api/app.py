"""
AI Personal Assistant using Assistants API
"""
import time
from openai import Client

client = Client(api_key="TU_APIKEY")


def load_file(file_path):
    """
    Loading a file in open ai
    """
    return client.files.create(
        file=open(
            file_path,
            "rb",
        ),
        purpose="assistants",
    )


def create_assistant():
    """
    Creates an assistant
    """
    contacts_file = load_file("files/contacts.json")
    sales_file = load_file("files/sales.csv")

    assistant = client.beta.assistants.create(
        name="Mi asistente personal",
        model="gpt-3.5-turbo-1106",
        instructions="""You are Julio's AI personal assistant,
        you need to fulfill tasks and assist him in whatever he wants""",
        tools=[{"type": "retrieval"}, {"type": "code_interpreter"}],
        file_ids=[contacts_file.id, sales_file.id],
    )
    return assistant


def create_thread():
    """
    Creates a new Thread
    """
    thread = client.beta.threads.create()
    print("Thread created, id: ", thread.id)
    return thread


def add_messages(thread_id, content):
    """
    Adds a message to a thread
    """
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content,
    )
    return message


def run_thread(assistant_id, thread_id):
    """
    Executes a run
    """
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    return run


def wait_on_run(run, thread):
    """
    Waits until run reaches an end state
    """
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(1)
        print("Waiting for run to complete...")


def get_messages(thread_id):
    """
    Returns all the messages from a thread
    """
    return client.beta.threads.messages.list(
        thread_id=thread_id,
    )


def main():
    """
    The main function
    """
    assistant = create_assistant()
    thread = create_thread()

    while True:
        user_input = input("> ")

        if user_input.lower() == "/exit":
            print("Exiting the application.")
            break

        message = add_messages(thread.id, user_input)
        run = run_thread(
            assistant_id=assistant.id,
            thread_id=thread.id,
        )
        wait_on_run(run, thread)
        messages = get_messages(thread_id=thread.id)
        last_message = messages.data[0]
        print(last_message.content[0])

main()
