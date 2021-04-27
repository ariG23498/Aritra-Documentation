# simplefilter







Insert a simple entry into the list of warnings filters (at the front).

<pre><code>simplefilter(
    action, category=Warning, lineno=0, append=(False)
)</code></pre>




A simple filter matches all modules and messages.
'action' -- one of "error", "ignore", "always", "default", "module",
            or "once"
'category' -- a class that the warning must be a subclass of
'lineno' -- an integer line number, 0 matches all warnings
'append' -- if true, append to the list of filters