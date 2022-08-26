class Solution:
    def isIsomorphic(self, s, t):

        #######################################################

        # this version of the code has a timeout limit, my initial hunch of using a dict to create a map was right
        # ommited_indices = []
        # list_s = list(s)
        # list_t = list(t)
        #
        # for char_s, char_t in zip(s, t):
        #     indices_s = [index for index, char in enumerate(list(s)) if char == char_s]
        #     indices_t = [index for index, char in enumerate(list(t)) if char == char_t]
        #
        #     if indices_t == indices_s:
        #         for index in indices_s:
        #             list_t[index] = char_s
        #         ommited_indices.append(indices_s)
        #
        # if list_t == list_s:
        #     return True
        # return False
        #######################################################
        dict_s = {}
        dict_t = {}

        for index, character in enumerate(s):
            if character not in dict_s:
                dict_s[character] = [index]
            else:
                dict_s[character].append(index)

        for index, character in enumerate(t):
            if character not in dict_t:
                dict_t[character] = [index]
            else:
                dict_t[character].append(index)

        if list(dict_s.values()) == list(dict_t.values()):
            return True
        return False


_object = Solution()
_object.isIsomorphic(s="tada", t="baba")
