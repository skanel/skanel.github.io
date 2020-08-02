លំហាត់ Rust សម្រាប់បញ្ចូលពត៌មានពីក្ដាយចុចរួចបញ្ចេញលទ្ធផលមកវិញលើអេក្រង់។ 

```
use std::io;
use std::io::Write;

fn main() {

    let name = input("តើអ្នកឈ្មោះអ្វី? ").expect("Something went wrong!");
    println!("សួរស្ដី, {}!", name);

    let age = input("តើអ្នកអាយុប៉ុន្មាន? ")
        .expect("failed to get age")
        .parse::<u8>().expect("Invalid age.");

    println!("អ្នកមានអាយុ {} ឆ្នាំ ហើយ!", age);
}

fn input(user_message: &str) -> io::Result<String> {

    print!("{}", user_message);
    io::stdout().flush()?;
    let mut buffer: String = String::new();
    io::stdin().read_line(&mut buffer)?;
    Ok(buffer.trim_end().to_owned())
}
```

output


> តើអ្នកឈ្មោះអ្វី? កុយ ពិសី

> សួរស្ដី, កុយ ពិសី!

> តើអ្នកអាយុប៉ុន្មាន? 45

> អ្នកមានអាយុ 45 ឆ្នាំ ហើយ!
`
