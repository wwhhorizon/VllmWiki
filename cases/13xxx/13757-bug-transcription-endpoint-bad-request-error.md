# vllm-project/vllm#13757: [Bug]: Transcription endpoint: Bad request error

| 字段 | 值 |
| --- | --- |
| Issue | [#13757](https://github.com/vllm-project/vllm/issues/13757) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Transcription endpoint: Bad request error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Vllm version: 0.7.3 Issue: On creating a POST request to transcriptions endpoint using following CURL request ``` curl --location 'http://localhost:8000/v1/audio/transcriptions' \ --form 'language="en"' \ --form 'model="whisper"' \ --form 'file=@"/Users/ishan1.mishra/Downloads/warning-some-viewers-may-find-tv-announcement-arcade-voice-movie-guy-4-4-00-04.mp3"' ``` I get the following error: ``` { "object": "error", "message": "[{'type': 'missing', 'loc': ('body', 'request'), 'msg': 'Field required', 'input': None, 'url': 'https://errors.pydantic.dev/2.9/v/missing'}]", "type": "BadRequestError", "param": null, "code": 400 } ``` On exploring the code I found that the route is defined like: ``` @with_cancellation async def create_transcriptions(request: Annotated[TranscriptionRequest, Form()], ..... ``` I think it should be that we explicitly define file and form type for each field like: ``` @app.post("/transcriptions") async def create_transcriptions( file: UploadFile = File(...), model: str = Form(...), language: Optional[str] = Form(None), prompt: str = Form(""), response_format: str = Form("json"), temperature: float = Form(0.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: bug;stale ### Your current environment ### 🐛 Describe the bug Vllm version: 0.7.3 Issue: On creating a POST request to transcriptions endpoint using following CURL request ``` curl --location 'http://localhost:8000/v1/a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: calhost:8000/v1/audio/transcriptions' \ --form 'language="en"' \ --form 'model="whisper"' \ --form 'file=@"/Users/ishan1.mishra/Downloads/warning-some-viewers-may-find-tv-announcement-arcade-voice-movie-guy-4-4-00-04.mp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Transcription endpoint: Bad request error bug;stale ### Your current environment ### 🐛 Describe the bug Vllm version: 0.7.3 Issue: On creating a POST request to transcriptions endpoint using following CURL reques...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: PR ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
