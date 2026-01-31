// Number of sweep counts
// Exercise 2-1: choose an appropriate window size (ms)
let P = 5;

// Number of elements in your trace
let K = 5 * 1000 / P;

// Array of length K with your trace's values
let T;

// Value of performance.now() when you started recording your trace
let start;

function record(traceLengthMs) {
  // Create empty array for saving trace values
  T = new Array(K);

  // Fill array with -1 so we can be sure memory is allocated
  T.fill(-1, 0, T.length);

  // Save start timestamp
  start = performance.now();

  // Exercise 2-1: sweep-counting for traceLengthMs
  const LINE_BYTES = 64;
  const BUF_BYTES = 32 * 1024 * 1024;
  const buf = new Uint8Array(BUF_BYTES);
  let sink = 0;

  for (let off = 0; off < buf.length; off += LINE_BYTES) sink ^= buf[off];

  for (let i = 0; i < K; i++) {
    const windowStart = performance.now();
    let sweeps = 0;

    while (performance.now() - windowStart < P) {
      for (let off = 0; off < buf.length; off += LINE_BYTES) {
        sink ^= buf[off];
      }
      sweeps++;
    }

    T[i] = sweeps;
  }

  if (sink === 123) postMessage(JSON.stringify({ sink }));

  // Once done recording, send result to main thread
  postMessage(JSON.stringify(T));
}

// DO NOT MODIFY BELOW THIS LINE -- PROVIDED BY COURSE STAFF
self.onmessage = (e) => {
  if (e.data.type === "start") {
    const traceLengthMs = e.data.trace_length ?? 5000;
    K = Math.floor(traceLengthMs / P);
    setTimeout(() => record(traceLengthMs), 0);
  }
};
