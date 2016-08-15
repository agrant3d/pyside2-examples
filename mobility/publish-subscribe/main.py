#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#
# Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
# All rights reserved.
# Contact: Nokia Corporation (qt-info@nokia.com)
#
# This file is a port of the Qt Mobility Examples
#
# $QT_BEGIN_LICENSE:BSD$
# You may use this file under the terms of the BSD license as follows:
#
# "Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
#     the names of its contributors may be used to endorse or promote
#     products derived from this software without specific prior written
#     permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
# $QT_END_LICENSE$
#
###############################################################################

import sys

from PySide.QtGui import QApplication
from QtMobility.PublishSubscribe import QValueSpace

try:
    from Qt import QtMaemo5
    USE_MAEMO_5 = True
except:
    USE_MAEMO_5 = False

from publisherdialog import PublisherDialog
from subscriberdialog import SubscriberDialog

def main():
    app = QApplication(sys.argv)

    if '-server' in sys.argv:
        QValueSpace.initValueSpaceServer()

    createPublisher = '-publisher' in sys.argv
    createSubscriber = '-subscriber' in sys.argv
    createDefault = not (createPublisher or createSubscriber)

    publisher = None
    if createDefault or createPublisher:
        publisher = PublisherDialog()
        publisher.rejected.connect(app.quit)
        if not USE_MAEMO_5:
            publisher.show()

    subscriber = None
    if createDefault or createSubscriber:
        subscriber = SubscriberDialog()
        subscriber.rejected.connect(app.quit)
        if USE_MAEMO_5:
            subscriber.showMaximized()
        else:
            subscriber.show()


    if USE_MAEMO_5:
        publisher.switchRequested.connect(subscriber.showMaximized)
        publisher.switchRequested.connect(subscriber.repaint)
        publisher.switchRequested.connect(subscriber.hide)

        subscriber.switchRequested.connect(publisher.showMaximized)
        subscriber.switchRequested.connect(publisher.repaint)
        subscriber.switchRequested.connect(publisher.hide)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

