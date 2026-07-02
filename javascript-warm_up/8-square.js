#!/usr/bin/node
/**
 * Script that prints a square
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */

const size = parseInt(process.argv[2], 10);
if (Number.isNaN(size)) {
	console.log('Missing size');
} else {
	for (let i = 0; i < size; i++) {
	  let line = '';
		for (let j = 0; j < size; j++) line += 'X';
		  console.log(line);
	}
}
