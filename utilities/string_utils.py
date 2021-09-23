import phonenumbers

from common_tools.logger.logger import Logger


class StringUtil:
    '''
    문자열 관련 유틸

    '''

    log = Logger().get_file_logger().getLogger()

    @classmethod
    def hide_str(cls, string:str, length:int):
        '''
        문자열의 마지막부터 숨길 글자수 만큼 *로 변환한다.
        :param string: 문자열
        :param length: 숨길 글자 수
        :return:
        '''
        if string and len(string) >= length:
            _string = string[:-length]
            return _string.ljust(len(string), '*')

    @classmethod
    def str_to_phonenum(cls, phone_num: str):
        '''
        연속된 휴대폰 번호를 구분자를 넣어 반환한다.

        01012341234 -> 010-1234-1234
        :param phone_num: 구분자 없는 핸드폰 번호
        :return:
        '''
        _pn = phonenumbers.parse(phone_num, 'KR')
        return phonenumbers.format_number(_pn, phonenumbers.PhoneNumberFormat.NATIONAL)


if __name__ == '__main__':
    pn = '01012341234'
    pn2 = '15441881'
    print(StringUtil.str_to_phonenum(pn))
    print(StringUtil.str_to_phonenum(pn2))
    print(StringUtil.hide_str(pn, 4))
