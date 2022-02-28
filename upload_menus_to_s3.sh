#!/bin/bash

aws s3 cp menu.txt s3://fwp-lunchbot/ --acl public-read
