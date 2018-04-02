class Status(object):

    status_sort = {'created':1, 'paid':2, 'delivery':3, 'confirmed':4}
    CREATED_NOT_PAID = 'create'
    PAID_NOT_DILIVERY = 'paid'
    DELIVERY_NOT_CONFIRMED = 'delivery'
    CONFIRMED = 'confirmed'
    CANCELED = 'canceled'

    @classmethod
    def check_status(self, status_new, status_old):
        if status_new != CANCELED:
            return True if (self.status_sort[status_new] - self.status_sort[status_old]) == 1 else False
        else:
            return False

    @classmethod
    def check_canceled(self, order, status):
        if status == CREATED_NOT_PAID:
            order.status = CANCELED
            order.save()
            return True
        elif status == CONFIRMED:
            return False
        elif status == PAID_NOT_DILIVERY:
            order.status =9 

