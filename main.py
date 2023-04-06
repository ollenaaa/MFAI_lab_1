import random
import math

n = int(input("Введіть кількість шахових ферзей "))


class chess_board:

    # функція початкової ініціалізації
    def initialize_solution(self, solution):
        for i in range(n):
            solution[i] = i
        return solution

    # функція випадкової зміни розв'язку
    def get_new_solution(self, solution):
        new_solution = list(solution)
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        while new_solution[i] == j:
            j = random.randint(0, n - 1)
        new_solution[i] = j
        return tuple(new_solution)

    # функція копіювання одного розв'язку в інший
    def copy_solution(self, current_solution, current_energy):
        new_solution = current_solution
        new_energy = current_energy
        return new_solution, new_energy

    # функція для оцінки розв'язку
    def get_energy(self, solution):
        conflicts = 0
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                if solution[i] == solution[j] or abs(i - j) == abs(solution[i] - solution[j]):
                    conflicts += 1
        return conflicts

    # функція для виводу результату
    def emit_solution(self, solution):
        board = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            board[i][solution[i]] = 1
        for i in range(n):
            print(board[i])


def simulated_annealing(initial_temperature, final_temperature, cooling_rate, iterations):
    board = chess_board()
    current_solution = [0] * n
    board.initialize_solution(current_solution)
    current_energy = board.get_energy(current_solution)
    best_solution = current_solution
    best_energy = current_energy
    while initial_temperature > final_temperature:
        for i in range(iterations):
            new_solution = board.get_new_solution(current_solution)
            new_energy = board.get_energy(new_solution)
            energy_delta = new_energy - current_energy
            if energy_delta < 0 or random.random() < math.exp(-energy_delta / initial_temperature):
                current_solution, current_energy = board.copy_solution(new_solution, new_energy)
            if current_energy < best_energy:
                best_solution, best_energy = board.copy_solution(current_solution, current_energy)
        initial_temperature *= cooling_rate
    board.emit_solution(best_solution)
    return best_solution


solution = simulated_annealing(40, 0.01, 0.97, 100)