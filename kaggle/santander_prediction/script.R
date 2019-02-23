library(rerf)
library(caret)

NUM.CORES <- 2L
TREES <- 2L
MAX.DEPTH <- 0L
NUM.FOREST <- 10L

print("Loading trainin data")
train <- read.csv('./train.csv')

print("Loading testing data")
X.test <- read.csv('./test.csv', row.names = 1)
ids <- rownames(X.test)

predictions <- matrix(0, nrow = nrow(X.test), ncol = 2)

for (i in 1:NUM.FOREST) {
  cat("\r Computing Tree: ", i)
  tmp <- downSample(train[1:nrow(train), 3:ncol(train)], 
                    as.factor(train[1:nrow(train), 2]), 
                    list=TRUE)
  
  X.train <- as.matrix(tmp[[1]])
  Y.train <- as.factor(tmp[[2]])
  
  forest <- RerF(X.train, 
                 Y.train, 
                 min.parent=1, 
                 max.depth = MAX.DEPTH,
                 trees=TREES, 
                 num.cores = NUM.CORES, 
                 store.oob=TRUE, 
                 progress=TRUE,
                 stratify=TRUE)
  
  tmp.pred <- Predict(X.test, forest, 
                      num.cores = NUM.CORES, 
                      aggregate.output = FALSE, 
                      output.scores = TRUE)

  predictions <- predictions + Reduce("+", tmp.pred) 
}

print("Computing predictions")
predictions <- max.col(predictions / (NUM.FOREST * TREES), ties.method="random") - 1

print(table(predictions) / nrow(X.test))

out <- cbind(ids, predictions)
colnames(out) <- c("ID_code", "target")

print("saving results")
write.csv(out, file='results.csv', quote=FALSE, row.names=FALSE)
