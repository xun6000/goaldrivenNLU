#!/usr/bin/env python
"""
Example of using PyDDL to solve the "Missionaries and Cannibals" Problem.
A boat must transport a group of 3 missionaries and 3 cannibals across a river,
but at no time can the cannibals outnumber the missionaries at either side of
the river.
"""

# state parameter:
# start want need_term need_money requirement plan recommend close
# term_short term_long money_large money_small fund insurance invest

from __future__ import print_function
from pyddl import Domain, Problem, Action, neg, planner


def problem(verbose):
    domain = Domain((
        Action(
            'askPhone',
            preconditions=(
                ('t', 'start'),
                ('t', 'want'),
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
                ('t', 'askPhoneNO'),
                ('f', 'close'),
            ),
            effects=(
                ('t', 'close'),
            ),
        ),
    ))
    init = (
        ('t', 'start'),
        ('f', 'suggest'),
        ('f', 'close'),
        ('t', 'want'),
        ('f', 'want', 'fund'),
        ('f', 'want', 'insurance'),
        ('t', 'want', 'invest'),
        ('f', 'want', 'short_invest'),
        ('f', 'want', 'plan'),
        ('t', 'need_term'),
        ('f', 'need_term', 'short'),
        ('t', 'need_term', 'long'),
        ('t', 'need_money'),
        ('f', 'need_money', 'small'),
        ('t', 'need_money', 'large'),
        ('t', 'requirement'),
        ('t', 'requirement', 'house'),
        ('f', 'requirement', 'education'),
        ('t', 'replan'),
        ('f', 'askPhoneNO'),
    )

    problem = Problem(
        domain,
        {
            # 'brick': ('want', 'need_term', 'need_money', 'requirement'),
            # 'state': ('fund', 'insurance', 'invest', 'short_invest', 'plan', 'short', 'long', 'small', 'large', 'house', 'pension', 'education', 'marriage'),
            # 'product': ('short_small', 'short_large', 'long_small', 'long_large', 'insurance', 'fund1', 'fund2'),
        },
        init=init,
        goal=(
            # ('t', 'start'),
            ('t', 'close'),
        )
    )

    plan = planner(problem, verbose=verbose)
    if plan is None:
        print('No Plan!')
    else:
        for action in plan:
            print(action)


if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser(usage="Usage: %prog [options]")
    parser.add_option('-q', '--quiet',
                      action='store_false', dest='verbose', default=True,
                      help="don't print statistics to stdout")

    # Parse arguments
    opts, args = parser.parse_args()
    problem(opts.verbose)
