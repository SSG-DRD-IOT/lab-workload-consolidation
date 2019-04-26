"""
Copyright (c) 2018 Intel Corporation.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""Visual trigger for PCB anomaly detection.
"""
import logging
from . import BaseTrigger


class Trigger(BaseTrigger):
    """PCB anomaly detection trigger object.
    """

    def __init__(self):
        """Constructor.
        """
        super(Trigger, self).__init__()
        self.log = logging.getLogger(__name__)
        # Flag to lock trigger from forwarding frames to classifier
        self.trigger_lock = False
        # count frames when trigger is locked
        self.lock_frame_count = 0
        self.count = 0

    def get_supported_ingestors(self):
        return ['video', 'video_file']


    def on_data(self, ingestor, data):
        """Process video frames as they are received and call the callback
        registered by the `register_trigger_callback()` method if the frame
        should trigger the execution of the classifier.

        Parameters
        ----------
        ingestor : str
            String name of the ingestor which received the data
        data : tuple
            Tuple of (camera serial number, camera frame)
        """

        if self.trigger_lock is False:
            # Send trigger start signal and send frame to classifier
            self.send_start_signal(data, -1)
            self.log.info("Sending frame")
            self.send_data(data, 1)
            # Send trigger stop signal and lock trigger
            self.send_stop_signal()
            self.trigger_lock = True
            # Re-initialize frame count during trigger lock to 0
            self.lock_frame_count = 0
        else:
        # Increment frame count during trigger lock phase
            self.lock_frame_count = self.lock_frame_count + 1
            if self.lock_frame_count == 7:
                # Clear trigger lock after timeout
                # period (measured in frame count here)
                self.trigger_lock = False
