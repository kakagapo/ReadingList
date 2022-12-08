# Git errors and their fixes

Following error in Windows OS when you do `git clone`
```
xxx/.../xxx.js: Filename too long
```

**Git filename size limit:** 4096 characters

On Windows when Git is compiled with msys it uses an older version of the Windows API and there's a limit of 260 characters for a filename.
More details here: https://github.com/msysgit/git/pull/110

**Fix:**
```
git config --system core.longpaths true
```