export const addOne = ({ dispatch }) => {
  dispatch('ADD');
};

export const sendMessage = ({ dispatch }, message) => {
  dispatch('SEND_MESSAGE', message);
};

export const updatePadding = ({ dispatch }, newVal) => {
  dispatch('UPDATE_PADDING', newVal);
};