
import time
import random
import threading
try:
    from crayons import green, red
except ImportError:
    green = red = print

from kuai import Kuai, set_backend, kuai_backend
set_backend("priority")
print("Using the Kuai `{}` backend".format(kuai_backend()))


class Model:
    def __init__(self, data):
        self._innerData = data

    def get(self, item):
        try:
            rv = self._innerData[item]
        except KeyError:
            return None
        else:
            # ~&% Kuài %&~
            Kuai.emit("model-accessed", item)
            return rv

    def set(self, item, value):
        self._innerData[item] = value

        # ~&% Kuài %&~
        Kuai.emit("model-changed", data=(item, value))


class Ego:
    def __init__(self, value):
        self.total = value

    def boost(self):
        self._stroke('gentle')

    def super_boost(self):
        self._stroke('hard')

    def _stroke(self, pressure):
        if pressure is 'hard':
            self.total += 10
        else:
            self.total += 1

        # ~&% Kuài %&~
        Kuai.emit('stroked')


class Boss:
    def __init__(self):
        self.ego = Ego(1)

        # ~&% Kuài %&~
        Kuai.on("model-changed", self.onModelChanged)
        Kuai.on("model-accessed", self.onModelAccessed)
        Kuai.on("jobs-done", self.onJobsDone)
        Kuai.on("stroked", self.onStroked)

    def onModelChanged(self, data):
        print(red("Big boss man: You changed {} to {}.. Why??"
                  .format(data[0], data[1])))
        self.ego.boost()

    def onModelAccessed(self, item):
        print(red("Big boss man: Gaawd.. Why the {} one? I don't like it."
                  .format(item)))
        self.ego.boost()

    def onJobsDone(self, *args):
        print(red("Big boss man: Hey! Why aren't you working!?234?#$%"))
        self.ego.super_boost()

    def onStroked(self, *args):
        if (self.ego.total % 3 == 0):
            if (self.ego.total % 5 == 0):
                print(red('Big boss man yells: FIZZ-BUZZ!!$#!$#@!@!'))
                return
            print(red('Big boss man thinks: Er gerd ya, erm so cool.'))

        elif (self.ego.total % 5 == 0):
            print(red('Big boss man thinks: A huhma-na, huhma-na, huhma-na.'))


class Worker:

    def __init__(self, model):
        self.activities = [
            "queryModel",
            "mutateModel"
        ]
        self.data = model
        self.t = threading.Thread(target=self.run)
        self.t.daemon = True
        self.t.start()

        # ~&% Kuài %&~
        Kuai.on('jobs-done', self.jobsDone, priority=1)

    def jobsDone(self, exclaim):
        print(green("Me: {}".format(exclaim)))

    def run(self):
        while True:
            job = random.choice(self.activities)
            if job == "queryModel":
                choice = random.choice("first second third".split(' '))
                print(green("Me: Better do some research on this {} one.."
                            .format(choice)))
                self.data.get(choice)
                print(green("Me: Okay so {} choice is the one then.."
                            .format(choice)))
            if job == "mutateModel":
                data = random.choice("first second third".split(' '))
                this = random.randint(1, 100)
                print(green("Me: Hmm.. Think i'll change {} to {}..".format(data, this)))
                self.data.set(data, this)
            time.sleep(random.randint(3, 9))

            # ~&% Kuài %&~
            Kuai.emit("jobs-done", "Hm, a job well done I'd say!")


def main():
    companyData = Model({
        "first": 1,
        "second": 2,
        "third": 3
    })
    boss = Boss()       # If we don't assign Boss() to a variable it will get garbage collected.
    Worker(companyData)

    input()  # Press any key to exit demo
    exit(1)


if __name__ == '__main__':
    main()
