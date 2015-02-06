[{'id': 91879,
  'message': 'We may need to add web hosts if this is consistently high.',
  'name': 'Bytes received on host0',
  'options': {'notify_audit': False, 'notify_no_data': False, 'silenced': {}},
  'org_id': 1499,
  'query': 'avg(last_1h):sum:system.net.bytes_rcvd{host:host0} > 100',
  'type': 'metric alert'},
 {'id': 91875,
  'message': u'',
  'name': '**system.net.bytes_rcvd** over **host:host0** was **> 100** on average during the **last 1h**.',
  'options': {'escalation_message': u'',
              'no_data_timeframe': False,
              'notify_audit': True,
              'notify_no_data': False,
              'renotify_interval': None,
              'silenced': {},
              'timeout_h': None},
  'org_id': 1499,
  'query': 'avg(last_1h):sum:system.net.bytes_rcvd{host:host0} > 100',
  'type': 'metric alert'}]