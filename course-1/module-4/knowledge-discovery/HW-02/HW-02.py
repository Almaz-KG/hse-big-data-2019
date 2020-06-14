import numpy
from functools import reduce


def create_random_vector(size):
    return numpy.random.randint(low=0, high=10, size=size)


def extract_canonical_info(vector):
    return (1,
            vector,
            numpy.outer(vector, vector.T)
            )


def initial_canonical_info():
    return (0,
            numpy.zeros(VECTOR_SIZE),
            numpy.zeros(shape=(VECTOR_SIZE, VECTOR_SIZE))
            )


def reduce_canonical_info(lhs, rhs):
    # Extracting canonical info from tuple3
    (ln, lS, lR) = lhs
    (rn, rS, rR) = rhs

    n = ln + rn
    S = lS + rS
    R = lR + rR

    # New canonical info - setting to tuple3
    return n, S, R


def sample_mean_vector(canonical_info):
    n, S, R = canonical_info
    return S * (1 / n)


def sample_covariance_matrix(canonical_info):
    # V = (1 / (n - 1)) * (R - S - St + nXXt)
    (n, S, R) = canonical_info
    const = n if (n <= 1) else 1 / (n - 1)

    X = sample_mean_vector(canonical_info)
    nXXt = X * n * X.T
    M = R - S - S.T + nXXt

    return M * const


def get_canonical_info(vectors):
    if (len(vectors[0]) != VECTOR_SIZE):
        raise AttributeError("Please, provide a valid vectors")

    # map phase
    canonical_infos = list(map(lambda v: extract_canonical_info(v), vectors))

    # reduce phase
    result = reduce(lambda lhs, rhs: reduce_canonical_info(lhs, rhs), canonical_infos, initial_canonical_info())

    return result


VECTOR_SIZE = 3
if __name__ == '__main__':
    vectors = [create_random_vector(VECTOR_SIZE) for i in range(0, 10)]

    # vectors = [
    #     numpy.zeros(VECTOR_SIZE),
    #     numpy.ones(VECTOR_SIZE),
    #     numpy.ones(VECTOR_SIZE)
    # ]

    # vectors = [numpy.array([1, 2, 3])]

    can_info = get_canonical_info(vectors)
    n, S, R = can_info

    print("========  INTERNALS  =========")
    print("INPUT VECTORS: " + str(vectors))
    print("SUM OF VECTORS: " + str(S))
    print("MATRIX OF VECTORS: " + str(R))
    print("========   RESULTS   =========")
    SMV = sample_mean_vector(can_info)
    SCM = sample_covariance_matrix(can_info)
    print("N: " + str(n))
    print("SMV: " + str(SMV))
    print("SCM: " + str(SCM))
