import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "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",
});

async function sendMessage(message) {
  const messages = [
    {
      role: "system",
      content: `
        Eres un asistente de IA que reconoce que funciones podrían ayudar a completar una tarea que
        te piden los usuarios. Existen 3 funciones:
        1. playSong(songName): Reproduce una canción, recibe como parametro el nombre de la canción
        2. stopSong(): Detiene la canción que se está reproduciendo.
        3. sendSong(contactName): Comparte una canción con un contacto, recibe como parametro el nombre del contacto
        Reconoce si alguna de estas funciones podría ayudar a completar la tarea que te piden los usuarios, 
        y responde con la función más los parametros en formato JSON, del tipo:
        {
          functionName: "playSong",
          parameters: "songName"
        }
        Por ejemplo:
        {
          functionName: "playSong",
          parameters: "Despacito"
        }
        Si la función no necesita parámetros, envía un string vacío.
        `,
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
  });

  console.log(completion);
  console.log(JSON.stringify(completion.choices[0].message, null, "\t"));
}

sendMessage(
  "Esta canción es muy buena, por favor envíasela a mi mamá, dile que la escuche con mi papá"
);
