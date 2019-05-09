---
layout: post
title: algorithm|តើ Hash SHA256​ដំណើរការដូចម្ដេច?
---

A cryptographic hash is an algorithm that takes an input and turns it into an output of a fixed size. 
It looks like a mix up of numbers and letters. 

![_config.yml]({{ site.baseurl }}/images/sha256.png)


There are many types of cryptographic hashes. Bitcoin, for example,uses a hashing algorithm called SHA-256. 
Here is an example of how this is done and the example code used.

```
import java.security.MessageDigest;
import java.util.Scanner;
import javax.xml.bind.DatatypeConverter;

public class HashUsingSHA256InJava {
	public static void main(String[] args){
		Scanner sn = new Scanner(System.in);
		System.out.print("Please enter data for which SHA256 is required");
		String data  = sn.nextLine();
		
		HashUsingSHA256InJava sj = new HashUsingSHA256InJava();
		String hash = sj.getSHA256Hash(data);
		System.out.println("The SHA256 (Hexadecimal encoded) hash is:"+hash)
	
	}
	private String getSHA256Hash(String data){
		String result = null;
		try {
			MessageDigest digest = MessageDigest.getInstance("SHA-256");
			byte[] hash = digest.digest(data.getBytes("UTF-8");
			return bytesToHex(hash);// make it printable
		}catch (Exception ex) {
			ex.printStackTrace();
		}
		return result;
	}
	private String bytesToHex(byte[] hash) {
		return DatatypeConverter.printHexBinary(hash);
	}
}
```
