#!/usr/bin/env ruby
##
# Sort integer arguments (ascending order).
# - Only numeric arguments are considered.
# - Non-numeric arguments are ignored.
##

# Get command line arguments
args = ARGV

# Filter out non-numeric arguments and convert to integers
numbers = []
args.each do |arg|
    # Try to convert to integer, skip if it fails
    begin
        # Check if the string represents an integer
        if arg.match?(/\A-?\d+\z/)
            num = Integer(arg)
            numbers << num
        end
    rescue ArgumentError
        # Skip non-numeric arguments
        next
    end
end

# FIXED: Sort numbers in ascending order
sorted_numbers = numbers.sort

# Print each number on a new line
sorted_numbers.each do |num|
    puts num
end