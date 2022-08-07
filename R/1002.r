input <-file ("stdin", "r")

a <- as.integer(readLines(input, n=1))
b = formatC(a*a*3.14159, digits = 4, format = "f")

write(paste(b), '')