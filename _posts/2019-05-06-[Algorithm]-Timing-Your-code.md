---
layout: post
title: Algorithm|វាស់ពេលវេលាពេលដំណើរកូដយើង
---

ពេលខ្លះជាអ្នកសរសេរកូដយើងត្រូវគិតដល់ថាតើកូដរបស់រត់លឿនប៉ុណ្ណា​ហើយ​តើមាន​វិធីណាទៀតដើម្បីធ្វើអោយប្រសើរឡើង។ដើម្បីងាយយល់គឺខ្ញុំបានសាកល្បងជាកូដខាងក្រោមនេះ
![_config.yml]({{ site.baseurl }}/images/timing.png)

```javascript
function addUpTo(n) {

    let total = 0;
    for (let i = 1; i<= n ; i++){
        total +=1
    }
    return total;
}
var t1 = performance.now()
addUpTo(1000000000)
var t2 = performance.now()

console.log(`Time Elapse: ${(t2 - t1) / 1000} second. `)
```

ប្រៀបធៀបនឹងកូដខាងក្រោមនេះ

```javascript
function addUpTo(n) {
    return n * (n+1) / 2;
}
var t1 = performance.now()
addUpTo(1000000000)
var t2 = performance.now()

console.log(`Time Elapse: ${(t2 - t1) / 1000} second. `)
```

ពេលដំណើរការយើងនឹងឃើញ​ថាតើមួយណាលឿនជាង ដូច្នេះពេលសរសេរគឹគម្បីគិតថាតើវិធីណាមួយល្អប្រសើរ។
