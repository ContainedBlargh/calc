# calc

A Python script command-line calculator.
Functionality is restricted to the regular python math package and a subset of numpy.

## Usage

Write your expressions as you would in Python, lists are converted to numpy arrays automatically.

Write the expression as individual arguments:

```
$> calc 2 + 2
4
$> calc 4 - 1
3
$> echo "Quickmafs"
Quickmafs
```

or as a string:

```
$> calc "2 + 2"
4
```

Include first number argument from stdin using `$`:

```
$> echo "2" | calc "$/2"
1
```

or include whole expressions from stdin using `$` in combination with `-w` (for `whole`).

```
$> echo "(2 + 2)" | calc -w "$/2"
2
```

That's it.

## Why?

Sometimes you want to write stuff like `wc -c ./my_file.txt | calc "$ / 200"`, but there is no simple way to do it.

Sure, you could use `awk` and you might consider it simple enough to use.

But I didn't want to **think**, that's what my computer is supposed to do.

## FAQ

>Your script is dumb/buggy/insecure.

Yes.
