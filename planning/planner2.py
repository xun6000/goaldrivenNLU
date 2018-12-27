# coding=utf-8
# !/usr/bin/env python
"""
Example of using PyDDL to solve the "Missionaries and Cannibals" Problem.
A boat must transport a group of 3 missionaries and 3 cannibals across a river,
but at no time can the cannibals outnumber the missionaries at either side of
the river.
"""
from __future__ import print_function
from pyddl import Domain, Problem, Action, neg, planner


def problem2(world):
    domain = Domain((
        Action(
            'askPhone',
            preconditions=(
                ('t', 'start'),
                ('f', 'askPhoneNO'),
            ),
            effects=(
                ('t', 'askPhoneNO'),
            ),
        ),
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
            'close2',
            preconditions=(
                ('t', 'start'),
                ('t', 'askPhoneNO'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'close'),
            ),
        ),
    ))
    init = [
        ('t', 'start'),
        ('f', 'close')
    ]
    goal = (
        ('t', 'close'),
    )
    init.append(('t', 'askPhoneNO')) if world.userProfile.phone > 0 else init.append(('f', 'askPhoneNO'))


    init = tuple(init)
    # print(init)
    problem = Problem(
        domain,
        {},
        init=init,
        goal=goal
    )

    plan = planner(problem)
    return plan
