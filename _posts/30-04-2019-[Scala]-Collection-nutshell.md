---
layout: post
title: Scala|យល់ពីScala Collection map,flatMap
---

Scala ជាភាសាបង្កើតដែលបង្កើតឡើងដើម្បីក្លាយជាភាសាមួយដែលប្រសើរជា Java (Better Java) ព្រោះមានបទបែនខ្ពស់និងធ្វើការបានទាំងលើ OOP និង Function Programming.
![_config.yml]({{ site.baseurl }}/images/scala.png)


យើងអាចសង្កេតលើ កូដនៃCollection ខាងក្រោមនេះ៖

```
scala collection
1) map

	+List

	scala> List(1,2,3).map { x => x*2 }
	List[Int] = List(2, 4, 6)

	scala> List(1,2,3).map(_*2)
	List[Int] = List(2, 4, 6)

	+Array
	scala> Array(1,2,3).map(_*2)
	Array[Int] = Array(2, 4, 6)

	+Set
	scala> Set(1,2,2,3).map(_*2)
	Set[Int] = Set(2, 4, 6)
	scala> (0 until 5).map(_*2)
	IndexedSeq[Int] = Vector(0, 2, 4, 6, 8)

	+Map
	The Map collection also has a map method, but it converts each key-value pair into a tuple for submission to the mapping function:
	
	scala> Map("key1" -> 1, "key2" -> 2).map { keyValue:(String,Int) => keyValue match { case (key, value) => (key, value*2) }}
	Map[String,Int] = Map(key1 -> 2, key2 -> 4)

	scala> Map("key1" -> 1, "key2" -> 2).map {
			 case (key, value) => (key, value*2)
		   }
	Map[String,Int] = Map(key1 -> 2, key2 -> 4)

	scala> Map("key1" -> 1, "key2" -> 2).map {
			 case (key, value) => value * 2
		   }
	Iterable[Int] = List(2, 4)
	scala> Map("key1" -> 1, "key2" -> 2).map {
			 case (key, value) => value * 2
		   }.toSet
	Set[Int] = Set(2, 4)

	+String 
	scala> "Hello".map { _.toUpper }
	String = HELLO

Scala collections also support flatten, which is usually used to eliminate undesired collection nesting:

scala> List(List(1,2,3),List(4,5,6)).flatten
List[Int] = List(1, 2, 3, 4, 5, 6)

The flatMap method acts as a shorthand to map a collection and then immediately flatten it. This particular combination of methods is quite powerful. For example, we can use flatMap to generate a collection that is either larger or smaller than the original input:

scala> List(1,4,9).flatMap { x => List(x,x+1) }
List[Int] = List(1, 2, 4, 5, 9, 10)
scala> List(1,4,9).flatMap { x => if (x > 5) List() else List(x) }
List[Int] = List(1, 4)

The true power of map and flatMap becomes much more apparent when we look at Options and Futures.
```
