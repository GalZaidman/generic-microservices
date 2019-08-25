from sqlalchemy import Table, Column, Boolean, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# from sqlalchemy.ext.hybrid import hybrid_property, Comparator


Base = declarative_base()

users_roles = Table(
    'users_roles',
    Base.metadata,
    Column('user_id' ,String(200), ForeignKey('users.user_id')),
    Column('role_id' ,String(200), ForeignKey('roles.role_id'))
)


roles_permissions = Table(
    'roles_permissions',
    Base.metadata,
    Column('role_id' ,String(200), ForeignKey('roles.role_id')),
    Column('permission_id' ,String(200), ForeignKey('permissions.permission_id'))
)


class User(Base):
    __tablename__ = 'users'
    # Table Columns
    user_id = Column(String(200), primary_key=True)
    username =  Column(String(300), nullable=False, unique=True)
    email = Column(String(500),nullable=False, unique=True)
    _password = Column(String(500), nullable=False)
    first_name = Column(String(500))
    last_name = Column(String(500))
    authenticated = Column(Boolean, default=False)
    signed_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    Column('role_id', String(200, nullable=False), ForeignKey("roles.role_id", onupdate='CASCADE'))
    # Relations
    roles = relationship(
        "Role",
        secondary=users_roles,
        backref=backref("users")
    )        

    def __repr__(self):
        return "User(username='{self.username}', " \
                        "email='{self.email}', " \
                        "first_name='{self.first_name}', " \
                        "last_name={self.last_name}, " \
                        "authenticated={self.authenticated}) " \
                        "signed_on={self.signed_on}) " \
                        "updated_on={self.updated_on})" \
                        .format(self=self)


class Role():
    __tablename__ = 'roles'
    # Table Columns
    role_id = Column(String(200), primary_key=True)
    name = Column(String(200))
    # Relations
    permissions = relationship(
        "Permission",
        secondary=users_roles,
        backref=backref("roles")
    )

    def __repr__(self):
        return "Role(name='{self.name}', " \
                        .format(self=self)

class Permission():
    __tablename__ = 'permissions'
    permission_id = Column(String(200), primary_key=True)
    name = Column(String(200))

    def __repr__(self):
        return "Permission(name='{self.name}', " \
                        .format(self=self)


class Users_DB():
    def __init__(self, connection, *args, **kwargs):
        #Fill in the postgrass connection info
        engine = create_engine("postgresql://scott:tiger@localhost/test")
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)

    
    def add_user(self, user):
        pass

    def delete_user(self, user_id):
        pass

    def update_user(self, new_user):
        pass

    def add_role(self, role):
        pass

    def delete_role(self, role_id):
        pass

    def update_role(self, new_role):
        pass

    def add_permission(self, permission):
        pass

    def delete_permission(self, permission_id):
        pass

    def update_permission(self, new_permission):
        pass





