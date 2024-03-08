<script lang="ts">
	import { page } from '$app/stores';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import { ProgressBar } from '@skeletonlabs/skeleton';
	let chatbot_id = $page.params.chatbot_id;
	let asking = false;
	let query = '';
	let answer = '';

	async function queryLLM() {
		asking = true;
		const response = await fetch(`${PUBLIC_BACKEND_URL}/ask_chatbot/${chatbot_id}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				question: query
			})
		});
		asking = false;
		let result = await response.json();
		answer = result.answer;
	}
</script>

<div class="flex justify-center p-4 w-full">
	<div class="flex-col p-4 w-3/4">
		<div class="card mb-8">
			<div class="p-4 md:p-10">
				<h1 class="text-xl">Chat with your PDF 📕 - Bot #{chatbot_id}</h1>
				<div class="flex">
					<input
						class="input text-xl p-4"
						type="text"
						placeholder="your question here"
						bind:value={query}
					/>
					<button
						type="button"
						class="btn variant-filled-secondary w-1/5 ml-4 text-xl"
						on:click={queryLLM}>Ask</button
					>
				</div>
				{#if asking}
					<div class="mt-6">
						<p>Asking...</p>
						<ProgressBar height="h-3" meter="bg-warning-500" />
					</div>
				{/if}
			</div>
		</div>
		{#if answer.length > 0}
			<div class="card mb-8">
				<div class="p-4">
					<h3 class="text-xxl mb-2">Answer</h3>
					<div class="flex flex-col rounded-[16px] bg-tertiary-500 p-4">
						<p style="white-space: pre-line;">{answer}</p>
					</div>
				</div>
			</div>
		{/if}
	</div>
</div>
