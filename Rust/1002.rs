use std::io;

fn main() {
    let mut inputA = String::new();
    io::stdin().read_line(&mut inputA);
    let r: f64 = inputA.trim().parse().unwrap();
    let area: f64 = 3.14159 * r * r;
    println!("A={:.4}", area);
}
