---
layout: post
title: Rust|define trait in rust
---


Similar to interfaces in other languages, traits allow you to set 'rules' or 'requirements' for a particular struct in order for it to be considered to be 'something'.

In this article we create a trait called 'HasVoiceBox' which says that any Struct implementing this trait must have a speak() and can_speak() method defined on it.

For more information refer to the Rust documentation:
https://doc.rust-lang.org/1.8.0/book/traits.html

If this article helped you out and you'd like to see more,


កូដ Rust ជាឧទាហណ៏ ដូចខាងក្រោមនេះ:

```
struct Player {
    first_name: String,
    last_name: String,
}

trait FullName {
    fn full_name(&self) -> String;
}
impl FullName for Player {
    fn full_name(&self)->String {
        format!("{} {}", self.first_name, self.last_name)
    }
}
fn main(){
    let player_2 = Player{
        first_name: "Soeng".to_string(),
        last_name: "kanel".to_string(),
    };
    println!("Player 2: {}", player_2.full_name())
}
```

