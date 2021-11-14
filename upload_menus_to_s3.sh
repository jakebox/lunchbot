#!/bin/bash

aws s3 sync menus/ s3://fwp-lunchbot/menus/ --acl public-read
