#!/usr/bin/node
// Write a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
  // Instance method that prints the rectangle using the charactere 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
  // Instance method that exchanges the width and the height of the rectangle}
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Instance method that multiples the width and the height
    // of the rectangle by 2
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
