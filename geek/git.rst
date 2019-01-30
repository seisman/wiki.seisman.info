git
===

Show changes in a commit::

    git show <COMMIT>

Add only non-whitespace changes::

    git diff -U0 -w --no-color | git apply --cached --ignore-whitespace --unidiff-zero -

Compare files in two branches:

    git diff branch1 branch2 files
