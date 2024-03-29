---
layout: post
date: 2023-08-15 17:35:30 +0800
tags: leetcode75 Two_Pointers String 双指针 字符串
---

# 1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```
Example 2:
```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
```
Example 3:
```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

Constraints:

+ 1 <= word1.length, word2.length <= 100
+ word1 and word2 consist of lowercase English letters.

# Solution 1

Java

``` java
class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder result = new StringBuilder();
        int maxlen = Integer.max(word1.length(), word2.length());
        int minlen = Integer.min(word1.length(), word2.length());
        for (int i = 0; i < minlen; i++) {
            result.append(word1.charAt(i));
            result.append(word2.charAt(i));
        }
        for (int i = minlen; i < Integer.min(word1.length(), maxlen); i++) {
            result.append(word1.charAt(i));
            // result.append(' ');
        }
        for (int i = minlen; i < Integer.min(word2.length(), maxlen); i++) {
            // result.append(' ');
            result.append(word2.charAt(i));
        }
        return result.toString();
    }
}
```
