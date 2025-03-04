
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


https://github.com/user-attachments/assets/78d5c157-1518-43ec-8368-892514cc74b7

