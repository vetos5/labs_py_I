from dataclasses import dataclass
from vectorExceptions import VectorExceptions

@dataclass
class Vector:
    data: list

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def add(self, other):
        if len(self.data) != len(other.data):
            print(VectorExceptions.VECTOR_SIZE_MISMATCH_MSG)
            exit(1)

        result_vector = [self.data[i] + other.data[i] for i in range(len(self.data))]
        return Vector(result_vector)

    def subtract(self, other):
        if len(self.data) != len(other.data):
            print(VectorExceptions.VECTOR_SIZE_MISMATCH_MSG)
            exit(1)

        result_vector = [self.data[i] - other.data[i] for i in range(len(self.data))]
        return Vector(result_vector)

    def dot_product(self, other):
        if len(self.data) != len(other.data):
            print(VectorExceptions.VECTOR_SIZE_MISMATCH_MSG)
            exit(1)

        return sum(self.data[i] * other.data[i] for i in range(len(self.data)))