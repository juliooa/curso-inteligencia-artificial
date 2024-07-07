from fastapi import FastAPI, HTTPException

from models import (
    Event,
    GetCalendarResponse,
    GetTasksResponse,
    NewTaskPayload,
    SendEmailPayload,
    Task,
)

app = FastAPI(
    title="Asistente Virtual con IA",
    version="0.1.0",
    description="Esta es la documentación de la API del asistente virtual con IA, ayuda a gestionar tareas, eventos de calendario y enviar correos electrónicos.",
    servers=[
        {
            "url": "https://gpt-ai-assistant-phi-snowy.vercel.app",  # Escribe tu servidor             "description": "production",
        }
    ],
)

current_tasks = [
    Task(id="1", name="comprar leche", status="pendiente"),
    Task(id="2", name="ir al banco", status="pendiente"),
    Task(id="3", name="pagar el internet", status="pendiente"),
]

events = [
    Event(name="Reunión de equipo", date="2024-07-10", location="Oficina"),
    Event(name="Cita médica", date="2024-10-11", location="Hospital"),
    Event(name="Cumpleaños de Ana", date="2024-12-12"),
]


# obtener todas las tareas
@app.get("/tasks", description="Obtener todas las tareas", operation_id="get_tasks")
async def query_tasks() -> GetTasksResponse:
    return GetTasksResponse(tasks=current_tasks)


# nueva tarea
@app.post(
    "/tasks",
    description="Crea una nueva tarea, se requiere un nombre y una descripción.",
    operation_id="post_tasks",
)
async def new_task(payload: NewTaskPayload) -> str:
    current_tasks.append(
        Task(id=str(len(current_tasks) + 1), name=payload.name, status="pendiente")
    )
    return "Tarea creada"


# obtener tarea en particular
@app.get(
    "/tasks/{task_id}",
    description="Obtiene la tarea con el id especificado",
    operation_id="get_task_with_id",
)
async def get_task(task_id: str):
    for task in current_tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


# obtener todos los eventos del calendario
@app.get(
    "/calendar",
    description="Obtiene todos los eventos del calendario",
    operation_id="get_calendar_events",
)
async def query_calendar_events() -> GetCalendarResponse:
    return GetCalendarResponse(events=events)


# nuevo evento en el calendario
@app.post(
    "/calendar",
    description="Crea un nuevo evento en el calendario",
    operation_id="post_calendar_event",
)
async def new_calendar_event(payload: Event):
    events.append(payload)
    return "Evento creado"


# enviar email
@app.post("/email", description="Envía un email", operation_id="send_email")
async def send_email(payload: SendEmailPayload) -> str:
    # TODO llamar a la función de envío de email
    # mailgun.send_email(payload.to, payload.subject, payload.body)
    return "Email enviado a " + payload.to


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
