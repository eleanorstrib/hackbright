import pusher

p = pusher.Pusher(
  app_id='92672',
  key='f6cce36561b80fa77833',
  secret='06ad53f1c6d3eaeaf495'
)
p['test_channel'].trigger('my_event', {'message': 'hello world'})