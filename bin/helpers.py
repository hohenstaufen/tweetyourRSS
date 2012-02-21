def unitn_science(timestamp_field, history):
    '''
    custom function for UNITN_SCIENCE rss feed. You can use this one as a
    sample
    '''
    current_timestamp = timestamp_field[-4:]
    if int(current_timestamp) > int(history):
        return current_timestamp
    else:
        return history
