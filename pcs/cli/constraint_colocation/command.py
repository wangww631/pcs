from __future__ import (
    absolute_import,
    division,
    print_function,
)

from pcs.cli.constraint import command
from pcs.cli.constraint_colocation import console_report


def create_with_set(lib, argv, modificators):
    """
    create colocation constraint with resource set
    object lib exposes library
    list argv see usage for "constraint colocation set"
    dict like object modificators can contain
        "force" allows resource in clone/master and constraint duplicity
        "autocorrect" allows correct resource to its clone/master parent
    """
    command.create_with_set(
        lib.constraint_colocation.set,
        argv,
        modificators,
    )

def show(lib, argv, modificators):
    """
    show all colocation constraints
    object lib exposes library
    list argv see usage for "constraint colocation show"
    dict like object modificators can contain "full"
    """
    print("\n".join(command.show(
         "Colocation Constraints:",
        lib.constraint_colocation.show,
        console_report.constraint_plain,
        modificators,
    )))
