from flask_table import Table, Col, LinkCol


class Results(Table):
    user_id = Col('Id', show=False)
    Date_of_Record = Col('Date_of_Record')
    No_of_Deaths = Col('No_of_Deaths')
    No_of_Discharge = Col('No_of_Discharge')
    No_of_Negative = Col('No_of_Negative')
    No_of_Positive = Col('No_of_Positive')
    No_of_Samples = Col('No_of_Samples')
    State_Name = Col('State_Name')
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))
