fastx
=====

Just a fasta/q parser based on `kseq.h` for CPython and PyPy.

    import fastx
    for name, seq, qual for Fastx(filename):
        print(">{}\n{}".format(name, seq))

This library was inspired by the benchmarking page below and that the
existing fastest entry for python works only on CPython. It is not
intended for general use.

https://github.com/lh3/biofast


Benchmarking
------------

Line profiling the previous code we find program spent as much time adding python
objects together as it does in the pyfastx package:
```
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    28                                           @profile
    29                                           def main():
    30         1         21.0     21.0      0.0      n, slen, qlen = 0, 0, 0
    31   5682011    7366975.0      1.3     47.9      for name, seq, qual in pyfastx.Fastq(sys.argv[1], build_index=False):
    32   5682010    2324629.0      0.4     15.1          n += 1
    33   5682010    2783887.0      0.5     18.1          slen += len(seq)
    34   5682010    2909447.0      0.5     18.9          qlen += qual and len(qual) or 0
    35         1        158.0    158.0      0.0      print('{}\t{}\t{}'.format(n, slen, qlen))
```

This modules works both under CPython and PyPy, unlike pyfastx which is
strictly a CPython extension. When using PyPy, the difference between
the Python and C implementation is narrowed dramatically. 

```
Running cpython
5682010	568201000	568201000

real	0m11.444s
user	0m10.944s
sys	0m0.284s


Running pypy
5682010	568201000	568201000

real	0m1.973s
user	0m1.555s
sys	0m0.258s


Running C
5682010	568201000	568201000

real	0m1.764s
user	0m1.508s
sys	0m0.217s
```
