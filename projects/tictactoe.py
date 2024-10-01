import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.turn = "X"
        self.board = [""] * 9
        self.score_x = 0
        self.score_o = 0
        self.move_count_x = 0
        self.move_count_o = 0

        
        # Score labels
        self.score_label = tk.Label(root, text=f"Player X: {self.score_x}  Player O: {self.score_o}", font=('Arial', 16))
        self.score_label.grid(row=1, column=0, columnspan=3)

        # Move count labels
        self.move_count_label = tk.Label(root, text=f"Moves - Player X: {self.move_count_x}  Player O: {self.move_count_o}", font=('Arial', 16))
        self.move_count_label.grid(row=2, column=0, columnspan=3)

        # Create buttons
        self.buttons = [tk.Button(root, text="", font=('Arial', 24), width=5, height=2,
                                   command=lambda i=i: self.on_button_click(i)) for i in range(9)]
        
        for i, button in enumerate(self.buttons):
            button.grid(row=(i // 3) + 3, column=i % 3, padx=10, pady=10, sticky='nsew')

        # Configure grid weights
        for i in range(3):
            root.grid_rowconfigure(i + 3, weight=1)
            root.grid_columnconfigure(i, weight=1)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", font=('Arial', 16), command=self.reset_game)
        self.reset_button.grid(row=6, column=0, columnspan=3, pady=10)

    def on_button_click(self, i):
        if self.board[i] == "":
            self.board[i] = self.turn
            self.buttons[i].config(text=self.turn)

            # Update move count
            if self.turn == "X":
                self.move_count_x += 1
            else:
                self.move_count_o += 1

            self.update_move_count()

            if self.check_winner():
                if self.turn == "X":
                    self.score_x += 1
                else:
                    self.score_o += 1
                self.update_score()
                messagebox.showinfo("Tic Tac Toe", f"Player {self.turn} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def update_score(self):
        self.score_label.config(text=f"Player X: {self.score_x}  Player O: {self.score_o}")

    def update_move_count(self):
        self.move_count_label.config(text=f"Moves - Player X: {self.move_count_x}  Player O: {self.move_count_o}")

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.turn = "X"
        self.move_count_x = 0
        self.move_count_o = 0
        self.update_move_count()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
