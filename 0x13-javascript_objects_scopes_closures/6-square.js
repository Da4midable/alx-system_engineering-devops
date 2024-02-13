#!/usr/bin/node
const fiveSquare = require('./5-square');

class Square extends fiveSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }

        console.log(line);
      }
    }
  }
}

module.exports = Square;
