# Author: Jin


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]
        watch = ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
        ans = watch
        for i in range(num - 1):
            temp = []
            for a in ans:
                for j in range(len(watch)):
                    time1 = a.split(':')
                    time2 = watch[j].split(':')
                    if time1[0] >= time2[0] and time1[1] >= time2[1]:
                        continue
                    if int(time1[1]) + int(time2[1]) >= 10:
                        time = str(int(time1[0]) + int(time2[0])) + ":" + str(int(time1[1]) + int(time2[1]))
                    else:
                        time = str(int(time1[0]) + int(time2[0])) + ":0" + str(int(time1[1]) + int(time2[1]))
                    temp.append(time)
            ans = temp
        return ans

s = Solution()
n = int(input())
print(s.readBinaryWatch(n))