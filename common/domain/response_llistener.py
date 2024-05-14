from typing import Optional, Callable


class ResponseListener:
    def __init__(
        self,
        onSuccess: Callable[[], None],
        onError: Optional[Callable[[str], None]],
        onLoading: Optional[Callable[[bool], None]],
    ):
        self.onSuccess = onSuccess
        self.onError = onError
        self.onLoading = onLoading
        pass
