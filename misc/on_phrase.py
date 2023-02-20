from talon import speech_system, actions


def on_phrase(phrase):
    if not actions.speech.enabled():
        return

    if not phrase.get("phrase"):
        return

    is_aborted, text = actions.user.abort_phrase(phrase)

    if not is_aborted:
        is_sleep, text = actions.user.talon_sleep_update_phrase(phrase)

    sim_commands = actions.user.simulate_phrase(phrase)

    if text:
        actions.user.subtitle(text)
        actions.user.command_history_append(sim_commands)
        actions.user.pretty_print_phrase(text, sim_commands)
        actions.user.print_phrase_timings(phrase, text)


speech_system.register("phrase", on_phrase)
