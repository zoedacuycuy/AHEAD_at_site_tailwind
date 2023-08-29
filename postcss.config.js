module.exports = {
    plugins: [
      require('tailwindcss'),
      require('autoprefixer'),
      process.env.NODE_ENV === 'production'
        ? require('@fullhuman/postcss-purgecss')({
            content: ['./index.html'], // Add your HTML files here
            defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
          })
        : '',
    ],
  };
  