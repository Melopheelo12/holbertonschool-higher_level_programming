#!/usr/bin/node
/**
 * Script that prints "C is fun" x times where x is the first argument
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */

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
