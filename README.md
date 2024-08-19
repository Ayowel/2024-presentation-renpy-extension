# Ren'py extensions

This presentation is written for the [Capitole du Libre](https://capitoledulibre.org/) 2024 edition.

Its aim is to go over what must be done to create, share and update code in Ren'Py and - in doing so - get a better understanding of how saving/reloading works with the python module `pickle` and how Ren'Py internally handles data changes and rollback.

## Build the doc

The presentation may both be generated as an actual presentation with revealjs and as a regular HTML document/pdf.

Building requires to have installed [Ruby](https://www.ruby-lang.org/en/) with the gems [asciidoctor](https://rubygems.org/gems/asciidoctor) (as well as [asciidoctor-revealjs](https://rubygems.org/gems/asciidoctor-revealjs) for the presentation).

*Build as a document:*

```bash
# Use asciidoctor-pdf instead to build a PDF
asciidoctor -o document.html presentation.adoc
```

*Build as a presentation:*

```bash
asciidoctor -r asciidoctor-revealjs -b revealjs -a revealjsdir="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0" -o index.html presentation.adoc
```

## Contribute

Contributions are welcome, please check [CONTRIBUTING.md](CONTRIBUTING.md) for generic guidelines when making changes.
