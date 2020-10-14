#!/usr/local/bin/Rscript

library(jsonlite)
args <- commandArgs(trailingOnly = TRUE)
options <- fromJSON(args)
# options <- list(
#   app_token = 'APP_TOKEN',
#   user_token = 'USER_TOKEN',
#   report_type = 'cohort',
#   report_parameters = list(
#     cohort_start = '2018-10-01',
#     cohort_end = '2018-10-01',
#     period = 'day'
#   ),
#   # report_parameters = list(
#   #   start_date = '2018-10-01',
#   #   end_date = '2018-12-31'
#   # ),
#   r_directory = dirname(getSrcFilename(function(x) {x}, full.names = TRUE))
# )

# Load the Adjust client
library(httr)
library(data.table)
library(adjust)

source(file.path(options$r_directory, 'api.r'))
source(file.path(options$r_directory, 'reporting.r'))

api <- AdjustAPI(user_token = options$user_token, app_token = options$app_token)
reporter <- AdjustReporter(api = api)

report_function = switch(
  options$report_type,
  cohort = function(report_parameters) {
     do.call(fetch_cohort_report, c(list(o = reporter), report_parameters))
  },
  events = function(report_parameters) {
    do.call(fetch_events_report, c(list(o = reporter), report_parameters))
  },
  deliverables = function(report_parameters) {
    do.call(fetch_deliverables_report, c(list(o = reporter), report_parameters))
  }
)

connect(api)
data <- report_function(options$report_parameters)
disconnect(api)

write.csv(data, row.names = FALSE)