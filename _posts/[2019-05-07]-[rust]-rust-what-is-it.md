```
layout:	title
postRust:| ស្វែងយល់ពី​Rust លឿនដូច C/C++
```

Rust (/rʌst/)  គឺជាភាសាបង្កើតកម្ម​វិធីសម្រាប់ប្រពន្ធ័ (system programming language) ដែលអាចមាន​ល្បឿនដំណើរលឿន,កាត់បន្ថយ bug crash (segfaults),
កាត់បន្ថយ data race, ធានាបាន memory safe ដោយ​មិន​ចាំបាច់ប្រើ garbage collector!

![_config.yml]({{ site.baseurl }}/images/rust.jpg)

ឃ្លាបញ្ជាសម្រាប់ការបង្កើតកម្មវិធី Hello World ក្នុង Rust ដូចខាងក្រោមនេះ:

fn main() {
  println!("hello, {}", "world");
}

អ្នកឃើញកូដខាងលើគឺប្រៀបដូចនឹង Cបន្តិច, ដូចនឹង Go​បន្តិច ឬ Swift, Java, C#,... មែនអត់?

# ហេតុអ្វីត្រូវប្រើ Rust?

អ្នកប្រហែលជាស្គាល់សមត្ថភាពក្នុងការគ្រប់គ្រងធនធាននៅពេលធ្វើការជាមួយភាសាដូចជា C / C ++ ឬ Java, Python, Ruby, JavaScript, ...

* ជាមួយ C / C ++ អ្នកទទួលបាន:

ត្រួតត្រាទាំងស្រុងលើអ្វីគ្រប់យ៉ាង ( malloc, free, ... )
ឈឺក្បាលញឹកញាប់ជាមួយ memory leak, data race, segfaults, ...
