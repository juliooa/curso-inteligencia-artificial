import { textToSpeech } from '$lib/elevenlabs';
import type { RequestHandler } from '@sveltejs/kit';

export const POST = (async ({ request }) => {
	const payload = await request.json();
	const text = payload.text;
	let julio_voice_id = 'SxkRQrhxKwiI5LlJjAvb';
	let response = await textToSpeech(julio_voice_id, text);
	if (response.status === 422) {
		const body = await response.json();
		return new Response(body, {
			headers: {
				'Content-Type': 'application/json'
			},
			status: response.status
		});
	} else if (response.status === 200) {
		return new Response(response.body, {
			headers: {
				'Content-Type': 'audio/mpeg'
			},
			status: 200
		});
	} else {
		const body = await response.json();
		throw new Error(
			'Unexpected response, err:' +
				response.status +
				' ' +
				response.statusText +
				' ' +
				JSON.stringify(body)
		);
	}
}) satisfies RequestHandler;
