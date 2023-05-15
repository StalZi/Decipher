def character_limit1(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:1])

def character_limit3(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:3])