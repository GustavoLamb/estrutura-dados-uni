from domain import QuadTree, Interval2D, Interval, Point


def test_search(quad_tree: QuadTree, point: Point):
    print(f"Valor encontrado no ponto {point} é: {quad_tree.search(point)}")


def test_allPoints(quad_tree: QuadTree):
    print(f"Valores encontrados: {quad_tree.all_points()}")


def test_query2D(quad_tree: QuadTree) -> None:
    rect: Interval2D = Interval2D(Interval(1, 8), Interval(4, 8))
    quad_tree.query_2D(rect)


if __name__ == '__main__':
    quad_tree: QuadTree = QuadTree()
    m = [[7, 6, 76],
         [5, 6, 56],
         [1, 1, 11],
         [5, 5, 55],
         [2, 7, 27],
         [3, 3, 33]]
    for a in m:
        quad_tree.insert(a[0], a[1], a[2])

    # test_query2D(quad_tree)
    test_search(quad_tree, Point(2, 7))
    test_allPoints(quad_tree)
