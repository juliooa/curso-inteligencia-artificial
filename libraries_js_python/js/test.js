import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "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",
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
