from __future__ import print_function
from pyddl import Domain, Problem, Action, planner


def problem1(world):
    domain = Domain((
        Action(
            'start',
            preconditions=(
                ('f', 'start'),
            ),
            effects=(
                ('t', 'start'),
            ),
        ),
        Action(
            'opening',
            preconditions=(
                ('t', 'start'),
                ('f', 'sizeConfirmation'),
                ('f', 'timeConfirmation'),
                ('t', 'doneWaiting'),
                ('t', 'reason'),
                ('f', 'bar'),
                ('f', 'confirm'),
                ('f', 'sayThanks'),
                ('f', 'doubleConfirm')
            ),
            effects=(
                ('t', 'sizeConfirmation'),
                ('t', 'timeConfirmation'),
                ('t', 'sayThanks'),
            ),
        ),

        Action(
            'tableFor2',
            preconditions=(
                ('t', 'start'),
                ('f', 'sizeConfirmation'),
                ('t', 'timeConfirmation'),
                ('f', 'tableFor2')
            ),
            effects=(
                ('t', 'tableFor2'),
                ('t', 'sayThanks'),
            ),
        ),

        Action(
            'combineTables',
            preconditions=(
                ('t', 'start'),
                ('t', 'tableFor2'),
                ('f', 'sizeConfirmation'),
                ('f', 'confirm'),
                ('t', 'timeConfirmation'),
                ('f', 'bar'),
                ('f', 'biggerTable'),
            ),
            effects=(
                ('t', 'sizeConfirmation'),
                ('t', 'sayThanks'),
            ),
        ),

        Action(
            'changeTime',
            preconditions=(
                ('t', 'start'),
                ('f', 'timeConfirmation'),
                ('t', 'sizeConfirmation'),
                ('f', 'askForAlternative'),
                ('f', 'confirm'),
            ),
            effects=(
                ('t', 'timeConfirmation'),
                ('t', 'sayThanks'),
            ),
        ),

        Action(
            'changeRestaurant',
            preconditions=(
                ('t', 'start'),
                ('t', 'changeRestaurant'),
            ),
            effects=(
                ('t', 'confirm'),
            ),
        ),

        Action(
            'tentativelyReserve',
            preconditions=(
                ('t', 'start'),
                ('t', 'tentativelyReserve'),
                ('t', 'timeConfirmation'),
                ('t', 'sizeConfirmation'),
            ),
            effects=(
                ('t', 'callBackLater'),
            ),
        ),

        Action(
            'askForAlternatives',
            preconditions=(
                ('t', 'start'),
                ('t', 'askForAlternative'),
            ),
            effects=(
                ('t', 'confirm'),
            ),
        ),

        Action(
            'askForReason',
            preconditions=(
                ('t', 'start'),
                ('f', 'sizeConfirmation'),
                ('f', 'timeConfirmation'),
                ('f', 'confirm'),
                ('f', 'reason')
            ),
            effects=(
                ('t', 'reason'),
                ('t', 'sizeConfirmation'),
                ('t', 'timeConfirmation'),
                ('t', 'sayThanks'),
            ),
        ),

        Action(
            'sitAtBar',
            preconditions=(
                ('t', 'start'),
                ('t', 'timeConfirmation'),
                ('f', 'sizeConfirmation'),
                ('f', 'confirm'),
                ('t', 'bar'),
            ),
            effects=(
                ('t', 'sizeConfirmation'),
                ('t', 'sayThanks'),
            ),
        ),

        Action(
            'callBackLater',
            preconditions=(
                ('t', 'start'),
                ('t', 'callBackLater'),
            ),
            effects=(
                ('t', 'confirm'),
            ),
        ),

        Action(
            'wait',
            preconditions=(
                ('t', 'start'),
                ('t', 'timeConfirmation'),
                ('t', 'sizeConfirmation'),
                ('f', 'confirm'),
                ('f', 'doneWaiting')
            ),
            effects=(
                ('t', 'doneWaiting'),
                ('t', 'sayThanks'),
            ),
        ),

        Action(
            'askForBiggerTable',
            preconditions=(
                ('t', 'start'),
                ('t', 'biggerTable'),
                ('t', 'timeConfirmation'),
                ('f', 'sizeConfirmation'),
            ),
            effects=(
                ('t', 'sizeConfirmation'),
                ('t', 'sayThanks'),
            ),
        ),

        Action(
            'sayName',
            preconditions=(
                ('t', 'start'),
                ('t', 'name')
            ),
            effects=(
                ('t', 'confirm'),
            ),
        ),

        Action(
            'doubleConfirm',
            preconditions=(
                ('t', 'start'),
                ('t', 'timeConfirmation'),
                ('t', 'sizeConfirmation'),
                ('f', 'tentativelyReserve'),
                ('f', 'confirm'),
                ('t', 'doubleConfirm'),
                ('t', 'doneWaiting'),
            ),
            effects=(
                ('t', 'confirm'),
            ),
        ),


        Action(
            'sayThanks',
            preconditions=(
                ('t', 'sayThanks'),
                ('t', 'start'),
                ('t', 'timeConfirmation'),
                ('t', 'sizeConfirmation'),
                ('f', 'tentativelyReserve'),
                ('f', 'confirm'),
                ('t', 'doneWaiting'),
            ),
            effects=(
                ('t', 'confirm'),
            ),
        ),

        Action(
            'close',
            preconditions=(
                ('t', 'confirm'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'close'),
            ),
        ),
    ))

    init = [
        ('f', 'close'),
    ]
    goal = (
        ('t', 'timeConfirmation'),
        ('t', 'sizeConfirmation'),
        ('t', 'close'),
    )
    init.append(('t', 'start')) if world.dialog.status >= 1 else init.append(('f', 'start'))

    init.append(('t', 'size_user'))
    init.append(('t', 'time_user'))

    if world.dialog.status == 6.1:
        init.append(('t', 'askForAlternative'))
    else:
        init.append(('f', 'askForAlternative'))

    if world.dialog.status == 6:
        init.append(('t', 'changeRestaurant'))
    else:
        init.append(('f', 'changeRestaurant'))

    if world.humanSlot.size > 0 and world.humanSlot.size == world.robotSlot.size:
        init.append(('t', 'sizeConfirmation'))
    else:
        init.append(('f', 'sizeConfirmation'))

    if len(world.humanSlot.time) > 0 and world.humanSlot.time == world.robotSlot.time:
        init.append(('t', 'timeConfirmation'))
    else:
        init.append(('f', 'timeConfirmation'))

    if world.dialog.status == 3:
        init.append(('f', 'doneWaiting'))
    else:
        init.append(('t', 'doneWaiting'))

    if world.dialog.status == 4.9:
        init.append(('t', 'name'))
    else:
        init.append(('f', 'name'))

    if world.dialog.status == 7:
        init.append(('t', 'callBackLater'))
    else:
        init.append(('f', 'callBackLater'))

    if world.dialog.status == 5:
        init.append(('t', 'sayThanks'))
    else:
        init.append(('f', 'sayThanks'))

    if world.dialog.status == 8:
        init.append(('t', 'confirm'))
    else:
        init.append(('f', 'confirm'))

    if world.dialog.status == 1.1:
        init.append(('f', 'reason'))
    else:
        init.append(('t', 'reason'))

    if world.dialog.status == 4.1:
        init.append(('t', 'biggerTable'))
    else:
        init.append(('f', 'biggerTable'))

    if world.dialog.status == 9:
        init.append(('t', 'askForAlternative'))
    else:
        init.append(('f', 'askForAlternative'))

    if world.dialog.status == 4.12:
        init.append(('t', 'bar'))
    else:
        init.append(('f', 'bar'))

    if world.dialog.status == 4.2:
        init.append(('f', 'tableFor2'))
    else:
        init.append(('t', 'tableFor2'))

    if world.dialog.status == 5.1:
        init.append(('t', 'tentativelyReserve'))
    else:
        init.append(('f', 'tentativelyReserve'))

    if world.dialog.status == 5.2:
        init.append(('t', 'doubleConfirm'))
    else:
        init.append(('f', 'doubleConfirm'))

    init = tuple(init)

    problem = Problem(
        domain,
        {},
        init=init,
        goal=goal
    )

    plan = planner(problem)
    return plan, init
