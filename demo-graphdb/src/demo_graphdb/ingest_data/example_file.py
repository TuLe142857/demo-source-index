from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search (BFS)

    graph: dict
        Đồ thị dạng danh sách kề.
    start:
        Đỉnh bắt đầu.
    """
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("Thứ tự duyệt BFS:")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print()


def main():
    # Ví dụ đồ thị
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start = input("Nhập đỉnh bắt đầu: ").strip().upper()

    if start not in graph:
        print("Đỉnh không tồn tại!")
        return

    bfs(graph, start)


if __name__ == "__main__":
    main()