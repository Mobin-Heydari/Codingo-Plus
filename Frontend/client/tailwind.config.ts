import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],

  screens: {
    'sm': '640px',
    // => @media (min-width: 640px) { ... }

    'md': '768',
    // => @media (min-width: 768) { ... }

    'lg': '1024px',
    // => @media (min-width: 1024px) { ... }

    'xl': '1280px',
    // => @media (min-width: 1280px) { ... }

    '2xl': '1536px',
    // => @media (min-width: 1536px) { ... }
  },

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