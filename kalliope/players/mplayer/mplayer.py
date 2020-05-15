import logging
import os
import subprocess

logging.basicConfig()
logger = logging.getLogger("kalliope")

MPLAYER_EXEC_PATH = "/usr/bin/mplayer"


class Mplayer(object):
    """
    This Class is representing the MPlayer Object used to play the all sound of the system.
    """

    def __init__(self, **kwargs):
        logger.debug("[Mplayer.__init__] instance")
        logger.debug("[Mplayer.__init__] args : %s " % str(kwargs))

    @classmethod
    def play(cls, filepath):
        """
        Play the sound located in the provided filepath

        :param filepath: The file path of the sound to play
        :type filepath: str

        :Example:

            Mplayer.play(self.file_path)

        .. seealso::  TTS
        .. raises::
        .. warnings:: Class Method and Public
        """

        # we try to get the path from the env
        mplayer_exec_path = cls._get_mplayer_path()
        # if still None, we set a default value
        if mplayer_exec_path is None:
            mplayer_exec_path = MPLAYER_EXEC_PATH

        mplayer_options = ['-slave', '-quiet']
        mplayer_command = list()
        mplayer_command.extend([mplayer_exec_path])
        mplayer_command.extend(mplayer_options)

        mplayer_command.append(filepath)
        logger.debug("Mplayer cmd: %s" % str(mplayer_command))

        fnull = open(os.devnull, 'w')

        subprocess.call(mplayer_command, stdout=fnull, stderr=fnull)

    @staticmethod
    def _get_mplayer_path():
        prog = "mplayer"
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, prog)
            if os.path.isfile(exe_file):
                return exe_file
        return None
