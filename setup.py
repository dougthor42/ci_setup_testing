from setuptools import setup

setup(
    name = 'ci_setup_check',
    version = '1.0.9',
    description = """This is a demo package used for figuring out travics-ci
 and AppVeyor""",
    packages=['ci_setup_check', 'ci_setup_check.tests'],
)