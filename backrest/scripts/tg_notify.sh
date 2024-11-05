URL="https://api.telegram.org/bot$TG_TOKEN/sendMessage"
curl -s -X POST $URL -d chat_id=$CHAT_ID -d text="$1 $2"
