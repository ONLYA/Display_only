# WSL uname test

> This demonstrates the problem of uname function in WSL. It will return "Windows" in WSL instead of "Linux" while it returns proper value on a real Linux machine.

A makefile project to demonstrate building a portable Hello World executable with [Cosmopolitan Libc](https://github.com/jart/cosmopolitan)

There is a great blog from [Getting Started with Cosmopolitan Libc | Jon Eskin's Website](https://web.archive.org/web/20221027125525/https://jeskin.net/blog/getting-started-with-cosmopolitan-libc/).

# Building

## Linux

```bash
$ make
```

## MacOS

```bash
$ brew install x86_64-elf-gcc
$ make CC=x86_64-elf-gcc OBJCOPY=x86_64-elf-objcopy
```

## Windows

See https://justine.lol/cosmopolitan/windows-compiling.html

# Running
## Linux Or MacOS Or Powershell

```bash
$ ./hello.com # Linux bash Or MacOS Or Powershell
```

## Windows CMD

```cmd
C:\> REM Windows cmd
C:\> hello.com
```

## Note: Running with ZSH

ZSH does not currently work, you'll see the following error:
```bash
zsh: exec format error: ./hello.com
```

You need to run with Bash until a pending fix is merged upstream:

```bash
$ bash -c './hello.com'
```
