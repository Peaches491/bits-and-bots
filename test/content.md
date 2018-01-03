# Perfecting the prose

The test document contains a little something for everybody! Whether you want
some _slanty italics_, or perhaps some really **in-your-face bold**, we've got
you covered. This definitely ~~doesn't~~ does support strikethroughs.

And what happens in Vim if we were to start writing a line that ended up being
more than `80 characters`? Oh, joyous day! It automatically hard-wraps! Thank
heavens.

Maybe inline formatting isn't your thing? How about a list?

-   Item 1
-   Item 2
-   Item 3

If that doesn't have enough _order_ for you, then how about a numbered list?

1) Apples
2) Bananas
3) Cake

## Writing code

And finally, any good robotics book wouldn't be complete without some good ol'
fashioned source code formatting. The simplest way to render a line of code is
using backticks, like so: `echo "Hello, world" >> /dev/null`. Other times, the
body of code is too long to be easily read inline. For that, we have the code
block:

```python
def greet(bar):
    print 'Hello, %s!'.format(bar)

greet('World')
> Hello, World!
```

If you want to get fancy, you can even add line numbers to the side of a code
block! It requires some fancy markup on the authors end:

```{.cpp .numberLines}
int main(int argc, char** argv) {
    std::cout << "Help me, there's _so much syntax_ ..." << std::endl;
    return 0;
}
```

## Taking note

At times, it is useful to include a footnote in the text. To activate a
footnote, another fancy plugin is used,
[pandoc-sidenode](https://github.com/jez/pandoc-sidenote). This plugin provides
the `[^pdsn]` tag inline [^pdsn] specifies the sidenote anchor, and
`[^pdsn]: Foo bar baz...` defines the contents.

[^pdsn]: Side notes (and footnotes in general) are useful for streamlining the
flow of information, allowing the main body of the document to contain only
the most critical information. Plus, sidenotes are a great place to make
jokes!

## Where credit is due

[tufte-pandoc-css](https://github.com/jez/tufte-pandoc-css) - Let's take a
moment to give a _huge_ shoutout to the developers and contributors behind this
wonderful library, which is the basis of this books typsetting.

[pandoc-sidenode](https://github.com/jez/pandoc-sidenote) - I love media which
has a generous use of side notes. I plan to use (if not over use) sidenotes in
this book.
