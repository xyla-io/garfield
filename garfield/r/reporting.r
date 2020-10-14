AdjustReporter <- setClass(
  # Set the name for the class
  "AdjustReporter",
  
  # Define the slots
  slots = c(
    api = "AdjustAPI"
  )
)

setGeneric(name="fetch_cohort_report",
           def=function(o, cohort_start, cohort_end, period) {
             standardGeneric("fetch_cohort_report")
           }
)

setMethod(f="fetch_cohort_report",
          signature="AdjustReporter",
          definition=function(o, cohort_start, cohort_end, period) {
            kpis <- c("revenue_events", "revenue", "events", "cohort_size", "converted_users")
            grouping <- c("networks", "campaigns", "adgroups", "creatives", "os_names", "events", "countries", "region")
            start_date <- format(cohort_start)
            end_date <- format(cohort_end)
            
            data <- adjust.cohorts(kpis=kpis, 
                                   grouping=grouping,
                                   start_date=start_date, 
                                   end_date=end_date, 
                                   period=period)
      
            return(data)
          }
)

setGeneric(name="fetch_events_report",
           def=function(o, start_date, end_date) {
             standardGeneric("fetch_events_report")
           }
)

setMethod(f="fetch_events_report",
          signature="AdjustReporter",
          definition=function(o, start_date, end_date) {
            kpis <- c("revenue_events", "revenue", "events", "first_events")
            grouping <- c("networks", "campaigns", "adgroups", "creatives", "os_names", "events", "countries", "region")
            
            data <- adjust.events(start_date = format(start_date), 
                                  end_date = format(end_date),
                                  kpis = kpis,
                                  grouping = grouping)
            
            return(data)
          }
)

setGeneric(name="fetch_deliverables_report",
           def=function(o, start_date, end_date) {
             standardGeneric("fetch_deliverables_report")
           }
)

setMethod(f="fetch_deliverables_report",
          signature="AdjustReporter",
          definition=function(o, start_date, end_date) {
            kpis <- c("impressions", "clicks", "installs", "revenue_events", "revenue", "events", "first_events")
            grouping <- c("networks", "campaigns", "adgroups", "creatives", "os_names", "events", "countries", "region")
            
            data <- adjust.deliverables(start_date = format(start_date), 
                                        end_date = format(end_date),
                                        kpis = kpis,
                                        grouping = grouping)
            
            return(data)
          }
)