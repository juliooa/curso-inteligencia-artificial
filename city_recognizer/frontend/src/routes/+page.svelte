<script lang="ts">
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import { FileDropzone, ProgressBar } from '@skeletonlabs/skeleton';
	let files: FileList;
	let processing = false;
	let imageUrl: string;
	let answer: string;

	async function startProcessing(event: Event) {
		processing = true;
		const form = event.target as HTMLFormElement;
		const formData = new FormData(form);
		const response = await fetch(`${PUBLIC_BACKEND_URL}/query`, {
			method: 'POST',
			body: formData
		});
		processing = false;
		let result = await response.json();
		if (result.error) {
			answer = result.error;
		} else {
			answer = result.answer;
		}
	}

	async function onAddedPhoto(input: Event) {
		const target = input.target as HTMLInputElement;
		if (target != null) {
			const file = target.files?.[0];
			if (file && file.type.startsWith('image/')) {
				imageUrl = URL.createObjectURL(file);
			}
		}
	}
</script>

<div class="flex items-center justify-center p-4">
	<div class="card m-11 h-full w-3/4">
		<div class="p-4 md:p-10">
			<h1 class="text-xl">Reconocedor de ciudades</h1>
			<h3 class="mt-6">Sube tu foto:</h3>
			<form method="POST" on:submit|preventDefault={startProcessing} class="w-full">
				<FileDropzone name="photo" bind:files on:change={onAddedPhoto} />
				{#if imageUrl}
					<div class="flex flex-col items-center justify-center">
						<div>
							<img class="preview max-w-96" src={imageUrl} alt="preview" />
						</div>
						<button class="btn variant-filled-secondary btn-lg mt-4 w-2/4">¿Qué ciudad es?</button>
					</div>
				{/if}
			</form>
			{#if answer}
				<div class="mt-4">
					<p>{answer}</p>
				</div>
			{/if}
			{#if processing}
				<div class="p-8">
					<p>Building...</p>
					<ProgressBar height="h-3" meter="bg-warning-500" />
				</div>
			{/if}
		</div>
	</div>
</div>
