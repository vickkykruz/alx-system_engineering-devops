#!/usr/bin/env ruby
# This is a ruby script that give the required output
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
