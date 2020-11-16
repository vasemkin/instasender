## description

the simplest implementation of an instargam message sender bot.

nowadays instagram smm uses a lot of emojis.
there is no straightforward way to use emojis via sendKeys.
after some experimentation with javascript emoji insertion i went with the simplest solution:
__the script sends the message that you copied to the clipboard__.
so make sure _not to copy anything while running the script_.

multilogin is required here, if you want to run on pure webdriver:
- replace the driver initialization code with pure webdriver
- either add your instagram login cookies to the webdriver instance
  or use the `login()` function from `app.py` (not recommended)

i might update the repo to get rid of multilogin in the future

**disclamer:** this app is a proof-of-concept and using it for spam is not recommended

## requirements

dependencies used:
- selenium
- instaloader

software used:
- multilogin

## usage

1.  create an `auth.json` file. it looks like this:

    ```
    {
        "login" : "your_login",
        "target_profile" : "profile_to_parse_followers_from",
        "pass" : "your_pass",
        "profile" : "multilogin profile id"
    }
    ```

2.  the script is using `followers.txt` to send the messages.
    to generate that file, run `profiles.py`

3.  if you are using multilogin, login to instagram in the target profile

4.  launch `app.py`