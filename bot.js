const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('pong');
  }
});

client.login('NjgzMzgyMjA3NzcxMDUwMDk2.XmBbiQ.IgJ9i8N0Cvy1wwg_xxxjKbvxlUA');
