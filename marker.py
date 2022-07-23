def mark(guess, answer):
    countsInCorrectPosition = [0]*26
    for (gl, al) in zip(guess, answer):
        if gl == al:
            countsInCorrectPosition[ord(gl) - ord('a')] += 1

    answerCharFreq = [0]*26
    for char in answer:
        answerCharFreq[ord(char) - ord('a')] += 1

    runningNonGreenCounts = [0]*26
    for (gl, al) in zip(guess, answer):
        idx = ord(gl) - ord('a')
        if (gl == al):
            yield 'g'
        elif runningNonGreenCounts[idx] < answerCharFreq[idx] - countsInCorrectPosition[idx]:
            yield 'y'
        else:
            yield 'b'
        if (gl != al):
            runningNonGreenCounts[idx] += 1
