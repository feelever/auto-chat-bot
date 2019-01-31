import requests
import json
import re
url ="https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
headers['Cookie']="JSESSIONID=E98BA4BB2B7E5C4E03A127E66CC65186; tk=jEGpMZ-MXe3Vj26ObRORe6QzSQaBQxxVxhc1c0; route=6f50b51faa11b987e576cdb301e545c4; RAIL_EXPIRATION=1549218217222; RAIL_DEVICEID=bpcBiHh5zibgyUdv4aHeqmEwaoao3R2-tacRnDUCqhPtft65pRaGX-sZIxB1hdocaktMYtprujs6MyKvvQvuq_Y955WqsaliTNUwm8cviP6Zf8D0XfIpac94wd_6F1GsTR_SZBBBHPc5D0eOaivOUCMzL0s4frE_; BIGipServerpool_passport=367854090.50215.0000; _jc_save_fromStation=%u6CC9%u5DDE%u4E1C%2CQRS; _jc_save_toStation=%u6DF1%u5733%2CSZQ; _jc_save_fromDate=2019-01-31; _jc_save_toDate=2019-01-31; _jc_save_wfdc_flag=dc; BIGipServerotn=32506378.50210.0000"
headers['Referer']="https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
r = requests.get("https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2019-01-31&leftTicketDTO.from_station=QYS&leftTicketDTO.to_station=IOQ&purpose_codes=ADULT",headers=headers)
def get_ticket_info(r):
    try:
        splitarr = str(json.loads(r.text)['data']['result'][1]).split("|")
        return splitarr                
    except:
        pass
    return []
arr = get_ticket_info(r)
print(arr)
if len(arr)>0 and len(arr[0])>0:
    token=arr[0]
    body="?secretStr="+token+"&train_date=2019-02-01&back_train_date=2019-01-31&tour_flag=dc&purpose_codes=ADULT&query_from_station_name=泉州东&query_to_station_name=深圳&undefined"    
    r =requests.post(url+body,headers=headers)
r = requests.post("https://kyfw.12306.cn/otn/confirmPassenger/initDc",headers=headers)
print((r.text))
print((re.match('ticketInfoForPassengerForm=(.*)$',r.text)))
# passengerTicketStr="O%2C0%2C1%2C%E8%94%A1%E6%96%87%E8%BE%BE%2C1%2C35058319981223921X%2C%2CN&oldPassengerStr=%E8%94%A1%E6%96%87%E8%BE%BE%2C1%2C35058319981223921X%2C1_&randCode=&purpose_codes=00&key_check_isChange=2FA7FAA4E059345173C72ABF9FCBDFA533604417E414460B771E42EA&leftTicketStr=hMLrImn8Zg9gEX0HNuLd%252F1xTQgLaKFqDzUJk44eQ1q0zMQPF&train_location=G2&choose_seats=&seatDetailType=000&whatsSelect=1&roomType=00&dwAll=N&_json_att=&REPEAT_SUBMIT_TOKEN=cd8b3a337f0a65676475496102c8df16"
# print(r.text)