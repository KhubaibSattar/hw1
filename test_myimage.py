import csv

from List import *
from PIL import Image
from urllib.request import urlopen

images = urlopen("https://waqarsaleem.github.io/img.txt").readlines()
images = [img.decode('utf-8').strip() for img in images]

img1 = MyImage.open(
    urlopen('https://cdn.sstatic.net/Sites/stackoverflow/img/logo.png'))
img2 = MyImage.open(
    urlopen('https://cdn.sstatic.net/Sites/stackoverflow/img/logo.png'))


class Case:
    def __init__(self):
        self.source = ''
        self.suppressed = ''
        self.rotated = ''
        self.masked = ''
        self.suppress = []
        self.maskfiles = []
        self.maskaverages = []

    def __repr__(self):
        return f'src: {self.source}, rot: {self.rotated}\n'\
            f'sup: {self.suppress}, sup: {self.suppressed}\n'\
            f'masks: {self.maskfiles}, avg: {self.maskaverages}, masked: {self.masked}'


casefile = "tests.csv"
cases = []


def local_or_remote_path(row, idx, prefix, suffix):
    if idx >= len(row) or not (f := row[idx]):
        return
    if f.startswith('https://'):
        return f
    return prefix + f + suffix


with open(casefile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        if not (row := list(map(str.strip, row))):
            continue
        case = Case()
        case.source = local_or_remote_path(row, 0, 'images/', '.png')
        case.rotated = local_or_remote_path(row, 1, 'images/', '.png')
        case.suppress = [(f := row[i]) == '1' for i in range(2, 5)
                         if i < len(row)]
        case.suppressed = local_or_remote_path(row, 5, 'images/', '.png')
        if (maskfiles := local_or_remote_path(row, 6, '', '')):
            maskfiles = maskfiles.split(':')
            case.maskfiles = [f if f.startswith('https://')
                              else 'masks/mask-'+f+'.txt' for f in maskfiles]
            case.maskaverages = [a == '1' for a in row[7].split(':')]
            case.masked = local_or_remote_path(row, 8, 'images/', '.png')
        cases.append(case)

outputfile = 'output.png'


def test_rotation():
    for case in cases:
        if case.rotated:
            rotations(MyImage.open(case.source)).save(outputfile)
            assert Image.open(outputfile) == Image.open(case.rotated),\
                f'rotation of {case.source} does not match reference'\
                f'{case.rotated}'


def test_suppression():
    for case in cases:
        if case.suppressed:
            sp = case.suppress
            remove_channel(MyImage.open(case.source),
                           red=sp[0], green=sp[1], blue=sp[2]).save(outputfile)
            assert Image.open(outputfile) == Image.open(case.suppressed),\
                f'suppression of {case.source} does not match reference'\
                f'{case.suppressed} under channels {case.suppress}'


def test_mask():
    for case in cases:
        if case.masked:
            avgs = case.maskaverages
            files = case.maskfiles
            dst = apply_mask(MyImage.open(case.source),
                             files[0], average=avgs[0])
            for mask, avg in zip(files[1:], avgs[1:]):
                dst = apply_mask(dst, mask, average=avg)
            dst.save(outputfile)
            assert Image.open(outputfile) == Image.open(case.masked),\
                f'masking of {case.source} does not match reference '\
                f'{case.masked}\nunder masks {case.maskfiles}'\
                f' and averages {case.maskaverages}'
