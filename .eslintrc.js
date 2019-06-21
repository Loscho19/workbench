module.exports = {
  env: {
    browser: true,
    es6: true,
    jquery: true,
  },
  extends: "eslint:recommended",
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: "module",
  },
  plugins: ["prettier"],
  rules: {
    indent: ["error", 2],
    "linebreak-style": ["error", "unix"],
    quotes: ["error", "double"],
    semi: ["error", "always"],
    "no-unused-vars": ["error", {argsIgnorePattern: "^_|event"}],
    "prettier/prettier": "error",
    quotes: 0,
  },
}
