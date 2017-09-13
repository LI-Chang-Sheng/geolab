# geolab

## 1.0.0

*Approx 10-15 lines*.

The aim of this project is to provide a python module for processing molecular 
dynamics data. We currently using CP2K, DLPOLY and LAMMPS to probe the interface
between minerals and water.

This project is divided into following parts:
	1. io
	2. structure
	3. dynamics
	4. energy and forces
	
## Ethics

This project operates under the W3C's
[Code of Ethics and Professional Conduct](https://www.w3.org/Consortium/cepc):

> W3C is a growing and global community where participants choose to work
> together, and in that process experience differences in language, location,
> nationality, and experience. In such a diverse environment, misunderstandings
> and disagreements happen, which in most cases can be resolved informally. In
> rare cases, however, behavior can intimidate, harass, or otherwise disrupt one
> or more people in the community, which W3C will not tolerate.
>
> A Code of Ethics and Professional Conduct is useful to define accepted and
> acceptable behaviors and to promote high standards of professional
> practice. It also provides a benchmark for self evaluation and acts as a
> vehicle for better identity of the organization.

We hope that our community group act according to these guidelines, and that
participants hold each other to these high standards. If you have any questions
or are worried that the code isn't being followed, please contact the owner of the repository.


## Language

The development language is English. All comments and documentation should be written in English, so that we don't end up with “franglais” methods, and so we can share our learnings with developers around the world.

However, the domain language is French. We consider each tax, collecting organism and French regulation as a domain-specific term. In the same fashion, well-known abbreviations of these domain-specific terms are accepted.

OR

Par souci de lisibilité pour les partenaires, la langue utilisée pour la description et le suivi de fonctionnalités est le français.

En revanche, pour éviter le coût du changement de contexte, les discussions techniques peuvent se faire en anglais, la langue la plus utilisée dans le cadre du développement logiciel.

## History

I started this project in 2016 for my undergraduate thesis.

I open-sourced it in 2017 and in an organized form.

## Installation

Just add the geolab directory to your PYTHONPATH like:
    export PYTHONPATH=/path/to/geolab:$PYTHNPATH

Once installed, you have to run these commands to use the project:

	import geolab
 or 
	from geolab import io

Enjoy!

## Contributing

We’re really happy to accept contributions from the community, that’s the main reason why we open-sourced it! There are many ways to contribute, even if you’re not a technical person.

We’re using the infamous [simplified Github workflow](http://scottchacon.com/2011/08/31/github-flow.html) to accept modifications (even internally), basically you’ll have to:

* create an issue related to the problem you want to fix (good for traceability and cross-reference)
* fork the repository
* create a branch (optionally with the reference to the issue in the name)
* hack hack hack
* commit incrementally with readable and detailed commit messages
* submit a pull-request against the master branch of this repository

We’ll take care of tagging your issue with the appropriated labels and answer within a week (hopefully less!) to the problem you encounter.

If you’re not familiar with open-source workflows or our set of technologies, do not hesitate to ask for help! We can mentor you or propose good first bugs (as labeled in our issues). Also welcome to add your name to Credits section of this document.

### Submitting bugs

You can report issues directly on Github, that would be a really useful contribution given that we lack some user testing on the project. Please document as much as possible the steps to reproduce your problem (even better with screenshots).

### Discussing strategies

We’re trying to develop this project in the open as much as possible. We have a dedicated mailing-list where we discuss each new strategic change and invite the community to give a valuable feedback. You’re encouraged to subscribe to it and participate.

### Adding documentation

We’re doing our best to document each usage of the project but you can improve it or add you own sections. The documentation is available within the /docs/ folder. You don’t have to build anything, we’ll take care of it once your changes are merged.


## License

We’re using the GNU GENERAL PUBLIC LICENSE Version 3 license.


## Credits

* [Yingchun Zhang]
* yczhang@smail.nju.edu.cn
