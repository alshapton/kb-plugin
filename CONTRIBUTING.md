# CONTRIBUTING

:Info: These are the contribution rules for kb-plugin.
:Copyright: 2012-2021, Andrew Shapton 
:License: GPLv3

Do you want to contribute to this project?  Great!  I’d love to see some help,
but you must comply with some rules.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
"OPTIONAL" in this document are to be interpreted as described in
RFC 2119.

# Issue reporting

GitHub Issues are the recommended way to report an issue.  If you do not have an account there, get one or mail me.

When pasting console sessions, you must paste them fully, *prompt-to-prompt*, to see all the messages and your input.  Trim only stuff that you are 1000% sure that is not related to the project in question.

# General preparations, rules and pull process

## Prepare

A GitHub account is recommended.  Patches by mail are accepted, but I’d prefer to work via GitHub.


## Rules

1. Commits must have short, informative and logical messages.  Signoffs and long messages are recommended.  "Fix #xxx" is required if an issue exists.
2. The following fancy Unicode characters should be used when needed: ``— " " ‘ ’``. ``…`` should not appear in console output, but may appear elsewhere.
3. For Python code, use the PEP 8 coding style and PEP 257 documentation style; run `flake` against your code. The only acceptable error is E501 (line too long). 
   For me, "too long" is a "reasonableness" issue - a couple of characters over the limit is ok, but 100 characters too long is clearly bad. I reserve the right to reject a PR on a "line too long" basis.
   You should also run the `codespell` tool with the following settings:
   `codespell . --ignore-words-list=hist --quiet-level=2`
   PRs will be rejected if they do not pass this test.
   For other languages, K&R style applies. Braces are mandatory in all blocks (even one-line blocks). Braces are on the same lines as class names and function signatures. Use 4-space indents.

## Request a Pull

Done?  Go hit the **Pull Request** button over on GitHub!  And if you don’t
use GitHub, ``git format-patch``.  Other formats are not accepted.

Your PR should be pulled up in a (longer) while.  If I like it.  Because
some PRs may be bad.  So, do your best not to do those bad ones!
