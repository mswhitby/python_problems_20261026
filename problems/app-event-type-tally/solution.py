def solution(events):
    event_dict = {
        'click': 0,
        'view': 0,
        'submit': 0,
    }
    
    # Write your code here.
    for e in events:
        print(event_dict.get(e.lower()))
        e = e.lower()
        event_dict[e] += 1
        
    return event_dict
