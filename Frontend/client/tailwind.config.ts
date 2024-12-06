import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#FFD700",
        secondary: "#0056B3",
        background: "#F8F9FA",
        text: "#333333",
        hover: "#0056B3",
        success: "#218838",
      },
      
      boxShadow: {
        'custom-light': '0 4px 6px rgba(189, 188, 184, 0.1)', // Light shadow with RGB
        'custom-dark': '0 4px 6px rgba(189, 188, 184, 0.5)', // Dark shadow with RGB
      },
    },
  },
  plugins: [],
} satisfies Config;