#!/usr/bin/node
const xArg = process.argv[2];
const n = parseInt(xArg, 10);
if (Number.isNaN(n)) {
	console.log('Missing number of occurrences');
} else {
	let out = '';
	for (let i = 0; i < n; i++) {
		out += 'C is fun';
		if (i !== n - 1) out += '\n';
	}
	if (out) console.log(out);
}
