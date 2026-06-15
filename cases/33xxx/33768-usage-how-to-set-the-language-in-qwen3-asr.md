# vllm-project/vllm#33768: [Usage]:  How to set the language in Qwen3-Asr

| 字段 | 值 |
| --- | --- |
| Issue | [#33768](https://github.com/vllm-project/vllm/issues/33768) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  How to set the language in Qwen3-Asr

### Issue 正文摘录

### Your current environment ```text import requests url = "http://0.0.0.0:9881/v1/chat/completions" headers = {"Content-Type": "application/json"} target_language = "Arabic" data = { "messages": [ { "role": "user", "content": [ {"type": "text", "text": f"Transcribe the following audio into {target_language}."}, { "type": "audio_url", "audio_url": { "url": "file:///nas/xyq/Qwen-Asr-POC/5262126349647872/1770072158499.mp3" # "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_en.wav" }, } ], } ] } response = requests.post(url, headers=headers, json=data, timeout=300) response.raise_for_status() content = response.json()['choices'][0]['message']['content'] print(content) language, text = content.split(" ") print(language) print(text) ``` (base) ➜ Qwen3-ASR git:(main) ✗ python3 infer_vllm_demo.py language English I'm a geek. I'm a geek. I'm a geek. Yeah, I'm a geek. I'm a geek. I'm a geek. I'm a geek. I'm a geek. language English I'm a geek. I'm a geek. I'm a geek. Yeah, I'm a geek. I'm a geek. I'm a geek. I'm a geek. I'm a geek. (base) ➜ Qwen3-ASR git:(main) ✗ I want the language to be Arabic ### How would you like to use vllm I want to run inference of a [specific mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: et the language in Qwen3-Asr usage ### Your current environment ```text import requests url = "http://0.0.0.0:9881/v1/chat/completions" headers = {"Content-Type": "application/json"} target_language = "Arabic" data = {...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to set the language in Qwen3-Asr usage ### Your current environment ```text import requests url = "http://0.0.0.0:9881/v1/chat/completions" headers = {"Content-Type": "application/json"} target_language = "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: language in Qwen3-Asr usage ### Your current environment ```text import requests url = "http://0.0.0.0:9881/v1/chat/completions" headers = {"Content-Type": "application/json"} target_language = "Arabic" data = { "messag...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
