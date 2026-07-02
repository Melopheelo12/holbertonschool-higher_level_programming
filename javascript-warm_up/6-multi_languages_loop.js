#!/usr/bin/node

/**
 * Script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You must use a loop (while, for, etc.)
 */

const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let out = '';
for (let i = 0; i < arr.length; i++) {
	out += arr[i] + '\n';
}
out = out.slice(0, -1);
console.log(out);
