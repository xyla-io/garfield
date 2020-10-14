# Load the Adjust client
library(httr)
library(data.table)
library(adjust)

# Set Adjust user and app credentials
prepare_adjust <- function(usertoken, apptoken) {
  adjust.setup(user.token=usertoken, app.token=apptoken)
}