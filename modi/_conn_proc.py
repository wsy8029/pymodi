
import time
import asyncio

import threading as th
import multiprocessing as mp

from modi._conn_task import ConnTask
from modi._ser_task import SerTask
from modi._can_task import CanTask
from modi._ble_task import BleTask
from modi._mac_ble_task import MacBleTask


class ConnProc(mp.Process):

    def __init__(self, recv_q, send_q, conn_mode):
        super().__init__()
        self._recv_q = recv_q
        self._send_q = send_q

        #self.__task = self.__init_task(conn_mode)(recv_q, send_q)
        self.__delay = 0.001
    
    def __init_task(self, conn_mode):
        # TODO: Replace if and else branches
        conn_mode_in_lower_case = conn_mode.lower()
        if conn_mode_in_lower_case.startswith("ser"):
            return SerTask
        elif conn_mode_in_lower_case.startswith("can"):
            return CanTask
        elif conn_mode_in_lower_case.startswith("ble"):
            return MacBleTask
        else:
            raise Exception("No connection mode exists for:", conn_mode)

    def run(self):
        #self.__task.open_conn()

        #read_thread = th.Thread(
        #    target=self.__task.run_read_data, args=(self.__delay,)
        #)
        #read_thread.daemon = True
        #read_thread.start()

        #write_thread = th.Thread(
        #    target=self.__task.run_write_data, args=(self.__delay,)
        #)
        #write_thread.daemon = True
        #write_thread.start()

        #read_thread.join()
        #write_thread.join()

        #self.__task.run(), 

        bletask = MacBleTask(self._recv_q, self._send_q)
