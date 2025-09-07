import json
class dataJson:

    def employeeInformation(self):
        data ="{\"firstName\":\"Diego\",\"lastName\":\"Gutierrez\",\"dependants\":1}"
        return data


    def employeeinformationUpdate(id):
        payload_str = "{\"id\":\"71b6af07-399c-429f-b27a-c35d0b6ea9d3\",\"firstName\":\"Steve1\",\"lastName\":\"Rogers\",\"dependants\":1}"
        payload_dict = json.loads(payload_str)
        payload_dict["id"] = id
        updated_payload_str = json.dumps(payload_dict)
        return updated_payload_str

    def employeeInformationHeaders(self):
       headers= {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4',
            'content-type': 'application/json; charset=UTF-8',
            'origin': 'https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com',
            'priority': 'u=1, i',
            'referer': 'https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Benefits',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': '.AspNetCore.Antiforgery.AsW4q1BB7-Y=CfDJ8H7b2M_BaNZLpuabQBmUpwEohWgUaWXpuiuivU8oYsq6xhTA9KFzPH4Tz4x4z-yPEvTO-bmsVB4MY2ya70EbVO98OmpD4XogNGPLpweSyKeybnphJeWeqpmFuG74VGusYYIuC2TtIm-VmJxH9uZ36yw; .AspNetCore.Cookies=CfDJ8H7b2M_BaNZLpuabQBmUpwFgSg8JNsFVrOwy3ZTWtld1b9OjpsRf2Opd32ipSP75L820YrffpmPSRIl0JEurq8fb8jHaLXC5dIVZDipglJTt9geDtVygpbco13L9DtynTNfOdiuJWzJJ5hoKkUeaSj14oe5xeatNQmyynXkrNV3-U9sZIQBw9MQtVbMXdmQUjjODUXoZ81j-65uvRxTKO4nIMnZSoNOglJs9ipox6T02ut_rWiQ174XI-pg2Y_tMMe35d7i7nObyO_XElN2UVrnfzvisQPqr2VzNO6OmmY5Z',
            'Authorization': 'Basic VGVzdFVzZXI3OTc6VCR9bmVsREw4ayNR'
        }
       return  headers

    def employeeeheadersupdate(self):
        headers= {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com',
                'priority': 'u=1, i',
                'referer': 'https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Benefits',
                'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
                'Cookie': '.AspNetCore.Antiforgery.AsW4q1BB7-Y=CfDJ8Bzw2F44xfFCsXkqkeGRkKOYrC5rn4uTZynTnmOvNoOR4C8oELEVCxZ7hmWddMU-99WkiXp32Wz4bMftEO-JZzkx3oKuTvORDMqdioadoaDzfl6Nae0CF4lnFXiv_tn-jDG0CSF9Izb8a-ab8a8vKZw; .AspNetCore.Cookies=CfDJ8Bzw2F44xfFCsXkqkeGRkKOpS7MY9i2KaaiULb0imh3fcXivM_irXIc4M86iSS1jjkxWJVsL83k8PGSezRnz7VG7AhLuAr1YGcnp_TjAUoUZs6mcThR-BaHx5dc4M8CS58dmC9pIdTp8E1TgzchD_mboK8MN0cEemAbY3gZdFV4C9WMpvRJ0vfXUWnFdZzpcLIu42IiJlsyDi6Jt6gwX_RZ3Xj-LIMOdbUuhyYdja_cWT3mzUUGkGDzJ1KxrrPm5mVkkACOI6NR9InUjX-Su0hVuNxQz-wifYs_F74AQgSbr'
            }
        return headers