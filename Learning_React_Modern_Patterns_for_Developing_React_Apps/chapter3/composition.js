const template = "hh:mm:ss tt"
const clockTime = template.replace("hh", "03")
  .replace("mm", "33")
  .replace("ss", "33")
  .replace("tt", "PM")

console.log(clockTime)

const both = date => appendAMPM(civilianHours(date));

both(new Date())

const compose = (...fns) => arg => fns.reduce((composed, f) => f(composed), arg);
