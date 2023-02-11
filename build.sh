file="community.json"
count=$(jq '.entries | length' $file)
echo "$count entries in $file"
rm list.md
for i in $(seq 1 $count)
#for i in $(seq 1 3)
do
  #echo $(jq '.entries['$i'].project_name' $file)
  name=$(jq '.entries['$i'].project_name' $file | tr -d '"')
  url=$(jq '.entries['$i'].project_url' $file | tr -d '"')
  desc=$(jq '.entries['$i'].description' $file | tr -d '"')
  echo "[$url]($name) - $desc" >> list.md
done
