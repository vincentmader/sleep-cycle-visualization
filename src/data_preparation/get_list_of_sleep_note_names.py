def get_list_of_sleep_note_names(nights):
    out = []
    for night in nights:
        notes = night.sleep_notes
        for note in notes:
            if note not in out:
                out.append(note)
    return out
