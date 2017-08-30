from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
import pysrt
import glob

"""
Module for training and executing a chat bot using subtitles files
"""

bot = ChatBot("SubtitlesBot")

def train(subtitles_path):
    """ Train a bot using a set of subtitles files """
    dialogs = []

    print("Preparing training data...")
    files = glob.glob("%s/*.srt" % subtitles_path.rstrip('/'))
    for f in files:
        try:
            subs = pysrt.open(f)
            dialogs = dialogs + list(map(lambda s: s.text, subs))
        except UnicodeDecodeError:
            print("Error decoding file: %s. Files must be encoded in utf-8"
                    % f)
        except Exception:
            print("There were errors processing file: %s" % s)

    print("Training...")
    bot.set_trainer(ListTrainer)
    bot.train(dialogs)

def run():
    """ Run the bot """
    print("Ready. Come on, say something!")

    while True:
        try: 
            text = input("You> ")
            print("Bot> %s" % bot.get_response(text))
        except KeyboardInterrupt:
            print("Bye!")
            break
        except Exception:
            print("Error while processing input. Try again.")

def train_and_run(subtitles_path):
    """ Train and run the bot """
    train(subtitles_path)
    run()
