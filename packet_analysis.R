library(ggplot2)

table<- read.csv("C:/Users/seanj/projects/ai_security/table.csv")
table <- table[,-1]
destination <- data.frame(table[,2], table[,4])
names(destination) <- c("Destination IP", "Destination Port")
dtable <- as.data.frame(table(destination))
source <- data.frame(table[,1], table[,3])
names(source) <- c("Source IP", "Source Port")
stable <- as.data.frame(table(source))
ggplot(dtable, aes(Destination.IP, Destination.Port, fill=Freq)) + geom_tile() + theme(axis.text.x = element_text(angle=90))
ggplot(stable, aes(Source.IP, Source.Port, fill=Freq)) + geom_tile()+ theme(axis.text.x = element_text(angle=90))
table(destination)
