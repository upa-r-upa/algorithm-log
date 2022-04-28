const readline = require("readline");

const stream = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputNumberList = [];

stream
  .on("line", function (line) {
    inputNumberList = line.split(" ").map((str) => parseInt(str, 10));
    stream.close();
  })
  .on("close", function () {
    const added = inputNumberList.reduce((prev, curr) => {
      return prev + curr;
    }, 0);

    console.log(added);
    process.exit();
  });
