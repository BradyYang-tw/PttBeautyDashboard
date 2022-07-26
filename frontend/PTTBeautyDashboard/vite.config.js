import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      // string shorthand
      // '/getData': 'http://localhost:5000/getData',
      // with options
      '/getAllImage': {
        target: 'http://localhost:5000/getAllImage',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/getAllImage/, '')
      },
      '/getImageByID': {
        target: 'http://localhost:5000/getImageByID',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/getImageByID/, '')
      },
      // with RegEx
      '^/fallback/.*': {
        target: 'http://jsonplaceholder.typicode.com',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/fallback/, '')
      },
      
    }}
})
