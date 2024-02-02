import { getCompletion, type Message } from '$lib/openai';
import { error, json, type RequestHandler } from '@sveltejs/kit';

export const POST = (async ({ request }) => {
	const payload = await request.json();
	const message = payload.userMessage;
	let openaiKey = payload.openaiKey;
	if (!openaiKey) {
		openaiKey = process.env.OPENAI_KEY;
	}
	if (!openaiKey) {
		throw error(400, 'no openai key provided');
	}

	const systemPrompt = `
    Tu eres un traductor de español a inglés.
    El usuario te va a mandar un mensaje, y tu lo vas a traducir.
    Además, vas a listar todas las palabras de tu traducción e indicar su significado en español.
    Finalmente vas a agregar 2 otras formas de decir lo mismo en inglés.
    Usa el siguiente formato para tu respuesta:
    Traducción: <tu traducción>
    Palabras:
     - <palabra 1>: <significado 1>
     - <palabra 2>: <significado 2>
    También puedes decirlo así:
     - <otra forma de decirlo 1>
     - <otra forma de decirlo 2>
    `;

	const messages = [
		{
			content: systemPrompt,
			role: 'system'
		},
		{
			content: message,
			role: 'user'
		}
	] satisfies Message[];

	const response = await getCompletion(messages, openaiKey);

	return json({ reply: response });
}) satisfies RequestHandler;
