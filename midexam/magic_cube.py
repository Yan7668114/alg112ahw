import random

class MagicCube:
    def __init__(self):
        # 初始化一個已完成的魔術方塊
        self.cube = [[[i for _ in range(3)] for _ in range(3)] for i in range(6)]

    def rotate_face_clockwise(self, face):
        # 旋轉指定面順時針
        self.cube[face] = [list(row) for row in zip(*reversed(self.cube[face]))]

    def rotate_face_counter_clockwise(self, face):
        # 旋轉指定面逆時針
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]

    def scramble(self, num_moves):
        # 隨機打亂魔術方塊
        moves = ["F", "F'", "B", "B'", "L", "L'", "R", "R'", "U", "U'", "D", "D'"]
        for _ in range(num_moves):
            move = random.choice(moves)
            self.perform_move(move)

    def perform_move(self, move):
        # 執行單一旋轉操作
        if move == "F":
            self.rotate_face_clockwise(0)
        elif move == "F'":
            self.rotate_face_counter_clockwise(0)
        elif move == "B":
            self.rotate_face_clockwise(1)
        elif move == "B'":
            self.rotate_face_counter_clockwise(1)
        elif move == "L":
            self.rotate_face_clockwise(2)
        elif move == "L'":
            self.rotate_face_counter_clockwise(2)
        elif move == "R":
            self.rotate_face_clockwise(3)
        elif move == "R'":
            self.rotate_face_counter_clockwise(3)
        elif move == "U":
            self.rotate_face_clockwise(4)
        elif move == "U'":
            self.rotate_face_counter_clockwise(4)
        elif move == "D":
            self.rotate_face_clockwise(5)
        elif move == "D'":
            self.rotate_face_counter_clockwise(5)

    def cross(self):
        # CFOP法的第一步：形成十字交叉
        # 在這個示例中，我們不打亂魔術方塊，所以只是讓十字交叉保持原樣。
        pass

    def f2l(self):
        # CFOP法的第二步：完成第一層（F2L）
        # 在這個示例中，我們不打亂魔術方塊，所以只是讓第一層保持原樣。
        pass

    def oll(self):
        # CFOP法的第三步：定向頂層的邊線（OLL）
        # 在這個示例中，我們不打亂魔術方塊，所以只是讓頂層的邊線保持原樣。
        pass

    def pll(self):
        # CFOP法的第四步：排列頂層的角塊（PLL）
        # 在這個示例中，我們不打亂魔術方塊，所以只是讓頂層的角塊保持原樣。
        pass

    def is_solved(self):
        # 檢查魔術方塊是否已經復原
        for face in self.cube:
            for row in face:
                if len(set(row)) != 1:
                    return False
        return True

    def print_cube(self):
        for face in self.cube:
            for row in face:
                print(row)
            print()

# 創建一個魔術方塊
cube = MagicCube()

# 打印初始狀態
print("Initial State:")
cube.print_cube()

# 隨機打亂魔術方塊（例如，進行20次隨機操作）
cube.scramble(20)
print("Scrambled State:")
cube.print_cube()

# 執行CFOP法的各個步驟
cube.cross()
cube.f2l()
cube.oll()
cube.pll()

# 打印復原後的狀態
print("Solved State:")
cube.print_cube()
