import os

import pysftp


def sftp_get_txt(file_name, file_dir, remote_file_dir, host, username, password, port):
    '''
    sftp에 있는 txt파일 저장
    :param file_name: 파일명 (확장자 제외)
    :param file_dir: 저장할 주소
    :param remote_file_dir: ftp 파일 주소
    :param host:
    :param username:
    :param password:
    :param port:
    :return:
    '''
    host = host
    username = username
    password = password
    port = port

    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    with pysftp.Connection(host = host, username = username, password = password, cnopts = cnopts) as sftp:
        # print("Connection succesfully stablished ... ")
        remoteFilePath = remote_file_dir + file_name
        localFilePath = os.path.join(file_dir, file_name + '.txt')

        sftp.get(remoteFilePath, localFilePath)
