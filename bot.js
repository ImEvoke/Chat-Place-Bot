const Discord = require('discord.js');
const client = new Discord.Client();

client.login('NjgzMzgyMjA3NzcxMDUwMDk2.XmBbiQ.IgJ9i8N0Cvy1wwg_xxxjKbvxlUA');

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === '.ping') {
    msg.reply('pong');
  }
});

client.on('message', async message => {
  // Voice only works in guilds, if the message does not come from a guild,
  // we ignore it
  if (!message.guild) return;

  if (message.content === '.join') {
    // Only try to join the sender's voice channel if they are in one themselves
    if (message.member.voice.channel) {
      const connection = await message.member.voice.channel.join();
    } else {
      message.reply('You need to join a voice channel first!');
    }
  }
});
