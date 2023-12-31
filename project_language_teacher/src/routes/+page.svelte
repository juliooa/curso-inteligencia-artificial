<script lang="ts">
	let message = '';
	let replyMessage = '';

	async function sendMessage() {
		const reply = await fetch('/api/messages', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ userMessage: message })
		});
		const data = await reply.json();
		console.log(data);
		replyMessage = data.reply;
	}
</script>

<h1>Bienvenido a clases de Inglés</h1>

<h3>¿Que quieres traducir hoy?</h3>
<input type="text" bind:value={message} placeholder="Escribe aquí" />
<button on:click={sendMessage}>Enviar</button>

<pre>{replyMessage}</pre>
