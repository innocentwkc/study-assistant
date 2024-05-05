import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import VueDevTools from "vite-plugin-vue-devtools";

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 4080, // Use port 5000 for the web app frontend
  },
  build: {
    outDir: "dist", // Specify the output directory
  },
  plugins: [
    vue({
      compilerOptions: {
        isCustomElement: (tag) => tag.startsWith("cds-") // catch custon carbon web components
      },
    }),
    VueDevTools(),
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
