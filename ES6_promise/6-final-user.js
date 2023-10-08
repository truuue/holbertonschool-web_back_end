import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(filename)])
    .then((results) => {
      const resultsArray = [];
      results.forEach((result) => {
        resultsArray.push({
          status: result.status,
          value: result.status === 'fulfilled' ? result.value : `${result.reason.name}: ${result.reason.message}`,
        });
      });
      return resultsArray;
    });
}
