#coding=utf-8
import sys
import os

def findPatternInFile(pattern, filename):
    res = []
    cnt = 1
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if pattern in line:
                res.append(cnt)
            cnt += 1
    return res

if __name__ == '__main__':
    rootPath = ''
    pattern = ''
    ignoreCurrentDir = False
    isRecursive = False
    for i in range(1, len(sys.argv)):
        if sys.argv[i][0] == '-':
            augment = sys.argv[i]
            for ch in augment[1:]:
                if ch == 'r':
                    isRecursive = True
                elif ch == 'i':
                    ignoreCurrentDir = True
                else:
                    print u'无效的参数，无法识别'
                    sys.exit()
            if 'r' in augment:
                isRecursive = True
            if 'i' in augment:
                ignoreCurrentDir = True
        else:
            if rootPath == '':
                rootPath = sys.argv[i]
            elif pattern == '':
                pattern = sys.argv[i]
                break
    while rootPath == '':
        print u'请输入需要操作的路径：'
        rootPath = raw_input()
    while pattern == '':
        print u'请输入需要查找的文本：'
        pattern = raw_input()
    if isRecursive:
        for parent, dirs, files in os.walk(rootPath):
            if ignoreCurrentDir and parent == rootPath:
                continue
            for f in files:
                res = findPatternInFile(pattern, parent + '\\' + f)
                for row in res:
                    print parent + '\\' + f, row
    else:
        if ignoreCurrentDir:
            sys.exit()
        filenams = os.listdir(rootPath)
        for filename in filenams:
            if os.path.isfile(filename):
                res = findPatternInFile(pattern, rootPath + '\\' + filename)
                for row in res:
                    print rootPath + '\\' + filename, row
