import os
import pandas as pd
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

file_path = 'all_words.csv'

def load_words():
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        df = pd.read_csv(file_path)
        return df['word'].tolist()
    return []

def save_words(words):
    df = pd.DataFrame({"word": words})
    df.to_csv(file_path, index=False)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.bot_data.clear()
    open(file_path, "w").close()

    context.bot_data['teams'] = {}
    context.bot_data['turn_order'] = []
    context.bot_data['current_turn'] = 0
    context.bot_data['chosen_letter'] = None

    await update.message.reply_text(
        "Гру почато! Кожен гравець має ввести команду через /join <назва_команди>\n"
        "Після того, як приєднається 2 і більше команд, хтось задасть букву для гри"
    )

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if 'teams' not in context.bot_data:
        context.bot_data['teams'] = {}
        context.bot_data['turn_order'] = []
        context.bot_data['current_turn'] = 0

    if user_id in context.bot_data['teams']:
        await update.message.reply_text("Ви вже приєдналися до гри")
        return

    if len(context.args) < 1:
        await update.message.reply_text("Використання: /join <назва_команди>")
        return

    team_name = ' '.join(context.args)
    context.bot_data['teams'][user_id] = team_name
    context.bot_data['turn_order'].append(user_id)

    await update.message.reply_text(f"Ваша команда '{team_name}' зареєстрована!")

    if len(context.bot_data['teams']) >= 2:
        await update.message.reply_text(
            "Тепер хтось з гравців може ввести одну букву, яка буде спільною для гри"
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_text = update.message.text.strip().lower()

    teams = context.bot_data.get('teams', {})
    if user_id not in teams:
        await update.message.reply_text("Ви не приєдналися до гри. Введіть /join <назва_команди>")
        return


    if context.bot_data.get('chosen_letter') is None:
        if len(user_text) == 1 and user_text.isalpha():
            context.bot_data['chosen_letter'] = user_text
            context.bot_data['team_words'] = {}
            current_team_id = context.bot_data['turn_order'][context.bot_data['current_turn']]
            current_team_name = context.bot_data['teams'][current_team_id]
            await update.message.reply_text(
                f"Буква '{user_text.upper()}' вибрана! Першою ходить команда '{current_team_name}'"
            )
        else:
            await update.message.reply_text("Спочатку потрібно вибрати одну букву ")
        return


    turn_order = context.bot_data['turn_order']
    current_turn = context.bot_data['current_turn']
    current_player_id = turn_order[current_turn]

    if user_id != current_player_id:
        await update.message.reply_text("Зараз не ваша черга. Будь ласка, зачекайте.")
        return

    if user_text == "доста":
        stats = "🏁 Результати гри:\n"
        team_words = context.bot_data.get('team_words', {})
        for team_id, team_name in context.bot_data['teams'].items():
            words = team_words.get(team_id, [])
            stats += f"— {team_name}: {len(words)} слів\n"

        await update.message.reply_text(stats)


        context.bot_data.clear()
        open(file_path, "w").close()
        return

    chosen_letter = context.bot_data['chosen_letter']
    word_list = [w for w in load_words() if w.lower().startswith(chosen_letter)]

    if not user_text.startswith(chosen_letter):
        await update.message.reply_text(f"Слово має починатися з букви '{chosen_letter.upper()}'.")
        return

    if user_text in [w.lower() for w in word_list]:
        await update.message.reply_text("Це слово вже було.")
        return


    all_words = load_words()
    all_words.append(user_text)
    save_words(all_words)


    team_words = context.bot_data.setdefault('team_words', {})
    team_words.setdefault(user_id, []).append(user_text)

    context.bot_data['current_turn'] = (current_turn + 1) % len(turn_order)
    next_player_id = turn_order[context.bot_data['current_turn']]
    next_team_name = context.bot_data['teams'][next_player_id]

    await update.message.reply_text(f"Слово прийнято. Наступна команда: {next_team_name}")

def main():
    TOKEN = ""

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущено...")
    app.run_polling()

if __name__ == "__main__":
    main()
