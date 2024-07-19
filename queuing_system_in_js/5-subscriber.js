import redis from 'redis';

const subscriber = redis.createClient(); // Create a Redis subscriber

subscriber.on('error', (error) => { // Log an error if the client is not connected to the server
  console.log(`Redis client not connected to the server: ${error.message}`);
});

subscriber.on('connect', () => { // Log a message when the client is connected to the server
  console.log('Redis client connected to the server');
});

const CHANNEL = 'holberton school channel'; // Define the channel name

subscriber.subscribe(CHANNEL); // Subscribe to the channel

subscriber.on('message', (channel, message) => { // Log the message when a message is received
  if (channel === CHANNEL) console.log(message);
  // Log the message if the channel is the same as the defined channel

  if (message === 'KILL_SERVER') { // Unsubscribe from the channel and quit the subscriber if the message is 'KILL_SERVER'
    subscriber.unsubscribe(CHANNEL); // Unsubscribe from the channel
    subscriber.quit(); // Quit the subscriber
  }
});