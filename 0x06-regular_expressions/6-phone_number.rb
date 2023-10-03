#!/usr/bin/env ruby
# This is a ruby script that must match a 10 digit phone number
puts ARGV[0].scan(/^\d{10,10}$/).join
