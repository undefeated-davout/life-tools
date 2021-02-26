require 'rexml/document'

# COMMAND
## Just in case, copy XML FILE to the current directory and then execute it.
# $ cp ~/Library/Containers/com.amazon.Kindle/Data/Library/Application\ Support/Kindle/Cache/KindleSyncMetadataCache.xml ./

## Just display it on terminal.
# $ ruby export-kindle-info.rb

## Output the result as text.
# $ ruby export-kindle-info.rb >> kindleTitle.txt

doc = REXML::Document.new(File.new("KindleSyncMetadataCache.xml"))
doc.elements.each('response/add_update_list/meta_data/title') do |element|
  puts element.text
end
