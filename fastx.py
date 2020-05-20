import _fastx
import sys

class Fastx:
    """Just a fasta/q parser build on kseq.h.

    >>> for name, seq, qualities in Fastx(filename):
    >>>    print(">{}\n{}".format(name, seq))
    """

    def __init__(self, fname):
        """Initialize parser.

        :param fname: input file path.
        """
        self.kseq = _fastx.lib.open_fastx(fname.encode())

    def __del__(self):
        _fastx.lib.close_fastx(self.kseq)

    def __next__(self):
        if _fastx.lib.kseq_read(self.kseq) >= 0:
            return (
                _fastx.ffi.string(self.kseq.name.s),
                _fastx.ffi.string(self.kseq.seq.s),
                _fastx.ffi.string(self.kseq.qual.s) if self.kseq.qual.l > 0 else "")
        else:
            raise StopIteration()

    def __iter__(self):
        return self
