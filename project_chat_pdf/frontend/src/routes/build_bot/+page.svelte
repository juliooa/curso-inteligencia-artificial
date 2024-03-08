<script lang="ts">
	import { goto } from '$app/navigation';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import { FileDropzone, ProgressBar } from '@skeletonlabs/skeleton';
	let files: FileList;
	let processing = false;

	async function startProcessing(event: Event) {
		processing = true;
		const form = event.target as HTMLFormElement;
		const formData = new FormData(form);
		const response = await fetch(`${PUBLIC_BACKEND_URL}/build_chatbot`, {
			method: 'POST',
			body: formData
		});
		processing = false;
		let result = await response.json();
		if (result) {
			goto('/ask_bot/' + result.chatbot_id);
		}
	}
</script>

<div class="flex justify-center items-center p-4">
	<div class="m-11 card h-full w-3/4">
		<div class="p-4 md:p-10">
			<h1 class="text-xl">Chat with your PDF 📕</h1>
			<h3 class="mt-6">Upload your file:</h3>
			<form method="POST" on:submit|preventDefault={startProcessing} class="w-full">
				<FileDropzone name="file" bind:files />
				{#if files}
					<ol class="list w-full mt-3">
						{#each Array.from(files) as document, i}
							<li>
								<span class="badge-icon p-4 variant-soft-primary">{i + 1}</span>
								<span class="text-xl">{document.name}</span>
							</li>
						{/each}
					</ol>
					<div class="justify-center items-center flex flex-col">
						<button class="w-2/4 btn variant-filled-secondary btn-lg mt-4"> Build Bot </button>
					</div>
				{/if}
			</form>
			{#if processing}
				<div class="p-8">
					<p>Building...</p>
					<ProgressBar height="h-3" meter="bg-warning-500" />
				</div>
			{/if}
		</div>
	</div>
</div>
