import streamlit as st

# Define the game board
if 'board' not in st.session_state:
    st.session_state.board = [[None for _ in range(3)] for _ in range(3)]
if 'current_player' not in st.session_state:
    st.session_state.current_player = "X"
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'winner' not in st.session_state:
    st.session_state.winner = None

def switch_player():
    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

def check_win():
    board = st.session_state.board
    current_player = st.session_state.current_player

    # Check rows and columns
    for i in range(3):
        if all([cell == current_player for cell in board[i]]) or \
           all([board[j][i] == current_player for j in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == current_player for i in range(3)]) or \
       all([board[i][2-i] == current_player for i in range(3)]):
        return True

    return False

def handle_click(row, col):
    if st.session_state.board[row][col] is None and not st.session_state.game_over:
        st.session_state.board[row][col] = st.session_state.current_player
        if check_win():
            st.session_state.game_over = True
            st.session_state.winner = st.session_state.current_player
        else:
            switch_player()

def reset_game():
    st.session_state.board = [[None for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

def main():
    st.title("Tic Tac Toe")
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            height: 100px;
            font-size: 24px;
            font-weight: bold;
            color: white;
            border: 2px solid #4CAF50;
        }
        @media (max-width: 600px) {
            .stButton>button {
                height: 80px;
                font-size: 20px;
            }
        }
        @media (max-width: 400px) {
            .stButton>button {
                height: 60px;
                font-size: 16px;
            }
        }
        .win-message {
            font-size: 24px;
            color: #2a9d8f;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if st.button("Restart Game"):
        reset_game()

    st.write(f"Current Player: {'❌' if st.session_state.current_player == 'X' else '⭕'}")

    for row in range(3):
        cols = st.columns([1, 1, 1])
        for col in range(3):
            button_text = st.session_state.board[row][col] or ""
            if button_text == "X":
                display_text = "❌"
            elif button_text == "O":
                display_text = "⭕"
            else:
                display_text = ""

            cols[col].button(display_text, key=f"{row}_{col}", on_click=handle_click, args=(row, col))

    if st.session_state.game_over:
        st.markdown(f"<div class='win-message'>{st.session_state.winner} wins!</div>", unsafe_allow_html=True)
    elif all(all(cell is not None for cell in row) for row in st.session_state.board):
        st.markdown("<div class='win-message'>It's a draw!</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
