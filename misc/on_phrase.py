from talon import speech_system, actions


def on_phrase(phrase):
    if not actions.speech.enabled() or not phrase.get("phrase"):
        return

    is_aborted, text = actions.user.abort_phrase(phrase)

    if not is_aborted:
        is_sleep, text = actions.user.talon_sleep_update_phrase(phrase)

    analyzed_phrase = actions.user.analyze_phrase(phrase)
    analyzed_phrase = actions.user.calc_analyzed_phrase_with_actions(analyzed_phrase)

    if text:
        actions.user.subtitle(text)
        actions.user.print_phrase_timings(phrase, text)
        actions.user.command_history_append(analyzed_phrase)
        actions.user.pretty_print_phrase(analyzed_phrase)


speech_system.register("phrase", on_phrase)
