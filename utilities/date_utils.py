import locale
import datetime
from dateutil.relativedelta import relativedelta
import holidays

from common_tools.logger.logger import Logger


class DateUtil:
    '''
    날짜 관련 util

    '''
    DATEPATTERN_DATE = '%Y%m%d'
    DATEPATTERN_TIME = '%H%M%S'
    DATEPATTERN_DATETIME = '%Y%m%d%H%M%S'
    DATEPATTERN_DATETIMEMS = '%Y%m%d%H%M%S%f'

    log = Logger().get_file_logger().getLogger()

    @classmethod
    def get_now(cls, **kwargs):
        '''
        현재 년월일 시분초를 %Y%m%d%H%M%S 패턴으로 반환한다.
        :param kwargs: pattern : 현재 년월일 시분초를 패턴에 맞는 문자열 날짜로 반환한다.
        :return:
        '''
        for key, value in kwargs.items():
            if 'pattern'.upper() == key.upper():
                pattern = value
                return cls.datetime_to_str(datetime.datetime.now(), pattern)
            else:
                return cls.datetime_to_str(datetime.datetime.now(), cls.DATEPATTERN_DATETIME)

    @classmethod
    def get_today(cls, **kwargs):
        '''
        오늘 날짜를 %Y%m%d 패턴으로 반환한다.
        :param kwargs: pattern : 오늘 날짜를 패턴에 맞는 문자열 날짜로 반환한다.
        :return:
        '''
        for key, value in kwargs.items():
            if 'pattern'.upper() == key.upper():
                pattern = value
                return cls.datetime_to_str(datetime.date.today(), pattern)
            else:
                return cls.datetime_to_str(datetime.date.today(), cls.DATEPATTERN_DATE)

        return cls.datetime_to_str(datetime.date.today(), cls.DATEPATTERN_DATE)

    @classmethod
    def datetime_to_str(cls, dt: datetime, pattern: str):
        '''
        datetime 타입의 날짜를 패턴에 맞는 문자열 타입의 날짜로 반환한다.
        :param dt: datetime
        :param format: 문자열 날짜 패턴
        :return:
        '''
        try:
            if not dt:
                return None
            return dt.strftime(pattern)
        except Exception as e:
            cls.log.error(f'Error : {e}')
            return None

    @classmethod
    def str_to_datetime(cls, str_dt: str, str_pattern: str):
        '''
        문자열 타입의 날짜를 datetime 타입의 날짜로 반환한다.
        :param str_dt: 문자열 날짜
        :param str_pattern: 문자열 날짜 패턴
        :return:
        '''
        try:
            return datetime.datetime.strptime(str_dt, str_pattern)
        except Exception as e:
            cls.log.error(f'Error : {e}')
            return None

    @classmethod
    def add_delimeter(cls, str_dt: str, delimeter: str):
        '''
        날짜 구분자를 추가하여 반환한다.
        :param str_dt: 문자열 날짜
        :param delimeter: 날짜 구분자
        :return:
        '''
        if str_dt and len(str_dt) == 8 and delimeter:
            date_str = str_dt[:4] + delimeter + str_dt[4:6] + delimeter + str_dt[6:]
            return date_str

    @classmethod
    def remove_delimeter(cls, str_dt: str):
        '''
        날짜 구분자를 제거하여 반환한다.
        :param str_dt: 문자열 날짜
        :return:
        '''
        if str_dt and len(str_dt) == 10:
            date_str = str_dt[:4] + str_dt[5:7] + str_dt[8:]
            return date_str

    @classmethod
    def replace_delimeter(cls, str_dt: str, delimeter: str):
        '''
        날짜 구분자를 변경하여 반환한다.
        :param str_dt: 문자열 날짜
        :param delimeter: 날짜 구분자
        :return:
        '''
        if str_dt and len(str_dt) == 10 and delimeter:
            date_str = str_dt[:4] + delimeter + str_dt[5:7] + delimeter + str_dt[8:]
            return date_str

    @classmethod
    def add_year_month_day(cls, str_dt: str, year: int, month: int, day: int):
        '''
        %Y%m%d 형식의 문자열 날짜를 입력 받아 년(year),월(month),일(day)을 가감한다.
        :param str_dt: 문자열 날짜
        :param year: 가감할 년
        :param month: 가감할 월
        :param day: 가감할 일
        :return:
        '''
        try:
            dt_obj = cls.str_to_datetime(str_dt, cls.DATEPATTERN_DATE)

            if year:
                dt_obj = dt_obj + relativedelta(years = year)
            if month:
                dt_obj = dt_obj + relativedelta(months = month)
            if day:
                dt_obj = dt_obj + relativedelta(days = day)

            return cls.datetime_to_str(dt_obj, cls.DATEPATTERN_DATE)

        except Exception as e:
            cls.log.error(f'Error : {e}')
            return str_dt

    @classmethod
    def add_year(cls, str_dt: str, year: int):
        '''
        %Y%m%d 형식의 문자열 날짜를 입력 받아 년(year)을 가감한다.
        :param str_dt: 문자열 날짜
        :param year: 가감할 년
        :return:
        '''
        return cls.add_year_month_day(str_dt, year, 0, 0)

    @classmethod
    def add_month(cls, str_dt: str, month: int):
        '''
        %Y%m%d 형식의 문자열 날짜를 입력 받아 월(month)을 가감한다.
        :param str_dt: 문자열 날짜
        :param month: 가감할 월
        :return:
        '''
        return cls.add_year_month_day(str_dt, 0, month, 0)

    @classmethod
    def add_day(cls, str_dt: str, day: int):
        '''
        %Y%m%d 형식의 문자열 날짜를 입력 받아 일(day)을 가감한다.
        :param str_dt: 문자열 날짜
        :param day: 가감할 일
        :return:
        '''
        return cls.add_year_month_day(str_dt, 0, 0, day)

    @classmethod
    def dt_to_weekday(cls, str_dt: str, kor = False):
        '''
        %Y%m%d 형식의 문자열 날짜를 해당하는 요일로 반환한다.
        :param str_dt: 문자열 날짜
        :param kor: False - 영어 , True - 한국어
        :return:
        '''
        _days = ['월', '화', '수', '목', '금', '토', '일']
        dt_obj = cls.str_to_datetime(str_dt, cls.DATEPATTERN_DATE)

        if kor:
            return _days[dt_obj.weekday()] + '요일'
        else:
            return dt_obj.strftime('%A')

    @classmethod
    def get_date_diff(cls, str_dt1: str, str_dt2: str):
        '''
        %Y%m%d 형식의 문자열 날짜 str_dt1과 str_dt2 사이의 일 수를 구한다.
        :param str_dt1: 문자열 날짜 1
        :param str_dt2: 문자열 날짜 2
        :return:
        '''
        _date1 = cls.str_to_datetime(str_dt1, cls.DATEPATTERN_DATE)
        _date2 = cls.str_to_datetime(str_dt2, cls.DATEPATTERN_DATE)

        if _date1 and _date2:
            diff = _date1 - _date2
            return diff.days
        else:
            return 0


if __name__ == '__main__':
    DATEPATTERN_DATE = '%Y%m%d'
    DATEPATTERN_TIME = '%H%M%S'
    DATEPATTERN_DATETIME = '%Y%m%d%H%M%S'
    DATEPATTERN_DATETIMEMS = '%Y%m%d%H%M%S%f'

    # _today = utilities.date.today()
    # _now = utilities.utilities.now()
    # _hour = utilities.time.hour
    #
    # print(f'_today = {_today}')
    # print(f'_now = {_now}')
    # print(f'_hour = {_hour}')

    print(DateUtil.get_now())
    print(DateUtil.get_today())
    print(DateUtil.get_today(pattern = DATEPATTERN_DATETIME))
    print(DateUtil.str_to_datetime('20210923', DATEPATTERN_DATE))
    print(DateUtil.add_delimeter('20210923', '-'))
    print(DateUtil.remove_delimeter('2021/09/23'))
    print(DateUtil.replace_delimeter('2021/09/23', '-'))
    print(DateUtil.add_year_month_day('20210923', 1, 1, 1))
    print(DateUtil.dt_to_weekday('20210923'))
    print(DateUtil.get_date_diff('20060228', '20060310'))
