# SFB Games

The *SFB Games* oTree application is a collection of a few selected behavioral economics games. They are wrapped in an interface suited for showcasing them at events, such that multiple devices can be configured for visitors to continuously play the games.

The following games are currently implemented:
- Trust game (one-shot, 2 players)
- Ultimatum game (one-shot, 2 players)
- Prisoners dilemma (one-shot, 2 players)
- Bomb risk elicitation task (3 rounds, 1 player)
- Wheel of fortune (infinite rounds, 1 player)

## Installation

One easy way to get this application running online is through Heroku. Simply deploy this repository
to Heroku and set up the following environment variables (called "*Config Vars*" on Heroku):
- `OTREE_ADMIN_USERNAME` (set any username)
- `OTREE_ADMIN_PASSWORD` (set any password)
- `OTREE_AUTH_LEVEL` (set to `STUDY`)
- `OTREE_PRODUCTION` (set to `1`)

Additionally, make sure to enable the labs feature for your application by running 
`$ heroku labs:enable runtime-dyno-metadata -a <app name>`. This is needed for your application to be able to retrieve
the `HEROKU_APP_DEFAULT_DOMAIN_NAME` environment variable.

For your Heroku resources, one web dyno needs to be active to run the application. While not needed, it is generally
recommended to also set up a Postgres database ("*Heroku Postgres*"). Without it the app will still work, however there are a few drawbacks. First, you might encounter performance issues. Second, data will be stored temporarily and gone when the dyno goes to idle or is deactivated.

## Usage

Once the application is installed, opening the app should redirect you to a login page. Use the previously defined 
credentials from the environment variables. After successfully logging in, follow the setup instructions 
shown on the landing page.

## Contributing

Pull requests are welcome. For major changes (e.g., additional games), please open an issue first to discuss what 
you would like to change.
