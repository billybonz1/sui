import pyautogui
from datetime import datetime
import json
import requests
import asyncio
import os
import openai
import json
from types import SimpleNamespace

async def read_digits():

    

    openai.api_key = "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"


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
                {"role": "system", "content": "Ты будешт играть в игру 2048. Ты будешь получать json массив данных игры и тебе нужно будет вернуть json массив с указанием стороны движения."},
                {"role": "user", "content": "Я даю json массив данных игры: [[2,128,64,4],[8,256,8,0],[4,32,0,0],[16,4,0,0]]"},
                {"role": "user", "content": "Определи пожалуйста правильную сторону движения и верни в формате JSON и верни только его: {\"direction\": \"right or left or up or down\"}"}
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    # detect json in string result
    result = result[result.find('{'):result.rfind('}')+1]
    # parse json to object
    x = json.loads(result, object_hook=lambda d: SimpleNamespace(**d))

    print(x)

    pyautogui.screenshot('screenshot.png')
    # find image on another image
    r32 = pyautogui.locateOnScreen('32.png')
    # python console log

    
    print(result)


async def click_upscale(clickCounter = 0, needScroll = True, element = None):
    if clickCounter == 0:
        sleep = 10
    else:
        sleep = 2
    

    if element is not None:
        pyautogui.click(element.left + (100*(clickCounter-1)), element.top + 20)
        pyautogui.sleep(sleep)
        needScroll = False
        clickCounter += 1
    else:    
        result = pyautogui.locateAllOnScreen('btn.png')
        count = 0
        resultArr = []
        for i in result:
            count += 1
            resultArr.append(i)
        
        offset = 0
        if count > (9 - clickCounter):
            offset = count - (9 - clickCounter)

        print(offset, clickCounter)

        # exit()
        print(resultArr)

        # if isset resultArr[offset] then click

        if len(resultArr) > 0:  
            pyautogui.click(resultArr[offset])
            pyautogui.click(resultArr[offset].left + 500, resultArr[offset].top)
            pyautogui.sleep(sleep)
            if needScroll:
                pyautogui.scroll(300)
            needScroll = False
            pyautogui.sleep(sleep)
            clickCounter += 1
            if clickCounter >= 2:
                element = resultArr[offset]

        
    if clickCounter <= 3:
        await click_upscale(clickCounter, needScroll, element)



async def main():
    await read_digits()


asyncio.run(main())

# click_upscale()

# type_message('male archangel for 2d platformer game digital art')

# get_channel_history()

# python wait 3 seconds
#pyautogui.sleep(3)

#console.log(pyautogui.position())
#pyautogui.click(100, 100)

