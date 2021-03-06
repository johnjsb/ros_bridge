"""Copyright 2012, System Insights, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License."""
    
import sys, os, time

path, file = os.path.split(__file__)
sys.path.append(os.path.realpath(path) + '/../src')

from data_item import Event, SimpleCondition, Sample
from mtconnect_adapter import Adapter

if __name__ == "__main__":
    adapter = Adapter(('localhost', 7878))
    e1 = Event('e1')
    adapter.add_data_item(e1)
    c1 = SimpleCondition('c1')
    adapter.add_data_item(c1)
    s1 = Sample('s1')
    adapter.add_data_item(s1)
    adapter.start()

    while True:
        adapter.begin_gather()
        e1.set_value(1)
        s1.set_value(200.1)
        adapter.complete_gather()
        time.sleep(1.0)

        adapter.begin_gather()
        c1.add('fault', 'A fault', '123')
        e1.set_value(2)
        adapter.complete_gather()
        time.sleep(1.0)

        adapter.begin_gather()
        c1.add('fault', 'Another fault', '124')
        e1.set_value(3)
        adapter.complete_gather()
        time.sleep(1.0)

        adapter.begin_gather()
        c1.remove('123')
        e1.set_value(4)
        s1.set_value(300.1)
        adapter.complete_gather()
        time.sleep(1.0)

        adapter.begin_gather()
        c1.remove('124')
        e1.set_value(5)
        s1.set_value(500.1)
        adapter.complete_gather()
        time.sleep(1.0)
