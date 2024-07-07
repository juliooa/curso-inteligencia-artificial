from pydantic import BaseModel


class Event(BaseModel):
    name: str
    date: str
    location: str | None = None
    description: str | None = None


class GetCalendarResponse(BaseModel):
    events: list[Event]


class NewTaskPayload(BaseModel):
    name: str
    description: str


class Task(BaseModel):
    id: str
    name: str
    status: str


class GetTasksResponse(BaseModel):
    tasks: list[Task]


class SendEmailPayload(BaseModel):
    to: str
    subject: str
    body: str
