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


def problem3(world):
    domain = Domain((
        Action(
            'suggestLong',
            preconditions=(
                ('f', 'start'),
            ),
            effects=(
                ('t', 'start'),
            ),
        ),
        Action(
            'askWant',
            preconditions=(
                ('t', 'start'),
                ('f', 'want'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'want'),
                ('t', 'want', 'short_invest'),
                ('t', 'want', 'invest'),
                ('t', 'want', 'insurance'),
                ('t', 'want', 'fund'),
                ('t', 'want', 'plan'),
            ),
        ),
        Action(
            'askTerm',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('f', 'need_term'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'need_term'),
                ('t', 'need_term', 'short'),
                ('t', 'need_term', 'long'),
            ),
        ),
        Action(
            'askMoney',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('f', 'need_money'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'need_money'),
                ('t', 'need_money', 'small'),
                ('t', 'need_money', 'large'),
            ),
        ),
        Action(
            'askRequirement',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('t', 'need_term'),
                ('t', 'need_money'),
                ('t', 'want', 'plan'),
                ('f', 'requirement'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'requirement'),
                ('t', 'requirement', 'house'),
                ('t', 'requirement', 'education'),
            ),
        ),
        Action(
            'suggestPlan',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('f', 'want', 'plan'),
                ('t', 'need_term', 'long'),
                ('t', 'need_money', 'large'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'want', 'plan'),
            ),
        ),
        Action(
            'suggestPlanResult',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('t', 'want', 'plan'),
                ('t', 'need_term'),
                ('t', 'need_money'),
                ('t', 'requirement'),
                ('f', 'suggest'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'suggest'),
            ),
        ),
        Action(
            'suggestShort',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('f', 'want', 'plan'),
                ('f', 'want', 'short_invest'),
                ('t', 'need_term', 'short'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'want', 'short_invest'),
            ),
        ),
        Action(
            'executeShortInvest',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('t', 'want', 'short_invest'),
                ('t', 'need_term', 'short'),
                ('f', 'suggest'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'suggest'),
            ),
        ),
        Action(
            'executeInvest',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('t', 'want', 'invest'),
                ('t', 'need_term', 'long'),
                ('t', 'need_money', 'small'),
                ('f', 'suggest'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'suggest'),
            ),
        ),
        Action(
            'suggestOther',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('f', 'want', 'invest'),
                ('f', 'want', 'plan'),
                ('t', 'need_term', 'long'),
                ('t', 'need_money', 'small'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'want', 'invest'),
            ),
        ),
        Action(
            'close',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
                ('t', 'suggest'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'close'),
            ),
        ),
    ))
    init = [
        ('f', 'start'),
        # ('f', 'want'),
        # ('f', 'want', 'invest'),
        # ('f', 'want', 'short_invest'),
        # ('f', 'want', 'fund'),
        # ('f', 'want', 'insurance'),
        # ('f', 'want', 'plan'),
        # ('f', 'need_term'),
        # ('f', 'need_term', 'short'),
        # ('f', 'need_term', 'long'),
        # ('f', 'need_money'),
        # ('f', 'need_money', 'small'),
        # ('f', 'need_money', 'large'),
        # ('f', 'requirement'),
        # ('f', 'requirement', 'house'),
        # ('f', 'requirement', 'education'),
        ('f', 'close')
    ]
    goal = (
        ('t', 'close'),
    )
    init.append(('t', 'want')) if world.salesProfile.status >= 1 else init.append(('f', 'want'))
    init.append(('t', 'want', 'invest')) if world.salesProfile.userGoal == 1 else init.append(('f', 'want', 'invest'))
    init.append(('t', 'want', 'short_invest')) if world.salesProfile.userGoal == 2 else init.append(
        ('f', 'want', 'short_invest'))
    init.append(('t', 'want', 'fund')) if world.salesProfile.userGoal == 3 else init.append(('f', 'want', 'fund'))
    init.append(('t', 'want', 'insurance')) if world.salesProfile.userGoal == 4 else init.append(
        ('f', 'want', 'insurance'))
    init.append(('t', 'want', 'plan')) if world.salesProfile.userGoal == 5 else init.append(('f', 'want', 'plan'))

    init.append(('t', 'need_term')) if world.userProfile.term > 0 else init.append(('f', 'need_term'))
    init.append(('t', 'need_term', 'short')) if world.userProfile.term == 1 else init.append(
        ('f', 'need_term', 'short'))
    init.append(('t', 'need_term', 'long')) if world.userProfile.term == 2 else init.append(('f', 'need_term', 'long'))
    init.append(('t', 'need_money')) if world.userProfile.money > 0 else init.append(('f', 'need_money'))
    init.append(('t', 'need_money', 'small')) if world.userProfile.money == 1 else init.append(
        ('f', 'need_money', 'small'))
    init.append(('t', 'need_money', 'large')) if world.userProfile.money == 2 else init.append(
        ('f', 'need_mongey', 'large'))

    init.append(('t', 'requirement')) if world.userProfile.purpose > 0 else init.append(('f', 'requirement'))
    init.append(('t', 'requirement', 'house')) if world.userProfile.purpose == 1 else init.append(
        ('f', 'requirement', 'house'))
    init.append(('t', 'requirement', 'education')) if world.userProfile.purpose == 4 else init.append(
        ('f', 'requirement', 'education'))

    init.append(('t', 'suggest')) if world.salesProfile.currentType == 2 and world.salesProfile.yesorno == 1 else init.append(
        ('f', 'suggest'))


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
