def increment(data=[1, 2, 3]):
    for i in range(len(data)):
        data[i] += 1
    return data


def decrement(data=[1, 2, 3]):
    return [data[i] - 1 for i in range(len(data))]


def add(data=[1, 2, 3], value=1):
    for i in range(len(data)):
        data[i] += value


def subtract(data=[1, 2, 3], value=1):
    for i in range(len(data)):
        data[i] -= value


def multiply(data=[1, 2, 3], value=1):
    for i in range(len(data)):
        data[i] *= value


def divide(data=[1, 2, 3], value=1):
    return [data[i] / value for i in range(len(data))]


def extend(data=[1, 2, 3], extend_data=[1, 2, 3]):
    return data.extend(extend_data)


if __name__ == "__main__":
    data = increment()
    print(data)
    increment()
    print(data)
    decrement(data)
    print(data)
    subtract(data, value=2)
    print(data)
    multiply(data, value=2)
    print(data)
    data = extend(data=data)
    print(data)
    extend(data)
    print(data)
