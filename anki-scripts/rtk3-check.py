import sys
import sqlite3

'''
This script queries an Anki SQLite3 database and checks
whether any RTK3 kanji that appear in sentence cards
are unsuspended.
'''

if len(sys.argv) == 1:
    print("Usage: python rtk3-check.py <sqlite-db-path>")
    sys.exit()

db = sys.argv[1]
con = sqlite3.connect(db)
cur = con.cursor()

def get_suspended_rtk3_notes():
    # queue -1 means it's suspended
    query = """
        SELECT notes.*
        FROM cards
             inner join notes on cards.nid = notes.id
        WHERE notes.tags like '%RTK3%'
              and cards.queue = -1
        """
    res = cur.execute(query)
    return res.fetchall()

def rtk3_kanji_from(notes):
    string_collection = ""
    kanji_col_index = 7
    for note in notes:
        string_collection = string_collection + note[kanji_col_index]
    return string_collection

def get_sentences():
    query = """
        SELECT sfld
        FROM notes
        WHERE tags like '%Japanese::Sentence%'
        """
    res = cur.execute(query)

    sentences = []
    for tuple in res:
        sentences.append(tuple[0])
    return sentences

def main():
    rtk3_notes = get_suspended_rtk3_notes()
    rtk3_kanji = rtk3_kanji_from(rtk3_notes)
    sentence_collection = get_sentences()

    result = []
    for sentence in sentence_collection:
        for kanji in rtk3_kanji:
            if kanji in sentence:
                result.append((kanji, sentence))

    print(result)

if __name__ == "__main__":
    main()