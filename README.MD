# SFB Games

The *SFB Games* oTree application is a collection of a few selected behavioral economics games. They are wrapped in an interface suited for showcasing them at events, such that multiple devices can be configured for visitors to continuously play the games.

The following games are currently implemented:
- Trust game (one-shot, 2 players)
- Ultimatum game (one-shot, 2 players)
- Prisoners dilemma (one-shot, 2 players)
- Bomb risk elicitation task (3 rounds, 1 player)
- Wheel of fortune (infinite rounds, 1 player)

## Setup on Heroku

Deploy this repository to Heroku and set up the following config variables:
- `OTREE_ADMIN_USERNAME` (set any username)
- `OTREE_ADMIN_PASSWORD` (set any password)
- `OTREE_AUTH_LEVEL` (set to `STUDY`)
- `OTREE_PRODUCTION` (set to `1`)

Additionally, make sure to enable the labs feature for your Heroku application by running 
`$ heroku labs:enable runtime-dyno-metadata -a <app name>` in the console.

For your Heroku resources, one single web dyno needs to be active to run the application. While not needed, it is generally
recommended to also set up a Postgres database. Without it the app will still work, however, with a few drawbacks. First, you might encounter performance issues. Second, all data will gone once the dyno goes to idle or is deactivated.

## Run

After the setup, opening the Heroku app should redirect you to a login page. Use the previously defined 
credentials from the environment variables to authenticate. Proceed by following the instructions 
shown on the landing page.
