import math


def entropy(xs_: dict | list):
    """ Считает энтропию по заданному распределению вероятностей """

    result = 0.0

    if type(xs_) == dict:
        for key_ in xs_:
            result -= xs_[key_] * math.log(xs_[key_], 2)
    elif type(xs_) == list:
        for x_ in xs_:
            result -= x_ * math.log(x_, 2)

    return result


def get_z(xs_, ys_):
    """ Строит распределение Z """

    zs_ = dict()

    for key_x_ in xs_:
        for key_y_ in ys_:
            key_z_ = (key_x_ - key_y_) ** 2
            if key_z_ in zs_:
                zs_[key_z_] += xs_[key_x_] * ys_[key_y_]
            else:
                zs_[key_z_] = xs_[key_x_] * ys_[key_y_]

    return zs_


X = {-2: 1/5, -1: 1/5, 0: 3/10, 1: 3/10}
Y = {0: 1/5, 1: 4/5}

h_x = entropy(X)
print(f'{h_x=}')

h_y = entropy(Y)
print(f'{h_y=}')

Z = get_z(X, Y)
print(f'{Z=}')

h_z = entropy(Z)
print(f'{h_z=}')

h_z_by_x = h_y
print(f'{h_z_by_x=}')

h_z_by_y = (0.2 * entropy([1/25/0.2, 1/25/0.2 + 3/50/0.2, 3/50/0.2]) +
            0.8 * entropy([4/25/0.8, 4/25/0.8, 15/50/0.8, 15/50/0.8]))
print(f'{h_z_by_y=}')

h_x_z = h_x + h_z_by_x
print(f'{h_x_z=}')

h_y_z = h_y + h_z_by_y
print(f'{h_y_z=}')

i_y_z = i_z_y = h_z - h_z_by_y
print(f'{i_y_z=}')

i_x_z = i_z_x = h_z - h_z_by_x
print(f'{i_x_z=}')

h_x_by_z = h_x - i_x_z
print(f'{h_x_by_z=}')

h_y_by_z = h_y - i_y_z
print(f'{h_y_by_z=}')

# Вторая задача
print()

h_z_by_x_2 = 0.8 * entropy([0.4, 0.3, 0.3]) + 0.2 * entropy([0.5, 0.5])
print(f'{h_z_by_x_2=}')

p_1 = 0.8*0.3 / (0.8*0.3 + 0.2*0.5)
p_2 = 0.2*0.5 / (0.8*0.3 + 0.2*0.5)

print(f'{p_1=}')
print(f'{p_2=}')

net = entropy([p_1, p_2])
print(net)
