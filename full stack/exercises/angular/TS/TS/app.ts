let a: string
let b: number
let c: boolean
let d: null
let e: undefined
let arr = ["", "or", "2"]
let arr2: number[] = []
let fn: (a: number) => number
let person: Person2 = {
    name: "oriel",
    age: 23,
    getName() {
        return this.name
    },
}

function getPerson(p: Person2) {

}

class Person {
    name: string
    age: number

    constructor(name: string, age: number) {
        this.name = name
        this.age = age
    }

    getName() {
        return this.name
    }
}

type Person2 = {
    name: string,
    age: number,
    getName: () => string
}


function fun(a: number, b: string) {
    if (a % 2 === 0) return b
    return a + 5
}

let un: number | string = 2
un = ""
function check(a:number | string) {
    if (typeof un === "number") {
        console.log(un + 4);
    }
    else {
        un.split(";")
    }
    
}