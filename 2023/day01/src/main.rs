use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::vec;

fn p1(lines: &Vec<String>) {
    let res: u32 = lines
        .iter()
        .map(|line| {
            let first_num = line
                .chars()
                .find(|c| c.is_digit(10))
                .and_then(|c| c.to_digit(10));
            let last_num = line
                .chars()
                .rev()
                .find(|c| c.is_digit(10))
                .and_then(|c| c.to_digit(10));

            match (first_num, last_num) {
                (Some(first), Some(last)) => first * 10 + last,
                _ => 0,
            }
        })
        .sum();

    print!("{res}")
}

fn p2(lines: &Vec<String>) {
    let mut str_to_int = HashMap::new();
    str_to_int.insert("one", 1);
    str_to_int.insert("two", 2);
    str_to_int.insert("three", 3);
    str_to_int.insert("four", 4);
    str_to_int.insert("five", 5);
    str_to_int.insert("six", 6);
    str_to_int.insert("seven", 7);
    str_to_int.insert("eight", 8);
    str_to_int.insert("nine", 9);

    let mut num_lines: Vec<Vec<u32>> = vec![];

    for line in lines {
        let mut nums: Vec<u32> = vec![];
        for i in 0..line.chars().count() {
            if line.chars().collect::<Vec<char>>()[i].is_digit(10) {
                nums.push(
                    line.chars().collect::<Vec<char>>()[i]
                        .to_digit(10)
                        .unwrap_or_default(),
                );
                continue;
            }
            for k in str_to_int.keys() {
                if line[i..].starts_with(k) {
                    nums.push(str_to_int.get(k).expect("").clone());
                    break;
                }
            }
        }
        num_lines.push(nums)
    }

    let res: u32 = num_lines
        .iter()
        .map(|nums| nums.first().unwrap() * 10 + nums.last().unwrap())
        .sum();

    print!("{res}")
}

fn main() {
    let file: File = File::open("src/input.txt").expect("could not read file");
    let reader: BufReader<File> = BufReader::new(file);

    let mut lines: Vec<String> = vec![];

    for line in reader.lines() {
        let line = line.expect("line is not a string");
        lines.push(line)
    }

    p1(&lines);
    println!("");
    p2(&lines);
}
