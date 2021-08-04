# Notes on Git

Ever wonder how git shows the right command when you type in the wrong one? It uses `levenshtein` distance (sort of).
**Note:**  The actual flavor used is weighted `Damerau–Levenshtein` distance.

```bash
λ git statas
git: 'statas' is not a git command. See 'git --help'.

The most similar command is
        status
```

The algorithm looks like below:

- Create a list of all git commands.
- Sort them(`qsort`) and weed out duplicates (`uniq`).
- For each command do the following
  - Special case for common command: assign high score(i.e, distance represented by `len` is 0) if input is prefix of a common command.
  - Compute the `levenshtein` distance between the command and the input.
- Sort by score. That is what the following does.

```c
QSORT(main_cmds.names, main_cmds.cnt, levenshtein_compare);
```

- Use a similarity lower cutoff criteria to filter the best matches.
- If the best match is above the upper cutoff criteria suggest the filtered matches to the user.

## Table comparing various edit distance metrics

|Edit distance metric               |Operations permitted       |
|-----------------------------------|---------------------------|
| Longest Common Subsequence (LCS)  | `add`, `delete`           |
| Hamming distance                  | `replace`                 |
| Levenshtein distance              | `add`, `delete`, `replace`|
| Damerau–Levenshtein distance      |

## Glossary

- **Levenshtein distance**: Minimum number of single-character edits(add/delete/replace) required to convert one string to another.
