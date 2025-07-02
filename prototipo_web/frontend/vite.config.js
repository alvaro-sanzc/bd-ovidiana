import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,         // <–– ESTO HABILITA describe, test, expect
    environment: 'jsdom',  // Simula un navegador
    setupFiles: './setupTests.js' // Opcional si usas jest-dom
  }
});
