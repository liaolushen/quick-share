export const addOne = ({ dispatch }) => {
  dispatch('ADD');
};

export const sendMessage = ({ dispatch }, message) => {
  dispatch('SEND_MESSAGE', message);
};
