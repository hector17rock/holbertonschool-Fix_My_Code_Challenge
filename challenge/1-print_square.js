#!/usr/bin/env node
/**
 * Print a square made of '#' characters
 */

function printSquare(size) {
    if (size <= 0) {
        return;
    }
    
    // FIXED: Using < instead of <= for correct dimensions
    for (let i = 0; i < size; i++) {
        let row = '';
        // FIXED: Using < instead of <= for correct number of characters per row
        for (let j = 0; j < size; j++) {
            row += '#';
        }
        console.log(row);
    }
}

// Get command line argument
const args = process.argv.slice(2);

if (args.length !== 1) {
    console.log('Usage: ./1-print_square.js <size>');
    process.exit(1);
}

const size = parseInt(args[0], 10);

if (isNaN(size)) {
    console.log('Please provide a valid number');
    process.exit(1);
}

if (size <= 0) {
    console.log('Please provide a positive number');
    process.exit(1);
}

printSquare(size);