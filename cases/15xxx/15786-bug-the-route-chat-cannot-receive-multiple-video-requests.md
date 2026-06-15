# vllm-project/vllm#15786: [Bug]: The route /chat cannot receive multiple video requests

| 字段 | 值 |
| --- | --- |
| Issue | [#15786](https://github.com/vllm-project/vllm/issues/15786) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The route /chat cannot receive multiple video requests

### Issue 正文摘录

### Your current environment When I run test with command `pytest -s -v entrypoints/openai/test_video.py::test_multi_video_input[video_urls0-llava-hf/llava-onevision-qwen2-0.5b-ov-hf]` Based on the name and content of this test case, I think this should support multiple videos as input. ### 🐛 Describe the bug I found it failed, so I try to launch server and send request manually. This is my command to launch server ``` python3 -m vllm.entrypoints.openai.api_server --model=llava-hf/llava-onevision-qwen2-0.5b-ov-hf ``` And this is my request command ``` curl -X POST http://0.0.0.0:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "llava-hf/llava-onevision-qwen2-0.5b-ov-hf", "messages": [{ "role": "user", "content": [ {"type": "video_url", "video_url": {"url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"}}, {"type": "video_url", "video_url": {"url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"}}, {"type": "text", "text": "What'\''s in this video?"} ] }], "max_completion_tokens": 10, "temperature": 0.0 }' ``` And server will throw exception as below: ``` ERROR 03-31 03:11:46 [se...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: trypoints/openai/test_video.py::test_multi_video_input[video_urls0-llava-hf/llava-onevision-qwen2-0.5b-ov-hf]` Based on the name and content of this test case, I think this should support multiple videos as input. ### 🐛...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: The route /chat cannot receive multiple video requests bug ### Your current environment When I run test with command `pytest -s -v entrypoints/openai/test_video.py::test_multi_video_input[video_urls0-llava-hf/lla...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ive multiple video requests bug ### Your current environment When I run test with command `pytest -s -v entrypoints/openai/test_video.py::test_multi_video_input[video_urls0-llava-hf/llava-onevision-qwen2-0.5b-ov-hf]` Ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
