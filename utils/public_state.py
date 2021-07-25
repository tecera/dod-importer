class PublicState:
    def __getstate__(self):
        state = self.__dict__.copy()
        try:
            new_items = {key: value for key, value in state.items() if key[0] != "_"}
            return new_items
        except KeyError:
            pass
        return state

    def __setstate__(self, state: dict):
        self.__dict__.update(state)
