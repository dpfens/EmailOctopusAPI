from datetime import datetime

class EmailOctopusClientException(Exception):
    def __init__(self, message, status_code=None):
        self.message = message
        self.status_code = status_code
        
    def __str__(self):
        if self.status_code:
            return "(%s) %s" % (self.status_code, self.message)
        else:
            return self.message
        
class EmailOctopusAPIException(Exception):
    def __init__(self, message, error_type, status_code=None):
        self.status_code = status_code
        self.error_type = error_type
        self.message = message
        
    def __str__(self):
        if self.status_code:
            return "(%s) %s" % (self.status_code, self.message)
        else:
            return self.message
        
class EOListMember(object):
    
    def __init__(self, id, email_address, first_name, last_name, subscribed=False, created_at=datetime.now()):
        self.id = id
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.subscribed = subscribed
        self.created_at = created_at
        
    def __str__(self, *args, **kwargs):
        return "(%s) %s %s" % (self.id, self.first_name, self.last_name)
    
    @classmethod        
    def from_dict(cls, data):
        return cls(data['id'], data['email_address'], data['first_name'], data['last_name'], data['subscribed'], data['created_at'])

class EOList(object):
    
    def __init__(self, id, name,created_at=datetime.now()):
        self.id = id
        self.name = name
        self.created_at = created_at
        
    def __str__(self, *args, **kwargs):
        return "(%s) %s" % (self.id, self.name)
    
    def __iter__(self):
        for i in self.arr:
            yield i
    
    @classmethod        
    def from_dict(cls, data):
        return cls(data['id'], data['name'], data['created_at'])