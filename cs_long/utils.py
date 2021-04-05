valid_yes = ["y", "yes", "yup"]
valid_no = ["n", "no", "nope"]


def yes_or_no(prompt):
    user_input = input(f"{prompt} -- (Y or N)").lower().strip()
    if user_input in valid_yes:
        return True
    elif user_input in valid_no:
        return False
    else:
        print(f"{user_input} was not a valid option; defaulting to no")
        return False


def prompt_and_respond(player, actions, title_prompt=None, action_prompt=None):
    if not title_prompt:
        title_prompt="Choose an action:\n"
    if not action_prompt:
        action_prompt="Action: "

    print(title_prompt)

    for action in actions:
        print(action)

    action_input = input(action_prompt).lower()

    for action in actions:
        if action.match_input(action_input):
            player.do_action(action, **action.kwargs)
            break