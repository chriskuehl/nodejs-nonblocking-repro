## Reproduction

1. `docker build -t ckuehl-test .`
2. `docker run ckuehl-test`


The output looks something like this:

```
$ docker run ckuehl-test
stdout is: blocking
stderr is: blocking
2
stdout is: nonblocking
stderr is: nonblocking
Now printing lots of data in Python causes an error:
Traceback (most recent call last):
  File "<string>", line 1, in <module>
BlockingIOError: [Errno 11] write could not complete without blocking
9999999999999999999999999999...
```

You can see that nodejs changes stdout/stderr to nonblocking mode when it runs
and doesn't appear to restore it.

(The actual traceback might appear before/after the nines, or be somewhere
inside of it.)
