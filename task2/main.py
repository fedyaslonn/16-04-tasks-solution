class Solution:
    def solution(self, strs):
        res_dict = {}
        res = []
        for word in strs:
            sorted_words = ''.join(sorted(word))
            if sorted_words in res_dict:
                res_dict[sorted_words].append(word)
            else:
                res_dict[sorted_words] = [word]
        for i in res_dict.values():
            res.append(i)
        return res


sol = Solution()
print(sol.solution(["eat","tea","tan","ate","nat","bat"]))
print(sol.solution([""]))
print(sol.solution(["a"]))

