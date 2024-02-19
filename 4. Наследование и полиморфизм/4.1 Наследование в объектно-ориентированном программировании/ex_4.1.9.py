class Layer(object):
    """docstring for Layer."""

    def __init__(self, name="Layer"):
        super(Layer, self).__init__()
        self.name = name
        self.next_layer = None

    def __call__(self, layer):
        self.next_layer = layer
        return self.next_layer


class Input(Layer):
    """docstring for Input."""

    def __init__(self, inputs):
        super(Input, self).__init__("Input")
        self.inputs = inputs


class Dense(Layer):
    """docstring for Dense."""

    def __init__(self, inputs, outputs, activation):
        super(Dense, self).__init__("Dense")
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator(object):
    """docstring for NetworkIterator."""

    def __init__(self, network):
        super(NetworkIterator, self).__init__()
        self.network = network

    def __iter__(self):
        self.top = self.network
        return self

    def __next__(self):
        if self.top:
            tmp = self.top
            self.top = self.top.next_layer
            return tmp
        else:
            raise StopIteration


nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, "relu"))
layer = layer(Dense(layer.inputs, 2048, "relu"))
layer = layer(Dense(layer.inputs, 10, "softmax"))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(
        x, Layer
    ), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"
