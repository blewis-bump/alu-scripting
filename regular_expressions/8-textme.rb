#!/usr/bin/env ruby
m = ARGV[0].match(/\[from:(?<sender>[^\]]+)\].*\[to:(?<receiver>[^\]]+)\].*\[flags:(?<flags>[^\]]+)\]/)
puts "#{m[:sender]},#{m[:receiver]},#{m[:flags]}"
