#!/usr/bin/env ruby
# This is a ruby script that find the regular expression that will match the
# above cases
puts ARGV[0].scan(/hb?tn/).join
