#!/usr/bin/env bash
docker run --rm -a stdout -a stderr --log-driver=none -v /home/mconway/temp/image:/de-app-work  --name thumbs -w /de-app-work --net=bridge diceunc/thumbnail:1.0 /de-app-work 250
