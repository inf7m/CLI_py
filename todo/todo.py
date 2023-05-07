import typer
import os
import configparser
import subprocess
import subprocess
import pkg_resources

from extentions.networking_extentions import is_valid_url, is_network_available

config = configparser.ConfigParser()
docker_script = config.read("/Users/inf7m/PycharmProjects/python_Automation/docker-config.ini")
docker_cmd = config.get(section="docker-run", option="docker-run-cmd")
app = typer.Typer()


@app.command()
def checking():
    def dependency():
        with open('/Users/inf7m/PycharmProjects/python_Automation/requirements.txt') as f:
            dependencies = f.read().splitlines()

        for libs in dependencies:
            subprocess.run(['pip', 'install', libs])

    def network() -> None:
        if is_network_available():
            print("Connection Stable")
        else:
            print("Connection Unstable")


@app.command()
def setup() -> None:
    def dockerContainer():
        result = subprocess.run('rpm -qa | grep "podman"', shell=True)
        stderr_lines = result.stderr.splitlines()
        stdout_lines = result.stdout.splitlines()
        if len(stderr_lines) > 0:
            print("Err: checking log file")
            return
        else:
            if len(stdout_lines) > 0:
                print("Podman package have alreat"
                      "dy installed")
            else:
                print("Podman package not installed yet")
                print("Will be install immediately")
                subprocess.run('yum -y install podman', shell=True)

    try:
        subprocess.run(docker_cmd)
    except subprocess.CalledProcessError:
        print("CalledProcessError")

@app.command()
def measure_performance():
    filter_lines = []
    def IOPS():
        for line  in filter_lines if "/dev" in lin

@app.command()
def environmentVar():
    pass
