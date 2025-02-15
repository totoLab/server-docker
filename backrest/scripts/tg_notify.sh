URL="https://api.telegram.org/bot$TG_TOKEN/sendMessage"

PLAN_ID="$1"
MESSAGE="$2"

if [[ "$MESSAGE" == *"snapshot success"* ]]; then
  text="*${PLAN_ID}* ✅
${MESSAGE}"  # Add checkmark for success
else
  text="*${PLAN_ID}*
${MESSAGE}"  # Only make plan ID bold for other messages
fi

# Send the message
curl -s -X POST $URL -d chat_id=$CHAT_ID -d parse_mode="Markdown" -d text="$text"
