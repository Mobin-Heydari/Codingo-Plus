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
      // Add other theme extensions here
    },
  },
  plugins: [],
} satisfies Config;