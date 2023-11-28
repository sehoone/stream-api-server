import asyncio
import json
import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response, StreamingResponse

app = FastAPI()

# def fake_data_streamer():
#     for i in range(10):
#         yield f"some fake data{i}\n\n"
#         time.sleep(1)

def fake_data_json():
    output = next(fake_dummy_data8())
    ret = {"text": output}
    outputJson = json.dumps(ret)
    yield f"{outputJson}"

def fake_data_streamer():
    func_name = "fake_dummy_data"
    for i in range(7):
        call_func = func_name + str(i+1)
        output = next(globals()[call_func]())
        ret = {"text": output}
        outputJson = json.dumps(ret)
        yield f"{outputJson}\n\n"
        time.sleep(1)

def fake_dummy_data1():
    yield f"Input:\n\n* xml_data: a string containing the XML data to be parsed\n\nOutput:\n\n*"

def fake_dummy_data2():
    yield f"Input:\n\n* xml_data: a string containing the XML data to be parsed\n\nOutput:\n\n* rawurl: a list of URLs extracted from the XML data\n\nExample:\n\n* xml_data = 'http://www.example.com/video1.mp4</url>http://www.example.com/video2.mp4</url>'"

def fake_dummy_data3():
    yield f"Input:\n\n* xml_data: a string containing the XML data to be parsed\n\nOutput:\n\n* rawurl: a list of URLs extracted from the XML data\n\nExample:\n\n* xml_data = 'http://www.example.com/video1.mp4</url>http://www.example.com/video2.mp4</url>'\n* rawurl = 'http://www.example.com/video1.mp4', '[http://www.example.com/video2.mp4']\n\nImplementation:\n\n*"

def fake_dummy_data4():
    yield f"Input:\n\n* xml_data: a string containing the XML data to be parsed\n\nOutput:\n\n* rawurl: a list of URLs extracted from the XML data\n\nExample:\n\n* xml_data = 'http://www.example.com/video1.mp4</url>http://www.example.com/video2.mp4</url>'\n* rawurl = 'http://www.example.com/video1.mp4', '[http://www.example.com/video2.mp4']\n\nImplementation:\n\n* The function uses the parseString function from the xml.dom.minidom module to parse the XML data\n* "

def fake_dummy_data5():
    yield f"Input:\n\n* xml_data: a string containing the XML data to be parsed\n\nOutput:\n\n* rawurl: a list of URLs extracted from the XML data\n\nExample:\n\n* xml_data = 'http://www.example.com/video1.mp4</url>http://www.example.com/video2.mp4</url>'\n* rawurl = 'http://www.example.com/video1.mp4', '[http://www.example.com/video2.mp4']\n\nImplementation:\n\n* The function uses the parseString function from the xml.dom.minidom module to parse the XML data\n* It then uses the getElementsByTagName method to retrieve all the elements in the XML data\n* "

def fake_dummy_data6():
    yield f"Input:\n\n* xml_data: a string containing the XML data to be parsed\n\nOutput:\n\n* rawurl: a list of URLs extracted from the XML data\n\nExample:\n\n* xml_data = 'http://www.example.com/video1.mp4</url>http://www.example.com/video2.mp4</url>'\n* rawurl = 'http://www.example.com/video1.mp4', '[http://www.example.com/video2.mp4']\n\nImplementation:\n\n* The function uses the parseString function from the xml.dom.minidom module to parse the XML data\n* It then uses the getElementsByTagName method to retrieve all the elements in the XML data\n* For each element, it retrieves the element using the getElementsByTagName method\n* "

def fake_dummy_data7():
    yield f"Input:\n\n* xml_data: a string containing the XML data to be parsed\n\nOutput:\n\n* rawurl: a list of URLs extracted from the XML data\n\nExample:\n\n* xml_data = 'http://www.example.com/video1.mp4</url>http://www.example.com/video2.mp4</url>'\n* rawurl = 'http://www.example.com/video1.mp4', '[http://www.example.com/video2.mp4']\n\nImplementation:\n\n* The function uses the parseString function from the xml.dom.minidom module to parse the XML data\n* It then uses the getElementsByTagName method to retrieve all the elements in the XML data\n* For each element, it retrieves the element using the getElementsByTagName method\n* It then appends the URL to the rawurl list using the append method\n* Finally, it returns the rawurl list\n\nLimitations:\n\n* The function assumes that the XML data is well-formed and contains only the and elements\n* It does not handle any errors that may occur during the parsing process\n\nConclusion:\n\n* "

def fake_dummy_data8():
    yield f"Input:\n\n* xml_data: a string containing the XML data to be parsed\n\nOutput:\n\n* rawurl: a list of URLs extracted from the XML data\n\nExample:\n\n* xml_data = 'http://www.example.com/video1.mp4</url>http://www.example.com/video2.mp4</url>'\n* rawurl = 'http://www.example.com/video1.mp4', '[http://www.example.com/video2.mp4']\n\nImplementation:\n\n* The function uses the parseString function from the xml.dom.minidom module to parse the XML data\n* It then uses the getElementsByTagName method to retrieve all the elements in the XML data\n* For each element, it retrieves the element using the getElementsByTagName method\n* It then appends the URL to the rawurl list using the append method\n* Finally, it returns the rawurl list\n\nLimitations:\n\n* The function assumes that the XML data is well-formed and contains only the and elements\n* It does not handle any errors that may occur during the parsing process\n\nConclusion:\n\n* The sina_xml_to_url_list function is a simple Python function that extracts URLs from XML data in the format used by the Sina video sharing website.\n* It uses the xml.dom.minidom module to parse the XML data and retrieve the URLs.\n* The function is limited to handling the specific format of the XML data used by Sina, and does not handle any errors that may occur during the parsing process."


# async def stream_results():
#     prompt = ""
#     output = ""
#     func_name = "fake_dummy_data"
    
#     for i in range(5):
#         call_func = func_name + str(i+1)
#         output = next(globals()[call_func]())

#     text_outputs = [
#         prompt + output
#     ]
#     ret = {"text": text_outputs}
#     yield (json.dumps(ret) + "\0").encode("utf-8")

# class AsyncCounter:
#     def __init__(self, stop):
#         self.current = 0
#         self.stop = stop

#     def __aiter__(self):
#         return self

#     async def __anext__(self):
#         if self.current < self.stop:
#             await asyncio.sleep(1.0)
#             r = self.current
#             self.current += 1
#             return r
#         else:
#             raise StopAsyncIteration

@app.get("/hello")
def hello():
    return {"message": "헬로 월드"} # JSON 형식으로 반환

@app.post("/stream")
async def stream(request: Request):
    request_dict = await request.json()
    stream = request_dict.pop("stream", True)
    if stream:
        return StreamingResponse(fake_data_streamer())
    else:
        output = next(fake_dummy_data8())
        ret = {"text": output}
        return JSONResponse(ret)


