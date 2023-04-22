class BaseDescriptor:
    def __set_name__(self, owner, name):
        self._owner = owner
        self._attr = name

    def _get(self, instance):
        raise NotImplementedError

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self._get(instance)

    def _set(self, instance, value):
        raise NotImplementedError

    def __set__(self, instance, value):
        self._set(instance, value)

    def _delete(self, instance):
        raise NotImplementedError

    def __delete__(self, instance):
        self._delete(instance)


class BaseProperty(BaseDescriptor):
    def __init__(
            self,
            *,
            getter=None,
            setter=None,
            deleter=None,
    ):
        self._getter = getter
        self._setter = setter
        self._deleter = deleter

    def _get(self, instance):
        return self._getter(instance)

    def _set(self, instance, value):
        self._setter(instance, value)

    def setter(self, setter):
        self._setter = setter
        return self

    def _delete(self, instance):
        self._deleter(instance)

    def deleter(self, deleter):
        self._deleter = deleter
        return self


class BaseParameterlessProperty(BaseProperty):
    def __init__(
            self,
            getter,  # assign getter on __init__
            *,
            setter=None,
            deleter=None,
    ):
        super().__init__(
            getter=getter,
            setter=setter,
            deleter=deleter,
        )


class BaseParameterProperty(BaseProperty):
    def __init__(
            self,
            *,
            getter=None,
            setter=None,
            deleter=None,
            **kwargs,  # assign parameters on __init__
    ):
        super().__init__(
            getter=getter,
            setter=setter,
            deleter=deleter,
        )
        self._params = kwargs

    def __call__(self, getter):  # assign getter on __call__
        self._getter = getter
        return self
