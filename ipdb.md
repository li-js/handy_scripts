# Execute multi-line commands when in ipython debugger
You could do this while in pdb to launch a temporary interactive Python session with all the local variables available:

```python
(pdb) !import code; code.interact(local=vars())
Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

#### When you're done, use Ctrl-D to return to the regular pdb prompt.

#### Just don't hit Ctrl-C, that will terminate the entire pdb session.
