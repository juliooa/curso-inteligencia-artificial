import { env as secret } from '$env/dynamic/private';
const elevenLabsApi = 'https://api.elevenlabs.io/v1';

export async function textToSpeech(voiceId: string, text: string) {
	const modelId = 'eleven_multilingual_v2';
	const url = `${elevenLabsApi}/text-to-speech/${voiceId}`;

	let response = await fetch(url, {
		method: 'POST',
		headers: {
			Accept: 'audio/mpeg',
			'Content-Type': 'application/json',
			'xi-api-key': secret.SECRET_ELEVENLABS_APIKEY
		},
		body: JSON.stringify({
			model_id: modelId,
			text: text
		})
	});
	return response;
}
