import ClassRoom from './0-classroom.js';

function initializeRooms() {
  const rooms = [];
  rooms.push(new ClassRoom(19));
  rooms.push(new ClassRoom(20));
  rooms.push(new ClassRoom(34));
  return rooms;
}

export default initializeRooms;
