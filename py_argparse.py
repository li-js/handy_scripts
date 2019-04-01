
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--backbone', type=str, default='ZFace_ft_parallel')
parser.add_argument('--pre_trained', type=str, default='')
parser.add_argument('--embedding_size', type=int, default=256)
parser.add_argument('--additional_embedding', type=int, default=64)

args = parser.parse_args()
