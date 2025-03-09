---
title: bitebeet (wip)
description: a bytebeat interpreter
published: true
date: 2021-04-13T16:44:15.567Z
tags: synths, keyboard, generative
editor: markdown
dateCreated: 2021-03-22T05:05:16.413Z
---

## screenshots

![bitebeet.png](/community/midouest/bitebeet.png)

## description

a [bytebeat](http://canonical.org/~kragen/bytebeat/) interpreter

> keyboard required (the typing kind)
{.is-info}

> this script is still a work-in-progress. expect bugs and usability issues
{.is-danger}

## install

`;install https://github.com/midouest/bitebeet`

> this script installs a custom ugen and engine. A reboot will be required the first time the script is launched.
{.is-info}

## guide

Enter bytebeat expressions by typing on a connected keyboard. text will wrap automatically when the screen extents are reached.

> scrolling is not yet implemented. The window can currently fit roughly 8 rows of 16 characters with the current font settings (128 characters).
{.is-warning}

### keyboard controls

- `ENTER` = evaluate expression
- `ESC` = reset `t` variable to `0`
- `BACKSPACE` = delete previous character
- `ARROW KEYS` = navigation

### syntax

The interpreter supports a subset of the C programming language expression syntax.

**example:** (the so called *crowd* bytebeat):
```
((t<<1)^((t<<1)+(t>>7)&t>>12))|t>>(4-(1^7&(t>>19)))|t>>7
```

> spaces are treated as whitespace and ignored
{.is-info}

#### Variables

Expressions may contain a single variable, `t`

> The `t` variable is automatically incremented at 8khz.
{.is-info}

> variable assignment is not supported
{.is-warning}

#### constants

constants come in two forms: integers and strings.

integers may be positive or negative

**example:** `42`, `0`, `-8`

strings are enclosed in double-quotes

**example:** `"hello, world!"`

> integers may be provided in decimal or hexadecimal format. hexadecimal integers must be preceeded with `0x`.
**example:** `0x1000`, `0xdeadbeef`
{.is-info}

#### mathematical operators

- `+` (add)
- `-` (subtract)
- `*` (multiply)
- `/` (divide)
- `%` (modulo)

**syntax:** `<left-operand> <operator> <right-operand>`

**example:** `(t+1)*(t+2)`

> Each operand of an operator must be an integer constant, the variable `t`, or an expression that evaluates to an integer.
{.is-info}

> Operators follow [c operator precedence rules](https://en.cppreference.com/w/c/language/operator_precedence). expressions can be wrapped in parenthesis to control evaluation order
{.is-info}

> division or modulo by 0 produces an internal "undefined" value. The undefined value propagates through the bytebeat expression and appears as silence in the final output.
{.is-warning}

#### bitwise operators

- `&` (and)
- `|` (or)
- `^` (xor)
- `<<` (shift left)
- `>>` (shift right)
- `~` (invert)

**example:** `(t>>8)^t`

> same rules apply as for mathematical operators
{.is-info}

#### relational operators

- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal)
- `>=` (greater than or equal)
- `==` (equal)
- `!=` (not equal)
- `!` (not)

> same rules apply as for mathematical operators
{.is-info}

> boolean (true/false) values produced by relational operators will be converted to integers using c conversion rules. `true` will become `1`, `false` will become `0`, and vice versa.
{.is-info}

#### ternary if-else

**syntax:** `<conditional> ? <if-true> : <if-false>`

**example:** `t%32<16?t>>4:t>>2`

> integers will be converted to booleans using c conversion rules (see above).
{.is-info}

> the branches of an if expression can produce strings or integers
{.is-info}

#### array subscript

**syntax:** `"<string>"[<expression>]`

**example:** `"<3 norns"[(t>>12)%8]*t>>3&t>>4`

> the result of the array subscript operation will be an 8-bit character. This character will be converted to an integer according to its [ascii representation](http://www.asciitable.com)
{.is-info}

> the interpreter performs bounds-checking when indexing string values. accessing out-of-bounds indices produces the internal undefined value (see above). It is recommended to limit index expressions to the length of the string being indexed using the modulo operator: `"<string>"[(<expression>)%<length>]`
{.is-warning}

## roadmap

- ux improvements
- dynamic values
- granular engine

## links

- [github (norns script)](https://github.com/midouest/bitebeet)
- [github (supercollider ugen)](https://github.com/midouest/bytebeat)
{.links-list}

## internals

- text entered with the script is sent to the engine using osc where it is parsed by the ugen
- parse/evaluate benchmarks can be found [here](https://github.com/midouest/bytebeat/blob/master/README.md#benchmarks). in general, the ugen is fast enough to parse and evaluate most expressions at audio rate
- the expression produces 32-bit integer values which are then truncated to the lowest 8-bits before being converted to floating point audio samples
- when the expression is sampled, the `(0, 255)` 8-bit output is converted linearly to `(-1.0, 1.0)` for audio output
- the expression produces new values at 8khz, but it is sampled at the supercollider engine's samplerate. interpolation is **not** performed when upsampling
