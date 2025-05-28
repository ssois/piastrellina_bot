import os
import random
from keep_alive import keep_alive
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

keep_alive()

# Define keyword variants and responses
keyword_responses = {
    "Giorgio": {
        "variants": [
            "giorgio", "piastrellina", "pazzo", "malato", "schizofrenico", "oligofrenico"
        ],
        "responses": [
            "Io ho la conoscenza.", "Cosa ne potete capire voi.", "Cosa ve lo dico a fare."
        ]
    },
    "Alieni": {
        "variants": [
            "alieni", "arconti", "fantasmi", "ologrammi", "pleiadiani", "rettiliani"
        ],
        "responses": [
            "Trump è un alieno, io lo so.",
            "Macron è parente di un arconte, voi non lo sapete",
            "I fantasmi esistono veramente. Per esempio da poco ho visto Baudo in tv.",
            "I miei figli sono degli ologrammi, ma li amo lo stesso.",
            "Siete tutti rettiliani!"
        ]
    },
    "Cospirazione": {
        "variants": [
            "bilderberg", "cospirazione", "covid", "frequenze", "terra cava", "terra piatta", "vite"
        ],
        "responses": [
            "Io ho 800 vite.", "Io esisto dalla notte dei tempi.",
            "Io vedo le verità nascoste",
            "Io conosco le frequenze. 103.3 è Isoradio, per dire.",
            "Il gruppo Bilderberg si riunisce a Chiuppano ogni luna piena.",
            "La terra è piatta, ed al tempo stesso è cava. E' piena di gnomi piccoli piccoli.",
            "Io assorbo la conoscenza astrale attraverso un complicato sistema di clisteri ed antenne.",
            "Prima del Conad-19 non moriva nessuno d'infarto. Ora muoiono come mosche.",
            "In Veneto non moriva nessuno d'infarto. Cirrosi, tumori al buco del culo, Pietro Maso sì. Ma infarto no."
        ]
    }
}


# Async reply handler
async def reply_to_keywords(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return  # Ignore non-text or system messages

    text = update.message.text.lower()
    for key, value in keyword_responses.items():
        if any(variant in text for variant in value["variants"]):
            if random.random() < 0.50:  # 50% chance
                response = random.choice(value["responses"])
                await update.message.reply_text(response)
            return


# Create app and run (no asyncio.run)
def main():
    application = Application.builder().token(os.environ["BOT_TOKEN"]).build()
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_keywords))
    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
