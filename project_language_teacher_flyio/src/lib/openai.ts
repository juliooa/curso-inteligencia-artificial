import OpenAI from 'openai';
import { env as secret } from '$env/dynamic/private';

export type Message = {
	content: string;
	role: 'system' | 'user' | 'assistant';
};

export async function getCompletion(messages: Message[], openaiKey: string) {
	const openai = new OpenAI({
		apiKey: openaiKey
	});

	console.log(messages);
	const response = await openai.chat.completions.create({
		model: 'gpt-3.5-turbo',
		messages,
		max_tokens: 150,
		temperature: 0.9
	});
	//TODO manejar errores

	console.log(response);
	return response.choices[0].message.content;
}
