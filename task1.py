import datetime


class Customer:
    def __init__(self, id: int):
        """
        Initialize base customer object

        :id: id of new customer
        """
        self.id = id
        self.registration_date = datetime.date.today()
        self._purchases = []

    @property
    def purchases(self) -> list:
        return self._purchases

    @purchases.setter
    def purchases(self, new_order: list[int]) -> None:
        """
        extend list of purchases by new order
        if total number of purchases is enough -> update Customer to VIPCustomer

        :new_order: list of ids of ordered goods
        """
        self._purchases.extend(new_order)

        if len(self._purchases) >= 20:
            print(f'{datetime.datetime.now()}   Updating Customer {self.id} to VIPCustomer')
            ...

    def __str__(self) -> str:
        return f'Customer id: {self.id}, VIP: no'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id!r})'


class VIPCustomer(Customer):
    def __init__(self, id: int):
        """
        Initialize VIPCustomer object
        Child of Customer class

        overloading reason: new attribute

        :id: id of new VIPCustomer object
        """
        super().__init__(id)
        self.price_mult = 0.85

    def purchases(self, new_order: list[int]) -> None:
        """
        extend list of purchases by new order

        overloading reason: not needed to check VIP requirements anymore

        :new_order: list of ids of ordered goods
        """
        self._purchases.extend(new_order)

    def talk_to_manager(self, message: str) -> None:
        """
        send message to manager

        :message: customer message to send
        """
        ...

    def __repr__(self) -> str:
        """
        overloading reason: changes in VIP part of returning str
        """
        return f'Customer id: {self.id}, VIP: yes'
