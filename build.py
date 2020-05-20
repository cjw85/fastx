from cffi import FFI

ffibuilder = FFI()
ffibuilder.set_source(
    "_fastx",
    r"""
    #include <zlib.h>
    #include <stdio.h>
    #include "kseq.h"

    KSEQ_INIT(gzFile, gzread)

    kseq_t *open_fastx (const char *fn) {
        gzFile fp = gzopen(fn, "r");
        return kseq_init(fp);
    }

    void close_fastx(kseq_t *kseq) {
        gzclose(kseq->f->f);
        kseq_destroy(kseq);
    }

    """,
    libraries=['z'], include_dirs=['src']
)

ffibuilder.cdef(
    r"""
    typedef struct kstring_t {
        size_t l, m; char *s;
    } kstring_t;

    typedef struct kseq_t {
        kstring_t name, comment, seq, qual;
        ...;
    } kseq_t;

    kseq_t *open_fastx(const char *fn);
    void close_fastx(kseq_t *kseq);
    int kseq_read(kseq_t *kseq);
    """
)
ffibuilder.compile(verbose=True)
