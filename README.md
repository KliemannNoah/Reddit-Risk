# Reddit-Risk
Code for the a reddit bot that sends out orders VIA PM

Reddit is a online messaging board split up into units called "subreddits," each of which revolve around a different thing. I was an avid follower for the College Football Subreddit. Over the summer they held a massive modified version of the board game Risk. Every User on the subreddit declared what team they wanted to play for, and then daily they had the option of either defending a territory held by their team or by attacking an adjacent territory held by another team. 

The teams that did the best were the teams that were organizing and coordinating strategy with each other. I helped with this process manually at first, but we had a problem where we had to do it in the open and thus it was easy for rivals to know what we were going to do.

So, I created a Python bot to help in the process. The python bot could get registered through reddit to send users messages from the bot itself. After those of us in charge of the Wisconsin faction decided where we wanted to send our users, I could place the percentage of users per-territory into the bot and it would then send out a message to all of the users with their assignment, randomized based on the percentages provided. This bot received constant tweaks and improvements to better represent what we wanted, and helped Wisconsin place top 10.

Adjustments had to be made very quickly, as the vote occurred at Midnight EST everyday, so I had to exhibit the ability to make fast changes as the game evolved on a daily basis as well as tackle some technical hurdles and forecast future needs.

A slightly more expanisve version of the bot is available in a private repository that I can provide, but as it contains more sensitive and active work is not public. Updates included weighting the value of a user when distributing them to certain territories and to randomize the users in addition to the blocks for futher 'randomness.' 

Currently working on incorporating references into python so the user list can be kept in an external script or a database so that we can perform better data metrics next year.
