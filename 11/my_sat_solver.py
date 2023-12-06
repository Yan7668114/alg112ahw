from pysat.solvers import Glucose3

def solve_sat_problem():
    # 創建一個SAT求解器
    solver = Glucose3()

    # 創建一個簡單的SAT問題：(A OR ~B) AND (B OR C) AND (A OR C)
    solver.add_clause([1, -2])
    solver.add_clause([2, 3])
    solver.add_clause([1, 3])

    # 求解SAT問題
    if solver.solve():
        print("滿足性解存在:")
        print("變數A:", solver.get_model()[0] > 0)
        print("變數B:", solver.get_model()[1] > 0)
        print("變數C:", solver.get_model()[2] > 0)
    else:
        print("沒有滿足性解存在")

if __name__ == "__main__":
    solve_sat_problem()
