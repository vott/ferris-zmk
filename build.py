#!/usr/bin/env python3

import subprocess
import os
import argparse

CWD = os.path.abspath(os.path.dirname(__file__))


def west(command: str, workdir="/"):
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            f"--volume={CWD}/build/zmk:/root",
            f"--volume={CWD}/config:/workspace/config",
            f"--workdir=/root/{workdir}",
            "zmkfirmware/zmk-build-arm:3.2",
            "/bin/bash",
            "-c",
            command,
        ],
        check=True,
    )


def build(side: str, pristine=False):
    west(
        " ".join([
            "west",
            "build",
            "-p" if pristine else "",
            f"-d build/{side}",
            "-b nice_nano",
            f"-- -DSHIELD=perosweep1_{side}",
            "-D ZMK_CONFIG=/workspace/config",
        ]),
        workdir="app",
    )


def reset():
    subprocess.run(
        ["cp", f"{CWD}/compiled/reset.uf2", "/Volumes/NICENANO"],
        check=True,
    )


def flash(side: str):
    subprocess.run(
        [
            "cp", f"{CWD}/build/zmk/app/build/{side}/zephyr/zmk.uf2",
            "/Volumes/NICENANO"
        ],
        check=True,
    )


def init():
    west("west init -l app/")


parser = argparse.ArgumentParser(
    prog="build.py",
    description="Build our ZMK firmware",
)
subparsers = parser.add_subparsers(dest="command")
build_parser = subparsers.add_parser("build")
build_parser.add_argument("--pristine", action="store_true")
build_parser.add_argument("--right", action="store_true")
build_parser.add_argument("--left", action="store_true")
subparsers.add_parser("reset")
flash_parser = subparsers.add_parser("flash")
flash_parser.add_argument("side", choices=["left", "right"])

args = parser.parse_args()
if args.command == "build":
    if not args.right or args.left:
        build("left", pristine=args.pristine)
    if not args.left or args.right:
        build("right", pristine=args.pristine)
if args.command == "reset":
    reset()
if args.command == "flash":
    flash(args.side)
