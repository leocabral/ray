
import peewee
from peewee import Model as PeeweeNativeModel
from ray.model import Model as BaseModel
from ray import exceptions


class PeeweeModel(PeeweeNativeModel, BaseModel):

    def describe(self):
        raise NotImplementedErrorls

    @classmethod
    def columns(cls):
        return sorted([c.name for c in cls._meta.sorted_fields])

    @classmethod
    def find(cls, *args, **kwargs):
        query = cls.select()
        for field, value in kwargs.items():
            query = query.where(getattr(cls, field) == value)

        return query

    @classmethod
    def get(cls, id=None):
        try:
            return super(PeeweeModel, cls).get(cls.id == int(id))
        except:
            return None

    def update(self, fields_to_update):
        model_id = fields_to_update['id']
        del fields_to_update['id']

        model_class = self.__class__

        query = super(PeeweeModel, self).update(**fields_to_update)
        query = query.where(model_class.id == model_id)
        query.execute()

        for field, value in fields_to_update.items():
            setattr(self, field, value)

        return self

    def put(self):
        super(PeeweeModel, self).put()
        self.save()
        return self

    def delete(self, model_id=None):
        query = super(PeeweeModel, self).delete().where(self.__class__.id == model_id)
        query.execute()
        return self

