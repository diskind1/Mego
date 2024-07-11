"use strict";
let a;
let b;
let c;
let d;
let e;
let arr = ["", "or", "2"];
let arr2 = [];
let fn;
let person = {
    name: "oriel",
    age: 23,
    getName() {
        return this.name;
    },
};
function getPerson(p) {
}
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    getName() {
        return this.name;
    }
}
function fun(a, b) {
    if (a % 2 === 0)
        return b;
    return a + 5;
}
let un = 2;
un = "";
function check(a) {
    if (typeof un === "number") {
        console.log(un + 4);
    }
    else {
        un.split(";");
    }
}
