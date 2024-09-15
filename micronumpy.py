#class MicroNumPy:
    # def __init__(self, name, gender):
    #     # Zuweisung der Argumente zu Attributen der Instanz
    #     self.name = name
    #     self.gender = gender

# numpy.polyfit(servo_1_array[:, 0], servo_1_array[:, 1], 3)
# polyfit([row[0] for row in servo_1_array], [row[1] for row in servo_1_array], 3)


def polyfit(x, y, degree):
    # Erstellen der Designmatrix
    X = [[xi**d for d in range(degree, -1, -1)] for xi in x]
    
    # Transponieren der Matrix X
    XT = list(zip(*X))
    
    # Matrixmultiplikation XT * X
    XT_X = [[sum(a*b for a, b in zip(XT_row, X_col)) for X_col in zip(*X)] for XT_row in XT]
    
    # Matrixmultiplikation XT * y
    XT_y = [sum(a*b for a, b in zip(XT_row, y)) for XT_row in XT]
    
    # Lösen des linearen Gleichungssystems XT_X * coeffs = XT_y
    coeffs = gauss_jordan(XT_X, XT_y)
    
    return coeffs

def gauss_jordan(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    
    for i in range(n):
        # Pivotisierung
        max_row = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[max_row] = M[max_row], M[i]
        
        # Normalisieren der Pivotzeile
        pivot = M[i][i]
        M[i] = [m / pivot for m in M[i]]
        
        # Eliminierung
        for j in range(n):
            if j != i:
                factor = M[j][i]
                M[j] = [m - factor * mi for m, mi in zip(M[j], M[i])]
    
    return [row[-1] for row in M]


def mean(data):
    # Berechnen der Summe der Elemente
    total = sum(data)
    
    # Berechnen der Anzahl der Elemente
    count = len(data)
    
    # Berechnen des Mittelwerts
    return total / count if count != 0 else 0


class Poly1d:
    def __init__(self, *coeffs):
        self.coeffs_list = coeffs

    def __call__(self, x, index=0):
        coeffs = self.coeffs_list[index]
        return sum(c * x**i for i, c in enumerate(reversed(coeffs)))

    def add(self, other, index=0):
        coeffs = self.coeffs_list[index]
        if isinstance(other, Poly1d):
            other_coeffs = other.coeffs_list[index]
        else:
            other_coeffs = other
        new_coeffs = [a + b for a, b in zip(self._pad(coeffs, other_coeffs), self._pad(other_coeffs, coeffs))]
        return Poly1d(new_coeffs)

    def sub(self, other, index=0):
        coeffs = self.coeffs_list[index]
        if isinstance(other, Poly1d):
            other_coeffs = other.coeffs_list[index]
        else:
            other_coeffs = other
        new_coeffs = [a - b for a, b in zip(self._pad(coeffs, other_coeffs), self._pad(other_coeffs, coeffs))]
        return Poly1d(new_coeffs)

    def mul(self, other, index=0):
        coeffs = self.coeffs_list[index]
        if isinstance(other, Poly1d):
            other_coeffs = other.coeffs_list[index]
        else:
            other_coeffs = other
        new_coeffs = [0] * (len(coeffs) + len(other_coeffs) - 1)
        for i, a in enumerate(coeffs):
            for j, b in enumerate(other_coeffs):
                new_coeffs[i + j] += a * b
        return Poly1d(new_coeffs)

    def _pad(self, a, b):
        return a + [0] * (len(b) - len(a))

    def __repr__(self):
        return "Poly1d(" + ", ".join(f"{coeffs}" for coeffs in self.coeffs_list) + ")"


