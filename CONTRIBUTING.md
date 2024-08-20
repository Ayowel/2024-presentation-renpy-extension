## If you make changes to the presentation

1. Test your changes in both document and presentation mode

## If you make changes to the examples

1. Test your change
2. Apply the change to all relevant examples (even if they are not shown in the presentation)
3. Ensure that the changed code does not require horizontal scrolling in revealjs if it is included in the presentation

## If you make changes to the extension loader

1. Test your change
2. Update ALL examples that make use of the extension loader
3. Build the zip reproducibly by setting all contained files' timestamp to the epoch. See the following commands if you do not use specific tooling:

```bash
# From the directory extension-loader
touch -t 198001010000 autorun.py
zip -X9o 01-extension-loader.rpe autorun.py
```
