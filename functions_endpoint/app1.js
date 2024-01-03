import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "TU_API_KEY",
});

function getCurrentTime() {
  let date = new Date();
  let hours = date.getHours();
  let minutes = date.getMinutes();
  let seconds = date.getSeconds();
  let timeOfDay = "AM";
  if (hours > 12) {
    hours = hours - 12;
    timeOfDay = "PM";
  }
  return hours + ":" + minutes + ":" + seconds + " " + timeOfDay;
}

async function sendMessage(message) {
  const functions = [
    {
      name: "getCurrentTime",
      description: "Get the current time of the day",
      parameters: {
        type: "object",
        properties: {},
      },
    },
  ];

  const messages = [
    {
      role: "system",
      content:
        "Eres un asistente de IA con acceso a funciones en el computador de los usuarios",
    },
    {
      role: "assistant",
      content: message,
    },
  ];

  const completion = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    max_tokens: 200,
    temperature: 0.9,
    messages: messages,
    functions: functions,
  });

  console.log(completion);
  console.log(completion.choices[0].message);

  if (completion.choices[0].message.function_call.name === "getCurrentTime") {
    messages.push(completion.choices[0].message);

    const currentTime = getCurrentTime();
    messages.push({
      role: "function",
      name: "getCurrentTime",
      content: currentTime,
    });
    const completion2 = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      max_tokens: 200,
      temperature: 0.9,
      messages: messages,
      functions: functions,
    });
    console.log(completion2);
    console.log(completion2.choices[0].message);
  }
}

sendMessage("Hola que hora es?");
