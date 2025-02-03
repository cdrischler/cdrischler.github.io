## Hello there!

I'm an Assistant Professor of Physics and [FRIB](https://frib.msu.edu/) Bridge Faculty at the [Institute of Nuclear and Particle Physics (INPP)](https://inpp.ohio.edu/~inpp/) at Ohio University. I'm also a member of the [FRIB Theory Alliance Executive Board](https://www.fribtheoryalliance.org/content/executive_board.php). 

My current research interests include:
* Neutron stars
* Equation of state of neutron-rich matter
* Chiral effective field theory
* Many-body perturbation theory
* Bayesian methods for uncertainty quantification
* Emulators for nuclear physics and model (order) reduction
* Computational physics

I'm collaborating with:
* NSF Physics Frontier Center _Network for Neutrinos, Nuclear Astrophysics, and Symmetries_ ([N3AS](https://n3as.berkeley.edu/))
* _Bayesian Uncertainty Quantification: Errors in Your EFT_ ([BUQEYE](https://buqeye.github.io/)) collaboration, and
* NSF Bayesian Analysis of Nuclear Dynamics ([BAND](https://bandframework.github.io/)) Framework

The complete list of my publications can be found on [inspirehep.net](https://inspirehep.net/authors/1405840?ui-citation-summary=true).

Don't hesitate to contact me if you are interested in a Research Fellowship of the [Alexander von Humboldt Foundation](https://www.humboldt-foundation.de/en/) (such as the [Feodor Lynen Research Fellowship](https://www.humboldt-foundation.de/en/apply/sponsorship-programmes/feodor-lynen-research-fellowship)) hosted by me at Ohio University.


## Awards and honors

* National Science Foundation (NSF) CAREER Award, 2024 to present
* Inaugural FRIB Early Achievement Award (theory), Facility for Rare Isotope Beams at Michigan State University, 2021
* FRIB Theory Alliance Fellowship, 2020-2022
* Feodor Lynen Fellowship of the Alexander von Humboldt Foundation, 2019-2020
* Research Award of the Gerhard Herzberg Foundation at Technical University Darmstadt, 2018

## In the News

* [Dr. Christian Drischler receives 2024 NSF CAREER Award to advance research, educate students and community](https://www.ohio.edu/news/2024/09/dr-christian-drischler-receives-2024-nsf-career-award-advance-research-educate)
* [Ohio University physicists aim to bring artificial intelligence, machine learning and computational tools to nation's researchers](https://www.ohio.edu/news/2023/09/ohio-university-physicists-aim-bring-artificial-intelligence-machine-learning)


## Funding

* [National Science Foundation's CAREER: Nuclear Matter from Chiral Effective Field Theory in the FRIB & Multimessenger Era (2339043)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2339043&HistoricalAwards=false)
* [Department of Energy's STREAMLINE Collaboration: Machine Learning for Nuclear Many-Body Systems
Award Status: Active (DE-SC0024233)](https://pamspublic.science.energy.gov/WebPAMSExternal/Interface/Common/ViewPublicAbstract.aspx?rv=66cb84af-5b64-41f7-a2a8-47c38f44ef3f&rtc=24&PRoleId=10)

## Research Group

My current research group consists of:
* [Jane Kim](https://www.ohio.edu/cas/janekim) (postdoc)
* [Yoon Gyu Lee](https://www.ohio.edu/cas/yl518521) (grad student)
* [Abhinav Giri](https://www.ohio.edu/cas/ag086822) (grad student, STREAMLINE collaboration)
* [Grace Eichler](https://www.linkedin.com/in/grace-eichler-b87a772b4) (undergrad student)

Previous members:
* [Joshua Maldonado](https://www.ohio.edu/cas/jm998521) (grad student, M.S. thesis 2024, summer 2023 to summer 2024, STREAMLINE collaboration)
* [Unish Gautam](https://www.ohio.edu/cas/ug783023) (grad student, summer 2024)

## Brief Academic CV

* Assistant Professor and FRIB Theory Alliance bridge faculty, Ohio University, 2022-today
* FRIB Theory Fellow (Visiting Assistant Professor), Facility for Rare Isotope Beams at Michigan State University, 2020-2022
* Humboldt Fellow, University of California, Berkeley, and Lawrence Berkeley National Laboratory, 2019-2020
* Postdoctoral researcher, University of California, Berkeley, and Lawrence Berkeley National Laboratory, 2017-2019
* Ph.D., Physics, Technical University Darmstadt, Germany, 2017
* M.Sc., Physics, Technical University Darmstadt, Germany, 2014
* B.Sc., Physics, Technical University Darmstadt, Germany, 2012

# Academic Pages
**Academic Pages is a GitHub Pages template for personal and professional portfolio-oriented websites.**

![Academic Pages template example](images/homepage.png "Academic Pages template example")

# Getting Started

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Click the "Use this template" button in the top right.
1. On the "New repository" page, enter your repository name as "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and add your content.
1. Upload any files (like PDFs, .zip files, etc.) to the `files/` directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## Running locally

When you are initially working your website, it is very useful to be able to preview the changes locally before pushing them to GitHub. To work locally you will need to:

1. Clone the repository and made updates as detailed above.
1. Make sure you have ruby-dev, bundler, and nodejs installed
    
    On most Linux distribution and [Windows Subsystem Linux](https://learn.microsoft.com/en-us/windows/wsl/about) the command is:
    ```bash
    sudo apt install ruby-dev ruby-bundler nodejs
    ```
    On MacOS the commands are:
    ```bash
    brew install ruby
    brew install node
    gem install bundler
    ```
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `jekyll serve -l -H localhost` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

If you are running on Linux it may be necessary to install some additional dependencies prior to being able to run locally: `sudo apt install build-essential gcc make`

## Using Docker

Working from a different OS, or just want to avoid installing dependencies? You can use the provided `Dockerfile` to build a container that will run the site for you if you have [Docker](https://www.docker.com/) installed.

You can build and execute the container by running the following command in the repository:

```bash
docker compose up
```

You should now be able to access the website from `localhost:4000`.

# Maintenance

Bug reports and feature requests to the template should be [submitted via GitHub](https://github.com/academicpages/academicpages.github.io/issues/new/choose). For questions concerning how to style the template, please feel free to start a [new discussion on GitHub](https://github.com/academicpages/academicpages.github.io/discussions).

This repository was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License (see LICENSE.md). It is currently being maintained by [Robert Zupko](https://github.com/rjzupkoii) and additional maintainers would be welcomed.

## Bugfixes and enhancements

If you have bugfixes and enhancements that you would like to submit as a pull request, you will need to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repository as opposed to using it as a template. This will also allow you to [synchronize your copy](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) of template to your fork as well.

Unfortunately, one logistical issue with a template theme like Academic Pages that makes it a little tricky to get bug fixes and updates to the core theme. If you use this template and customize it, you will probably get merge conflicts if you attempt to synchronize. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch.

---
<div align="center">
    
![pages-build-deployment](https://github.com/academicpages/academicpages.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/academicpages/academicpages.github.io.svg)](https://github.com/academicpages/academicpages.github.io/graphs/contributors)
[![GitHub release](https://img.shields.io/github/v/release/academicpages/academicpages.github.io)](https://github.com/academicpages/academicpages.github.io/releases/latest)
[![GitHub license](https://img.shields.io/github/license/academicpages/academicpages.github.io?color=blue)](https://github.com/academicpages/academicpages.github.io/blob/master/LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/academicpages/academicpages.github.io)](https://github.com/academicpages/academicpages.github.io)
[![GitHub forks](https://img.shields.io/github/forks/academicpages/academicpages.github.io)](https://github.com/academicpages/academicpages.github.io/fork)
</div>
