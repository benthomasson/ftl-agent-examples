#!/bin/bash
ftl-agent-shell --tools-files ../../tools/tools.py \
          -t complete \
          -t slack \
          -M ../../modules \
          -i inventory.yml \
          -s "A linux machine" \
          -e "slack_token=${SLACK_TOKEN}"
