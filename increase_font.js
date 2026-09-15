const fs = require('fs');

let content = fs.readFileSync('src/pages/index.astro', 'utf8');

// Replace rem values
content = content.replace(/font-size:\s*([0-9.]+)rem;/g, (match, p1) => {
  const newSize = parseFloat(p1) + 0.125;
  return `font-size: ${newSize}rem;`;
});

// Replace px values
content = content.replace(/font-size:\s*([0-9.]+)px;/g, (match, p1) => {
  const newSize = parseFloat(p1) + 2;
  return `font-size: ${newSize}px;`;
});

fs.writeFileSync('src/pages/index.astro', content);
console.log("Updated font sizes in index.astro");
