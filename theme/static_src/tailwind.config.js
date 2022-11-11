const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: [
    "../templates/**/*.html",
    "../../templates/**/*.html",
    "../../**/templates/**/*.html",
    "../../levensfilosofie/settings.py",
  ],
  theme: {
    extend: {
      colors: {
        "limed-spruce": "#3d5155",
        "bison-hide": "#c2c1a9",
        pewter: "#92af9e",
        gumbo: "#759fa7",
        "gumbo-dark": "#588791",
        sundance: {
          DEFAULT: "#d0b95a",
          900: "#d5c06b",
          800: "#d9c77b",
          700: "#dece8c",
          600: "#e3d59c",
          500: "#e8dcad",
          400: "#ece3bd",
          300: "#f1eace",
          200: "#f6f1de",
          150: "#f8f5e6",
          100: "#faf8ef",
          50: "#fdfcf7",
        },
      },
      fontFamily: {
        sans: ["Raleway", ...defaultTheme.fontFamily.sans],
        heading: ["Soria", ...defaultTheme.fontFamily.serif],
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
