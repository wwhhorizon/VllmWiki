# vllm-project/vllm#19977: [Bug]: OpenAI-compatible server doesn't support audio inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#19977](https://github.com/vllm-project/vllm/issues/19977) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OpenAI-compatible server doesn't support audio inputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I followed this tutorial: https://docs.vllm.ai/en/stable/features/multimodal_inputs.html#video-inputs_1 and get an error. Lauch vllm server: ```bash vllm serve Qwen/Qwen2-Audio-7B-Instruct \ --max_model_len 4096 \ --trust-remote-code \ --enforce-eager \ --limit-mm-per-prompt '{"audio":2}' ``` Then, curl the server with this script: ```python import base64 import requests from openai import OpenAI from vllm.assets.audio import AudioAsset client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1", ) audio_url = AudioAsset("winning_call").url chat_completion_from_url = client.chat.completions.create( messages=[{ "role": "user", "content": [ { "type": "text", "text": "What's in this audio?" }, { "type": "audio_url", "audio_url": { "url": audio_url }, }, ], }], model="Qwen/Qwen2-Audio-7B-Instruct", ) result = chat_completion_from_url.choices[0].message.content print("Chat completion output from audio url:", result) ``` It failed with: ```bash # server log: INFO 06-23 08:18:26 [logger.py:43] Received request chatcmpl-8643198b042f45808368806f24864fc5: prompt: " system\nYou are a helpful assistant. \n user\nWhat's in this audi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e bug I followed this tutorial: https://docs.vllm.ai/en/stable/features/multimodal_inputs.html#video-inputs_1 and get an error. Lauch vllm server: ```bash vllm serve Qwen/Qwen2-Audio-7B-Instruct \ --max_model_len 4096 \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pt '{"audio":2}' ``` Then, curl the server with this script: ```python import base64 import requests from openai import OpenAI from vllm.assets.audio import AudioAsset client = OpenAI( api_key="EMPTY", base_url="http://...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=4071, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Then, curl the server with this script: ```python import base64 import requests from openai import OpenAI from vllm.assets.audio import AudioAsset client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1", )...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
