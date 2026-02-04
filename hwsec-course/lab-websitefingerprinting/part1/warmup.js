const runs = 10;

function measureOneLine() {
  const LINE_SIZE = 16; // 128/sizeof(double) Note that js treats all numbers as double
  let result = [];

  // Fill with -1 to ensure allocation
  const M = new Array(runs * LINE_SIZE).fill(-1);

  for (let i = 0; i < runs; i++) {
    const start = performance.now();
    let val = M[i * LINE_SIZE];
    const end = performance.now();

    result.push(end - start);
  }

  return result;
}

function measureNLines() {
  let result = [];

  // Exercise 1-1: measure access time for N cache lines (10 runs per N)
  const Ns = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000];
  const LINE_BYTES = 64;
  let sink = 0;

  for (const N of Ns) {
    let arr;
    try {
      arr = new Uint8Array(N * LINE_BYTES);
    } catch (e) {
      result.push(`N=${N}: N/A`);
      continue;
    }
    const measurements = [];

    for (let r = 0; r < runs; r++) {
      const start = performance.now();
      for (let off = 0; off < arr.length; off += LINE_BYTES) {
        sink ^= arr[off];
      }
      const end = performance.now();
      measurements.push(end - start);
    }

    result.push(`N=${N}: [${measurements.join(", ")}]`);
  }

  if (sink === 123) console.log("sink", sink);

  return result;
}

document.getElementById(
  "exercise1-values"
).innerText = `1 Cache Line: [${measureOneLine().join(", ")}]`;

document.getElementById(
  "exercise2-values"
).innerText = `N Cache Lines: [${measureNLines().join(", ")}]`;
