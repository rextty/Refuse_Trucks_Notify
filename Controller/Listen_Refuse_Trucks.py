def start(self):
    while 1:
        if datetime.date.today().isoweekday() is 1 or 2 or 4 or 5:
            if self.checkTimeInRange('16 30', '17 05'):
                rs = requests.post(url=self.url, data=self.data, headers=self.headers)
                jData = json.loads(rs.content.decode())
                for data in jData:
                    if data["RouteID"] == '55':
                        result = self.checkCoordinateInRange(self.coordinateRange[0],
                                                             self.coordinateRange[1],
                                                             self.coordinateRange[2],
                                                             self.coordinateRange[3],
                                                             data["CarLat"], data["CarLon"])
                        if result:
                            winsound.MessageBeep(20)
                            self.tk.showNotify('垃圾車通知', '你差不多該出門了')
                            time.sleep(5)
                            winsound.MessageBeep(20)
                            self.tk.showNotify('垃圾車通知', '你差不多該出門了')
                            return 1
                        break
                time.sleep(8)
            else:
                time.sleep(5)
        else:
            break