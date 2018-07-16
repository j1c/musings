fn main() {
    let mut longest = 0u64;
    let mut sequence = 0u64;

    for x in 2u64..1000000 {
        let mut y = x;
        let mut counter = 1u64;

        while y != 1 {
            if y % 2 != 0 {
                y = 3 * y + 1;
            } else {
                y /= 2;
            }
            counter += 1;
        }

        if longest < counter {
            longest = counter;
            sequence = x;
        }
    }
    println!("{}", sequence)
}
