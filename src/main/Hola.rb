def fibs(n)
     if n == 1 or n == 0
          return 1
     else
          return fibs(n-1)+fibs(n-2)
     end
end

if __FILE__ == $0
     n = gets.chomp().to_i
     out = fibs(n)
     puts "#{out}"
end