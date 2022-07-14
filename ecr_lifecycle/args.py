import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="""AWS ECR LIFECYCLE""",
        add_help=True,
        prog="aws ecr lifecycle"
    )
    parser.add_argument(
        "-l",
        "--level",
        choices=["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"],
        required=False,
        dest="log_level",
        default="DEBUG",
        help="""level of logging""",
        type=str,
    )
    parser.add_argument(
        "-a",
        "--age",
        required=False,
        default=30,
        dest="age",
        help="""Age of the image tag""",
        type=int,
    )
    parser.add_argument(
        "-r",
        "--region",
        required=True,
        dest="aws_region",
        help="""AWS region""",
        type=str,
    )
    parser.add_argument(
        "-n",
        "--n",
        required=True,
        dest="repository_name",
        help="""AWS ECR repository name""",
        type=str,
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        required=False,
        default=False,
        dest="dry_run",
        help="""Dry run the script""",
        type=bool,
    )

    return parser.parse_args()
