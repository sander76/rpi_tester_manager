import logging
from pathlib import Path

from invoke import task

_LOGGER = logging.getLogger(__name__)


REPO_FOLDER = Path.home() / "repos"
TEST_FOLDER = Path.home() / "tests"


@task
def make_folders(ctx):
    REPO_FOLDER.mkdir(exist_ok=True)
    TEST_FOLDER.mkdir(exist_ok=True)


@task(make_folders)
def clean(ctx):
    if (Path.home() / "squid_nodes").exists():
        print("moving squid nodes folder")
        ctx.run("mv ~/squid_nodes {}".format(REPO_FOLDER))

    if (Path.home() / "test_configs_bak").exists():
        print("removing test_configs_folder")
        ctx.sudo("rm test_configs_bak -r -y")


@task(make_folders)
def install_hmip_driver(ctx):
    with ctx.cd(REPO_FOLDER):
        ctx.run("git clone https://github.com/sander76/hmip-rf-usb-linux.git")
        with ctx.cd("hmip-rf-usb-linux/driver"):
            ctx.sudo("bash install.sh")
