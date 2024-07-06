import argparse

def preload(parser: argparse.ArgumentParser):
    parser.add_argument(
            "--generation-scheduler-yaml",
            help = "[Generation Scheduler] A YAML file containing the schedule",
            )

