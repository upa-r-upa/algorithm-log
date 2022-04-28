const readline = require("readline");

const stream = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

stream.on("line", function (line) {
  const inputNumberList = line.split(" ").map((str) => parseInt(str, 10));
  stream.close();
  console.log(inputNumberList[0] + inputNumberList[1]);
  process.exit();
});
