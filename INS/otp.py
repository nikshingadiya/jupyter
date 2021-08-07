import argparse
import base64
import bz2
import logging
import sys

__version__ = "2017.06.04"


def main(argv):
    """
    Entry point for onepad.
    Arguments:
        argv: command line arguments
    """
    logging.basicConfig(level="WARNING", format="%(levelname)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "cmd", type=str, choices=["enc", "dec"], help="action to perform"
    )
    parser.add_argument("datafile", type=str, help="name of the key-file.")
    parser.add_argument("keyfile", type=str, help="name of the key-file.")
    args = parser.parse_args(argv)
    try:
        with open(args.datafile, "rb") as df:
            data = df.read()
        with open(args.keyfile, "rb") as kf:
            key = unwrap(kf.read())
    except IOError as e:
        logging.error("reading input files failed; {}".format(e))
        sys.exit(1)
    if args.cmd == "dec":
        data = unwrap(data)
    else:
        # Compress *before* encryption.
        # The slice removes the bz2 header which would otherwise be a crib.
        data = bz2.compress(data)[10:]
    if len(data) > len(key):
        logging.error("message longer than the key.")
        sys.exit(2)
    rv = bytes([i ^ j for i, j in zip(data, key)])
    if args.cmd == "enc":
        rv = bytes(encode(rv), "utf-8")
    else:
        # Decompress after decryption. Re-add bz2 header first.
        rv = bz2.decompress(b"BZh91AY&SY" + rv)
    print(rv.decode("utf-8"))


def unwrap(data):
    """
    Decode a formatted base64 keystring or an encrypted string.
    Arguments:
        data: Bytes to decode.
    Returns:
        The decoded input.
    """
    data = bytes([b for b in data if b not in b" \r\n"])
    return base64.b64decode(data)


def encode(data, chunklen=6, linelen=78):
    """
    Encode data with base64 and format it.
    Arguments:
        data: String to be encoded.
        chunklen: Number of bytes in a chunk, defaults to 6.
        linelen: Length of a line, defaults to 78 characters.
    Returns:
        The base64 encoded data.
    """
    length = len(data)
    n = int(linelen // (4 * chunklen / 3))
    chunks = [
        base64.b64encode(data[j : j + chunklen]).decode("ascii")
        for j in range(0, length, chunklen)
    ]
    lines = [" ".join(chunks[i : i + n]) for i in range(0, len(chunks), n)]
    return "\n".join(lines)


if __name__ == "__main__":
    main(sys.argv[1:])