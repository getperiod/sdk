def empty(): pass
bindings = dict(
    on_start=empty,
    on_frame=empty,
    on_background=empty
)


def on_start(function): bindings.update({'on_start': function}); return function
def on_tick(function): bindings.update({'on_tick': function}); return function
def on_background(function): bindings.update({'on_background': function}); return function
