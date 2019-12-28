import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys
import json
from datetime import datetime


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path[0:7] == '/?year=':  # 1 task processing
            try:
                year = int(self.path[7:])
            except:
                self._full_send(1, "BAD YEAR NUMBER")
                return

            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                self._full_send(200, "12/09/%d" % year)
            else:
                self._full_send(200, "13/09/%d" % year)


        elif self.path[0:14] == '/?currentDate=' and len(self.path[0:]) == 22:  # 2 task prorcessing

            try:
                day = int(self.path[14:16])
                month = int(self.path[16:18])
                year = int(self.path[18:22])
                print("%d.%d.%d" % (day, month, year))

            except:
                self._full_send(1, "BAD YEAR NUMBER")
                return

            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                prog_day = datetime(day=12, month=9, year=int(year))
            else:
                prog_day = datetime(day=13, month=9, year=int(year))

            passed_date = datetime(day=day, month=month, year=year)
            result_day = prog_day - passed_date
            self._full_send(200, result_day.days)

        else:
            self._full_send(2, "BAD REQUEST")

    def _full_send(self, errorCode, dataMessage):
        self.send_response(200)
        self.send_header('content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps({"errorCode": errorCode, "dataMessage": dataMessage}).encode())


def signal_handler(sig, frame):
    print('Exiting server')
    sys.exit(0)


def main():
    port = 8080

    print("Starting simple http server...")

    signal.signal(signal.SIGINT, signal_handler)
    print("SIGINT handler created")

    serv = HTTPServer(('', port), HttpProcessor)
    print("Requests expected on %d port\nRunning server..." % port)

    serv.serve_forever()


if __name__ == '__main__':
    main()
