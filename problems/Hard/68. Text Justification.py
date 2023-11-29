from typing import List


class Solution:
    def _justify_line(self, line: List[str], maxWidth: int) -> str:
        num_separators = len(line)-1
        avaible_spaces = maxWidth - sum(map(len, line))

        if num_separators == 0:
            return line[0] + ' '*avaible_spaces

        # calculate number of spaces for each separator
        idx = 0
        spaces_config = [0] * num_separators
        while avaible_spaces:
            spaces_config[idx%len(spaces_config)] += 1

            idx+=1
            avaible_spaces -= 1
        
        # add spaces to ords acording to configuration
        resp = ''
        for word, n_space in zip(line, spaces_config):
            resp += word + ' ' * n_space
        resp += line[-1]

        return resp

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_per_line: List[List[str]] = [[]]
        
        # divide words per line acording to 'maxWidth'
        cur_leng = 0
        for word in words:
            if cur_leng + len(word) > maxWidth:
                words_per_line.append([word])
                cur_leng = len(word) + 1
            
            else:
                cur_leng += len(word)+1
                words_per_line[-1].append(word)

        # add padding to justify acording to 'maxWidth'
        justified_text = []
        for line in words_per_line[:-1]:
            justified_text.append(
                self._justify_line(line, maxWidth)
            )
        justified_text.append(
            ' '.join(words_per_line[-1]) + 
            ' ' * (maxWidth - sum(map(len, words_per_line[-1])) - (len(words_per_line[-1]) - 1))
        )
        
        return justified_text


def main():
    s = Solution()

    print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))


if __name__ == '__main__':
    main()
