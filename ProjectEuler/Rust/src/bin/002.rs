fn main() {
    let mut first = 1i32;
    let mut second = 2i32;
    let mut total = 2i32;

    while second <= 4000000 {
        let temp = first + second;
        if &temp % 2 == 0 {
            total += temp;
        }
        second = temp;
        first = temp - first;
    }

    println!("{}", total) // Outputs 4613732
}
