dynamic.map <- function(x){
a = scan("gam.dat")
b = matrix(a, ncol=20, byrow=TRUE)
rs = rowSums(b)
e.theta = b / rs
for (i in 1:119339){
write(e.theta[i, x], file = "topic_probs", append = TRUE)
}
}
