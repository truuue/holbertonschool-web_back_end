import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
};

const displaySchoolValue = async (schoolName) => { // async function to display the value of a school
  const getAsync = promisify(client.get).bind(client); // promisify the get function of the client
  const reply = await getAsync(schoolName); // get the value of the schoolName
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');