<script lang="ts">
	let message = '';
	let replyMessage = '';
	let openaiKey = '';

	async function sendMessage() {
		const reply = await fetch('/api/messages', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ userMessage: message, openaiKey })
		});
		const data = await reply.json();
		console.log(data);
		replyMessage = data.reply;
	}
</script>

<div class="container">
	<h1>Bienvenido a clases de Inglés</h1>

	<h3>¿Que quieres traducir hoy?</h3>
	<input class="input_question" type="text" bind:value={message} placeholder="Escribe aquí" />
	<button on:click={sendMessage}>Enviar</button>

	<pre>{replyMessage}</pre>

	<div style="text-align: left; flex">
		<span style="font-size: small;">OpenAI Key:</span>
		<input class="input_apikey" type="text" bind:value={openaiKey} placeholder="sk-..." />
	</div>
</div>

<style>
	:global(body) {
		height: 100%;
		margin: 0;
		padding: 0;
		font-family: 'Arial', sans-serif; /* Change font to a more modern one */
	}
	.container {
		width: 50%; /* Adjust width as needed */
		margin: 50px auto 0; /* Center the container horizontally and add a 50px margin from the top */
		padding: 20px;
		border: 2px solid #ccc; /* Add border */
		box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Add shadow */
		text-align: center; /* Center align text */
	}

	.input_question {
		padding: 10px;
		margin: 10px 0;
		width: 70%; /* Adjust width as needed */
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box; /* Include padding and border in element's total width and height */
	}

	.input_apikey {
		padding: 10px;
		margin: 10px 0;
		width: 30%;
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box; /* Include padding and border in element's total width and height */
	}

	button {
		padding: 10px 20px;
		background-color: #007bff; /* Blue color */
		color: white;
		border: none;
		border-radius: 5px;
		cursor: pointer;
		transition: background-color 0.3s ease; /* Smooth transition */
	}

	button:hover {
		background-color: #0056b3; /* Darker blue color on hover */
	}

	pre {
		background-color: #f9f9f9;
		padding: 10px;
		border-radius: 5px;
		text-align: left;
		overflow-x: auto;
	}
</style>
