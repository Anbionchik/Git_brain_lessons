class MeetingGraph:

    def __init__(self, N):
        self.N = N

    def draw_schema(self):
        print(f'   ', end='')
        for i in range(self.N):
            print(f'{(i + 1):>3}', end='')
        print()
        for i in range(self.N):
            print(f'{(i + 1):>3}', end='')
            for j in range(self.N):
                if i == j:
                    print(f'{0:>3}', end='')
                else:
                    print(f'{1:>3}', end='')
            print()

    def count_handshakes(self):
        handshakes = 0
        for i in range(1, self.N):
            handshakes += i
        return handshakes


met = MeetingGraph(10)
met.draw_schema()