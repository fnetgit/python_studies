# argparse.ArgumentParser - para argumentos mais complexos

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    "-b",
    "--basic",
    help="Mostra o valor de b",
    type=int,
    metavar="STRING",
    default="olá mundo",
    nargs="+",
    action="append",
)
args = parser.parse_args()

if args.basic is None:
    print("Você não passou o valor de b.")
    print(args.basic)
else:
    print("O valor de b:", args.basic)
