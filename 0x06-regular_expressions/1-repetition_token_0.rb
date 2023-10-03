#!/usr/bin/env ruby
# This is ruby script that find the regular expression that will match the
# above cases
puts ARGV[0].scan(\hbt{2,5}n\).join;
