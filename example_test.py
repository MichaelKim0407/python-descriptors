from example_base_classes import BaseDescriptor, BaseParameterlessProperty


class LoggedField(BaseDescriptor):
    def _get(self, instance):
        print(f'get {self._attr}')
        return instance.__dict__[self._attr]

    def _set(self, instance, value):
        print(f'set {self._attr}')
        instance.__dict__[self._attr] = value

    def _delete(self, instance):
        print(f'delete {self._attr}')
        del instance.__dict__[self._attr]


class WritableCachedProperty(BaseParameterlessProperty):
    def __init__(
            self,
            getter,
            *,
            setter=None,
            deleter=None,
    ):
        if setter is None:
            def setter(instance, value):
                instance.__dict__[self._attr] = value
        if deleter is None:
            def deleter(instance):
                del instance.__dict__[self._attr]

        super().__init__(
            getter=getter,
            setter=setter,
            deleter=deleter,
        )

    def _get(self, instance):
        if self._attr not in instance.__dict__:
            instance.__dict__[self._attr] = super()._get(instance)
        return instance.__dict__[self._attr]


class Test:
    x = LoggedField()

    @WritableCachedProperty
    def y(self):
        return 0


a = Test()
a.x = 10
print(a.x)

print(a.y)
a.y = 20
print(a.y)
del a.y
print(a.y)
