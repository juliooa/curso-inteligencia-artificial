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

function playSong(songName) {
  console.log("Playing song: " + songName);
  return "true";
}

async function sendMessage(message) {
  console.log(message);
  const functions = [
    {
      name: "getCurrentTime",
      description: "Get the current time of the day",
      parameters: {
        type: "object",
        properties: {},
      },
    },
    {
      name: "playSong",
      description: "Play a song",
      parameters: {
        type: "object",
        properties: {
          songName: {
            type: "string",
          },
        },
      },
    },
  ];

  const messages = [
    {
      role: "system",
      content:
        "Eres un asistente que reconoce la mejor función para cumplir tareas para el usuario",
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
    functions,
  });
  console.log(completion.choices[0].message);

  if (completion.choices[0].finish_reason === "function_call") {
    messages.push(completion.choices[0].message);

    switch (completion.choices[0].message.function_call.name) {
      case "getCurrentTime":
        const currentTime = getCurrentTime();
        messages.push({
          role: "function",
          content: currentTime,
          name: "getCurrentTime",
        });
        break;
      case "playSong":
        const funcArguments =
          completion.choices[0].message.function_call.arguments;
        const songName = JSON.parse(funcArguments).songName;
        const songPlaying = playSong(songName);
        messages.push({
          role: "function",
          content: songPlaying,
          name: "playSong",
        });
        break;
      default:
        break;
    }

    const completion2 = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      max_tokens: 200,
      temperature: 0.9,
      messages: messages,
      functions,
    });

    console.log(completion2.choices[0].message);
  }
}

sendMessage("Por favor quiero escuchar Let it be de Los Beatles");
