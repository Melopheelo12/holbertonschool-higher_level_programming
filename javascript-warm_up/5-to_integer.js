#!/usr/bin/node
/**
 * Script that prints a number if the first argument
 *  can be converted to an integer
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */
const number = Number(process.argv[2]);

if (Number.isInteger(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log("Not a number");
}
