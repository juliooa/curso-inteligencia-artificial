import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "TU_API_KEY",
});

async function main() {
  const response = await openai.completions.create({
    model: "gpt-3.5-turbo-instruct",
    prompt: "Saluda a los estudiantes del curso de IA",
    max_tokens: 100,
    temperature: 0.9,
  });
  console.log(response);
}

main();
