#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number' || !Number.isInteger(w) || !Number.isInteger(h)) {
			return `${Rectangle.name} {}`;
		} else {
			this.width = w;
			this.height = h;
		}
	}


 print() {
	if (!this.width || !this.height) {
      console.log(`${Rectangle.name} {}`);
    } else {
		for (let i = 0; i < this.height; i++) {
			let line = '';
			for (let j = 0; j < this.width; j++) {
				line += 'X';
			}

			console.log(line);
			
		}
	}
}
}

module.exports = Rectangle;


