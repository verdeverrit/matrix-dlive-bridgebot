### Runs once

# Initial sync for bot
curl -X GET --header 'Authorization: Bearer '"$token"'' --header 'Accept: application/json' 'https://base_url/_matrix/client/r0/sync' > sync.json

# Export all events in target room
cat sync.json | jq '.rooms.join."room_id:homeserver".timeline' > timeline.json

# Saves prev_batch token
prev_batch=$(cat timeline.json | jq '.prev_batch' | sed 's/"//g')

# Export all message events
cat timeline.json | jq '.events[] | select(.type=="m.room.message") | del(.origin_server_ts,.type,.content.msgtype) | [{sender:.sender,content:.content.body,id:.event_id,age:.unsigned.age}]' | jq -s '.' > messages.json

# Gets number of messages
let index_count="(`cat messages.json | wc -l` / 8) - 1"

# Prints messages and $prev_batch token for confirmation
for ((i=0;i<=$index_count;i++)); do cat messages.json | jq .[$i]; done && echo $prev_batch

### Repeats with $end instead of $prev_batch

# Export all new events in target room
curl -X GET --header 'Authorization: Bearer '"$token"'' --header 'Content-Type: application/json' --header 'Accept: application/json' --data '{}' 'https://base_url/_matrix/client/r0/rooms/room_id:homeserver/messages?from='"$prev_batch"'&dir=f' > chunk.json

# Saves end token
end=$(cat chunk.json | jq '.end' | sed 's/"//g')

# Export all new message events
cat chunk.json | jq '.chunk[] | select(.type=="m.room.message") | del(.origin_server_ts,.type,.content.msgtype) | [{sender:.sender,content:.content.body,id:.event_id,age:.unsigned.age}]' | jq -s '.' > new.json

# Gets number of new messages
let new_index_count="(`cat new.json | wc -l` / 8) - 1"

# Prints new messages and $end token for confirmation
for ((i=0;i<=$new_index_count;i++)); do cat new.json | jq .[$i]; done && echo $end
