from .action import Action

import subprocess


class LeapInstallation(Action):

    def __init__(self):
        self.name = "install leapp"

    def _prepare_action(self):
        subprocess.check_call(["yum", "install", "-y", "http://repo.almalinux.org/elevate/elevate-release-latest-el7.noarch.rpm"])

        pkgs_to_install = [
            "leapp-upgrade",
            "leapp-data-almalinux",
        ]

        subprocess.check_call(["yum", "install", "-y"] + pkgs_to_install)

    def _post_action(self):
        # Todo. We could actually remove installed leap packages at the end
        pass

class CheckInstall(Action):
    def __init__(self):
        self.name = "check Install"

    def _prepare_action(self):
        print("Install")

    def _post_action(self):
        print("back Install")