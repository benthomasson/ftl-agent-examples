#!/bin/bash
ftl-agent --tools-files ../tools/tools.py \
          -t complete \
          -t slack \
          -s "A linux machine" \
          -M ../modules \
          -i inventory.yml \
          -p "Send message to Slack, and call complete when done" \
          -e "slack_token=${SLACK_TOKEN}"
