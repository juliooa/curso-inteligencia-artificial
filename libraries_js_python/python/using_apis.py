import openai

openai.api_key = "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"
completion = openai.Completion.create(
    model="text-davinci-003",
    prompt="Saluda a los estudiantes del curso de IA",
    max_tokens=100,
    temperature=1
)

print(completion)
