---
layout: post
title: Rust|ស្វែងយល់ពី​Rust ភាសាដែលលឿនដូច C/C++
---

Rust (/rʌst/)  គឺជាភាសាបង្កើតកម្ម​វិធីសម្រាប់ប្រពន្ធ័ (system programming language) ដែលអាចមាន​ល្បឿនដំណើរលឿន,កាត់បន្ថយ bug crash (segfaults),
កាត់បន្ថយ data race, ធានាបាន memory safe ដោយ​មិន​ចាំបាច់ប្រើ garbage collector!

![_config.yml]({{ site.baseurl }}/images/rust.jpg)

ឃ្លាបញ្ជាសម្រាប់ការបង្កើតកម្មវិធី Hello World ក្នុង Rust ដូចខាងក្រោមនេះ:

```
fn main() {
    let greetings = ["Hello", "Hola", "Bonjour",
                     "Ciao", "こんにちは", "안녕하세요",
                     "Cześć", "Olá", "Здравствуйте",
                     "Chào bạn", "您好", "Hallo",
                     "Hej", "Ahoj", "سلام","สวัสดี","សួស្ដី"];

    for (num, greeting) in greetings.iter().enumerate() {
        print!("{} : ", greeting);
        match num {
            0 =>  println!("This code is editable and runnable!"),
            1 =>  println!("¡Este código es editable y ejecutable!"),
            2 =>  println!("Ce code est modifiable et exécutable !"),
            3 =>  println!("Questo codice è modificabile ed eseguibile!"),
            4 =>  println!("このコードは編集して実行出来ます！"),
            5 =>  println!("여기에서 코드를 수정하고 실행할 수 있습니다!"),
            6 =>  println!("Ten kod można edytować oraz uruchomić!"),
            7 =>  println!("Este código é editável e executável!"),
            8 =>  println!("Этот код можно отредактировать и запустить!"),
            9 =>  println!("Bạn có thể edit và run code trực tiếp!"),
            10 => println!("这段代码是可以编辑并且能够运行的！"),
            11 => println!("Dieser Code kann bearbeitet und ausgeführt werden!"),
            12 => println!("Den här koden kan redigeras och köras!"),
            13 => println!("Tento kód můžete upravit a spustit"),
            14 => println!("این کد قابلیت ویرایش و اجرا دارد!"),
            15 => println!("โค้ดนี้สามารถแก้ไขได้และรันได้"),
            15 => println!("អ្នកអាចកែកូដនឹងដំណើរការបាន។"),
            _ =>  {},
        }
    }
}
```

អ្នកឃើញកូដខាងលើគឺប្រៀបដូចនឹង C បន្តិច, ដូចនឹង Go​បន្តិច ឬ Swift, Java, C#,... មែនអត់?

# ហេតុអ្វីត្រូវប្រើ Rust?

អ្នកប្រហែលជាស្គាល់សមត្ថភាពក្នុងការគ្រប់គ្រងធនធាននៅពេលធ្វើការជាមួយភាសាដូចជា C / C ++ ឬ Java, Python, Ruby, JavaScript, ...

** ជាមួយ C / C ++ អ្នកទទួលបាន:

- ត្រួតត្រាទាំងស្រុងលើអ្វីគ្រប់យ៉ាង ( malloc, free, ... )
- ឈឺក្បាលញឹកញាប់ជាមួយ memory leak, data race, segfaults, ...

# លក្ខណៈពិសេស
- zero-cost abstractions
- move semantics
- តែងតែធានាបាននូវ​សុវត្ថភាអង្គចងចាំ
-threads មិនកើតមានករណី data races
- trait-based generics
- pattern matching
- type inference
- runtime តូច
- Binding ពី C ប្រកបដោយប្រសិទ្ធិភាពខ្លាំង។
