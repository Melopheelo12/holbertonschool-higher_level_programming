#!/usr/bin/node
/**
 * Script that prints 3 lines:
 * (like 1-multi_languages.js)
 */

const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let out = '';
for (let i = 0; i < arr.length; i++) {
	out += arr[i] + '\n';
}
out = out.slice(0, -1);
console.log(out);
