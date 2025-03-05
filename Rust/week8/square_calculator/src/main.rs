use std::io;

fn main() {
    println!("-------------------------------------");
    println!("|     Susie's Square Calculator     |");
    println!("-------------------------------------");
    // create a mutable string to store user input
    let mut input = String::new();
    // prompt the user to enter the length of a side
    println!("Enter the length of a side: ");
    // read the user input from the standard input(keyboard)
    // store it in the 'input' var
    io::stdin().read_line(&mut input).expect("Failed to read line: ");
    // trim any whitespaces from the input
    // parse it as a 64-bit float
    // store it ni the 'side' var
    let side: f32 = input.trim().parse().expect("Enter a valid number: ");
    // calculate the area of the square
    let area = side * side;
    // calculate the perimeter of the square
    let perimeter = side * 4.0;
    //disp the results
    println!("     Area : {}", area);
    println!("Perimeter : {}", perimeter);
}
