from typing import Optional, List
import actions

valid_yes = ["y", "yes", "yup"]
valid_no = ["n", "no", "nope"]


def yes_or_no(prompt):
    print(f"{prompt}")
    user_input = input(">> Decision (Y or N): ").lower().strip()
    if user_input in valid_yes:
        return True
    elif user_input in valid_no:
        return False
    else:
        print(f"{user_input} was not a valid option; defaulting to no")
        return False


def prompt_and_respond(
        player,
        available_actions: List,
        title_prompt: Optional[str] = None,
        action_prompt: Optional[str] = None
):
    if not title_prompt:
        title_prompt = "Choose an action:\n"
    if not action_prompt:
        action_prompt = ">> Action: "

    action_list = "\n\t".join(str(action) for action in available_actions)
    print(f"{title_prompt}\t{action_list}")

    action_input = input(f"\n{action_prompt}").lower()

    for action in available_actions:
        if action.match_input(user_input=action_input):
            if isinstance(action, actions.SideEffect):
                action()
                break
            else:
                player.do_action(action, **action.kwargs)
                break
