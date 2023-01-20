from collections import defaultdict

class Solution(object):
    def is_valid(self, d, s, word_length, total_word_length):
        copy_d = d.copy()
        for i in range(0, total_word_length, word_length):
            w = s[i: i + word_length]
            if w in copy_d:
                copy_d[w] -= 1
                if copy_d[w] < 0:
                    return False
            else:
                return False
        return True

    def findSubstring(self, s, words):
        a, i, word_length, total_word_length = [], 0, len(words[0]), len(words) * len(words[0])
        d = defaultdict(int)
        for word in words:
            d[word] += 1

        while i + total_word_length <= len(s):
            if self.is_valid(d, s[i: i + total_word_length], word_length, total_word_length):
                a.append(i)
            i += 1
        return a
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """