const fs = require('fs')
const readline = require('readline')

function solve() {
    v = fs.readFileSync("input1.txt", "utf-8").split("\n\n");
    let vals = v.map(cals => {
        return cals.split("\n").map(x => {return parseInt(x)}).reduce((x,y) => {return x + y});
    })

    console.log(Math.max.apply(null, vals))
}

function solve2() {
    
}