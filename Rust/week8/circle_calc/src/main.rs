use std::io;

fn main() {
    println!("------------------------------------------------");
    println!("|     Circle Calculator written in Rust btw    |");
    println!("------------------------------------------------");
    loop {
        println!("Enter the radius:");
        let mut rad = String::new();
        let pi = std::f32::consts::PI;
        io::stdin()
            .read_line(&mut rad)
            .expect("Failed to read line");
        let rad: f32 = match rad.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        let diam = rad * 2.0;
        let area = rad * rad * pi;
        let circ = diam * pi;
        println!("     Diameter: {diam}");
        println!("         Area: {area}");
        println!("Circumference: {circ}");
        println!("New calculation? y/n");
        let mut answer = String::new();
        io::stdin()
            .read_line(&mut answer)
            .expect("Failed to read line");
        if !answer.trim().starts_with('y') {
            break;
        }
    }
}
