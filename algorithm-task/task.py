from collections import defaultdict


def graph_build(net):
    graph = defaultdict(set)

    for connection in net:
        graph[connection[0]].add(connection[1])
        graph[connection[1]].add(connection[0])

    return graph


def check_relation(net, first, second, visited=None):
    if not visited:
        visited = set()

    visited.add(first)

    for next in net[first] - visited:
        check_relation(net, next, second, visited)

    if second in visited:
        return True

    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    net = graph_build(net)

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
