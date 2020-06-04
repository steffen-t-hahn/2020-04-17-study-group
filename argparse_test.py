"""Example script to show the capabilities of the argparse module."""
import argparse


if "__main__" == __name__:
    p = argparse.ArgumentParser()
    p.add_argument('-r', '--redo', default=False, action='store_true',
                   help='redo train/test split, default: False')
    p.add_argument('-d', '--datafolder', default='aachen_input',
                   type=str, help='<path>')
    p.add_argument('-o', '--outputfolder', default='aachen_input_norm',
                   type=str, help='<path>')
    p.add_argument('-ha', '--hadronicmodel', default='EPOS',
                   type=str, help='EPOS or QGSJ')

    p.add_argument('-s', '--standardize', default=False, action='store_true',
                   help='use event\'s azimuth to standardize shower')
    p.add_argument('-e', '--extra', default='_linear',
                   type=str, help='default: _linear')

    p.add_argument('-tr', '--trainsize', default=200000,
                   type=int, help='default: 200000')
    p.add_argument('-te', '--testsize', default=50000,
                   type=int, help='default: 50000')

    p.add_argument('-p', '--pdf', default=False, action='store_true',
                   help='use a special energy pdf')
    p.add_argument('-az', '--azimuth', default=False, action='store_true',
                   help='cut all wrong azimuths out')

    args = p.parse_args()

    print(args)
