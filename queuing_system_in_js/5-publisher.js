import redis from 'redis';

const publisher = redis.createClient(); // Create a Redis publisher

publisher.on('error', (error) => { // Log an error if the client is not connected to the server
  console.log(`Redis client not connected to the server: ${error.message}`);
});

publisher.on('connect', () => { // Log a message when the client is connected to the server
  console.log('Redis client connected to the server');
});

const CHANNEL = 'holberton school channel'; // Define the channel name

function publishMessage(message, time) { // Publish a message after a specified time
  setTimeout(() => { // Set a timeout for the message
    console.log(`About to send ${message}`);
    publisher.publish(CHANNEL, message); // Publish the message to the channel
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);