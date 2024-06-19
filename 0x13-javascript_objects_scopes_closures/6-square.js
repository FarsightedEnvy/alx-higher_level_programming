#!/usr/bin/node

const supSquare = require('./5-square');

class Square extends supSquare {
    charPrint(c) {
        if (c === null || c === undefined) {
            c = 'X';
        }
        for (let i = 0; i < this.height; i++) {
            console.log(c.repeat(this.width));
        }
    }
}

module.exports = Square;
