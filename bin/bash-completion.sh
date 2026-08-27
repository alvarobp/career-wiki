#!/bin/bash
# Tab completion for the `wiki` command.
# Source it from your shell config:
#   source ~/personal/code/career-wiki/bin/bash-completion.sh

_wiki_completion() {
    local cur prev
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD - 1]}"

    if [ "$COMP_CWORD" -eq 1 ]; then
        COMPREPLY=($(compgen -W "add" -- "$cur"))
        return
    fi

    if [ "${COMP_WORDS[1]}" = "add" ]; then
        # --from takes a path; everything else is a URL, which we can't complete
        if [ "$prev" = "--from" ] || [ "$prev" = "-f" ]; then
            COMPREPLY=($(compgen -f -- "$cur"))
        elif [[ "$cur" == -* ]]; then
            COMPREPLY=($(compgen -W "--text --from" -- "$cur"))
        fi
    fi
}

complete -F _wiki_completion wiki
