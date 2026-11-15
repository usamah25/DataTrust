<script setup lang="ts">
const apiBase = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api/v1";
</script>

<template>
  <main class="min-h-screen bg-[#f7f9f8] text-[#26332e]">
    <header class="border-b border-[#e5ebe8] bg-white">
      <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        <div class="flex items-center gap-3">
          <div class="grid h-9 w-9 place-items-center rounded-xl bg-[#16866b] text-lg font-bold text-white">D</div>
          <div>
            <p class="text-lg font-semibold tracking-tight">DataTrust</p>
            <p class="text-xs text-[#697771]">From Raw Data to Meaningful Insights</p>
          </div>
        </div>
        <span class="rounded-full bg-[#e8f4ef] px-3 py-1 text-xs font-medium text-[#11745b]">MVP workspace</span>
      </div>
    </header>
    <section class="mx-auto max-w-7xl px-6 py-16">
      <div class="max-w-2xl">
        <p class="mb-3 text-sm font-semibold uppercase tracking-[0.16em] text-[#16866b]">Workspace foundation</p>
        <h1 class="text-4xl font-semibold tracking-tight sm:text-5xl">Your data, clear and trustworthy.</h1>
        <p class="mt-5 max-w-xl text-base leading-7 text-[#697771]">
          The DataTrust development environment is running. The next vertical slice will add CSV import,
          data profiling, the workspace grid, recipe-based editing, and version publishing.
        </p>
        <div class="mt-8 rounded-2xl border border-[#e5ebe8] bg-white p-5 shadow-sm">
          <p class="text-sm font-semibold">Development API</p>
          <code class="mt-2 block rounded-lg bg-[#f7f9f8] px-3 py-2 text-sm text-[#3978d5]">{{ apiBase }}</code>
          <p class="mt-3 text-sm text-[#697771]">API health endpoint: <a class="font-medium text-[#16866b] underline" href="http://localhost:8000/api/v1/health" target="_blank">Check API</a></p>
        </div>
      </div>
    </section>
  </main>
</template>
