import read
import dateutil

def extractHour(field, extractType):
    dateComposition = {
        "hour": "%H",
        "minute": "%M",
        "weekday": "%U",
        "day": "%d",
        "month": "%m",
        "year": "%Y"
    }

    timeParsed = dateutil.parser.parse(field)
    return timeParsed.strftime(dateComposition[extractType])

data = read.load_data()

print(data["submission_time"].head(5))
data["hour"] = data["submission_time"]

variablesTime = ["hour", "minute", "weekday", "day", "month", "year"]

for v in variablesTime:
    data[v] = data["submission_time"]
    data[v] = data[v].apply(extractHour, extractType=v)
    print(data[v].value_counts())


