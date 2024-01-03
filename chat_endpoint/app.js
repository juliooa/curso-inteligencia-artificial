import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "TU_API_KEY",
});

async function chat(message) {
  const completion = await openai.chat.completions.create({
    model: "gpt-4",
    max_tokens: 400,
    temperature: 0.9,
    messages: [
      {
        role: "system",
        content:
          "Eres un robot asistente de muy mal humor, todas tus respuestas son negativas y sarcásticas.",
      },
      {
        role: "assistant",
        content: "Hola en que puedo ayudarte?",
      },
      {
        role: "user",
        content: message,
      },
    ],
  });
  console.log(completion);
  console.log(completion.choices[0].message);
  const prompt_tokens = completion.usage.prompt_tokens;
  const completion_tokens = completion.usage.completion_tokens;

  const prompt_cost = (prompt_tokens * 0.03) / 1000;
  const completion_cost = (completion_tokens * 0.06) / 1000;

  console.log("Costo de prompt: " + prompt_cost + " USD");
  console.log("Costo de completion: " + completion_cost + " USD");
  console.log("Costo total: " + (prompt_cost + completion_cost) + " USD");
  console.log(
    "1 millón de transacciones: " +
      (prompt_cost + completion_cost) * 1000000 +
      " USD"
  );
}

chat("Cómo puedo hacer un pedido?");
