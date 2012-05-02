#!/usr/bin/env python

class AnimationFrames(object):
    def __init__(self, frames, loops=-1):
        self._times = []
        self._data = []
        total = 0
        for t, data in frames:
            total += t
            self._times.append(total)
            self._data.append(data)
        
        self.end = total
        self.loops = loops

    def get(self, time):
        if self.loops == -1 or time < self.loops * self.end:
            time %= self.end

        if time > self.end:
            return self._data[-1]

        idx = 0
        while self._times[idx] < time:
            idx += 1

        return self._data[idx]
