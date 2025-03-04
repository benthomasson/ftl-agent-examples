
```console
ftl-agent-ui --tools-files ../../tools/tools.py \
          -M ../../modules \
          -t complete \
          -t slack \
          -s "A linux machine" \
          -e "slack_token=${SLACK_TOKEN}" \
          -e "discord_channel=${DISCORD_CHANNEL}" \
          -e "discord_token=${DISCORD_TOKEN}"
```

Demo:

https://github.com/user-attachments/assets/2ab58c24-16dc-41c7-9992-c73ec7183dd0

