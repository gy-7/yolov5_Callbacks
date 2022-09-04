from Register.logger import Logger
from Register.callbacks import Callbacks

logger = Logger()
callbacks = Callbacks()


def methods(instance):
    # Get class/instance methods
    return [f for f in dir(instance) if callable(getattr(instance, f)) and not f.startswith("__")]


# Register actions
for k in methods(logger):
    print(k)
    callbacks.register_action(k, callback=getattr(logger, k))
print('-' * 20)

# get all actions
actions = callbacks.get_registered_actions()
print(actions)
print('-' * 20)

# Run all actions
for i in actions.keys():
    callbacks.run(i)
print('-' * 20)

# Run part action
callbacks.run('logger1')
