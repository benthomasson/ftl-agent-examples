#!/bin/bash
ftl-agent-ui --tools-files ../../tools/tools.py \
          -M ../../modules \
          -t complete \
          -t slack \
          -s "A linux machine" \
          -e "slack_token=${SLACK_TOKEN}" \
          -e "discord_channel=${DISCORD_CHANNEL}" \
          -e "discord_token=${DISCORD_TOKEN}"
