import html from 'eslint-plugin-html';

export default [
  {
    files: ["**/*.js", "**/*.html"],
    languageOptions: {
      ecmaVersion: 2020,
      globals: {
        $: "readonly",
        Stripe: "readonly",
      },
    },
    plugins: {
      html,
    },
  },
];