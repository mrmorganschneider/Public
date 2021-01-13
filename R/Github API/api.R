library(httr)

oauth_endpoints("github")

myapp <- oauth_app("github",
  key = "1df5f08d3846099db9c4",
  secret = "32f5941ee3e3bf320955bcd27eadc7916f067207"
)

# 3. Get OAuth credentials
github_token <- oauth2.0_token(oauth_endpoints("github"), myapp)

# 4. Use API
gtoken <- config(token = github_token)
req <- GET("https://api.github.com/users/jtleek/repos", gtoken)
stop_for_status(req)
content(req)