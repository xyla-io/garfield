AdjustPeriod <- list(day="day", week="week", month="month")

AdjustAPI <- setClass(
  # Set the name for the class
  "AdjustAPI",

  # Define the slots
  slots = c(
    user_token = "character",
    app_token = "character"
  )
)

setGeneric(name="connect",
           def=function(o) {
             standardGeneric("connect")
           }
)

setMethod(f="connect",
          signature="AdjustAPI",
          definition=function(o) {
            library(adjust)
            adjust.setup(user.token=o@user_token, app.token=o@app_token)
          }
)

setGeneric(name="disconnect",
           def=function(o) {
             standardGeneric("disconnect")
           }
)

setMethod(f="disconnect",
          signature="AdjustAPI",
          definition=function(o) {
            detach("package:adjust", unload=TRUE)
          }
)
