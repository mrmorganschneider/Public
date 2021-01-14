library(httr)
library(jsonlite)
library(httpuv)

oauth_endpoints("github")

myapp <- oauth_app("Mschneider week 2 test api",
  key = "1df5f08d3846099db9c4",
  secret = "3e9d4a7885b73cd5e7ef612f1058bf0b7d08021d"
)

# 3. Get OAuth credentials
github_token <- oauth2.0_token(oauth_endpoints("github"), myapp)

# 4. Use API
gtoken <- config(token = github_token)
req <- GET("https://api.github.com/users/jtleek/repos", gtoken)

stop_for_status(req)
json_out = content(req)

DF = jsonlite::fromJSON(jsonlite::toJSON(json_out))