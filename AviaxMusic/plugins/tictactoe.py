# AviaxMusic/plugins/tictactoe.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext

games = {}

def empty_board():
    return [[" "]*3 for _ in range(3)]

def board_markup(board):
    keyboard = [[InlineKeyboardButton(cell if cell != " " else "⬜", callback_data=f"move_{i}_{j}")
                 for j, cell in enumerate(row)] for i, row in enumerate(board)]
    return InlineKeyboardMarkup(keyboard)

def check_winner(board):
    lines = board + [list(col) for col in zip(*board)] + [
        [board[i][i] for i in range(3)],
        [board[i][2-i] for i in range(3)]
    ]
    for line in lines:
        if line[0] != " " and all(cell == line[0] for cell in line):
            return line[0]
    if all(cell != " " for row in board for cell in row):
        return "Draw"
    return None

async def start_ttt(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    games[chat_id] = {"board": empty_board(), "turn": "❌"}
    await update.message.reply_text("Tic-Tac-Toe started! ❌ goes first.",
                                    reply_markup=board_markup(games[chat_id]["board"]))

async def handle_move(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    info = games.get(query.message.chat_id)
    if not info:
        await query.edit_message_text("No active game. Start with /ttt")
        return
    _, row, col = query.data.split("_")
    row, col = int(row), int(col)
    if info["board"][row][col] != " ":
        return
    info["board"][row][col] = info["turn"]
    winner = check_winner(info["board"])
    if winner:
        text = f"{winner} wins!" if winner != "Draw" else "It's a draw!"
        await query.edit_message_text(text, reply_markup=board_markup(info["board"]))
        del games[query.message.chat_id]
        return
    info["turn"] = "⭕" if info["turn"] == "❌" else "❌"
    await query.edit_message_text(f"Tic-Tac-Toe — Turn: {info['turn']}",
                                  reply_markup=board_markup(info["board"]))

def register_tictactoe(dp):
    dp.add_handler(CommandHandler("ttt", start_ttt))
    dp.add_handler(CallbackQueryHandler(handle_move, pattern="^move_"))
