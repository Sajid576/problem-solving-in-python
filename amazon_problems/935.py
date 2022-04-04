from my_test import test

from typing import List


# def reorderLogFiles(logs: List[str]) -> List[str]:
#     letter_logs = []
#     digit_logs = []

#     for i in range(len(logs)):
#         logList = logs[i].split(' ')
#         if(logList[1].isnumeric()):
#             digit_logs.append(logs[i])
#         else:
#             letter_logs.append(logs[i])

#     # letter_logs.sort(key=lambda x: ' '.join(x.split()[1:]) + x.split()[0])
#     letter_logs = sorted(letter_logs, key=lambda x: (
#         x.split()[1:], x.split()[0]))
#     print(letter_logs)
#     return letter_logs + digit_logs


# test(reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]), [
#      "let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"])
# test(reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]), [
#      "g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"])
# test(reorderLogFiles(["dig1 8 1 5 1", "let1 art zero can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]), [
#      "let3 art zero", "let1 art zero can", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"])
x = 'hello sajid l1 l2'
print(x.split()[1:], x.split()[0])
