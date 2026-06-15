# vllm-project/vllm#30250: [Bug]: Qwen2.5-VL-72B-Instruct W8A8 Abnormal reasoning results

| 字段 | 值 |
| --- | --- |
| Issue | [#30250](https://github.com/vllm-project/vllm/issues/30250) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL-72B-Instruct W8A8 Abnormal reasoning results

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to use W8A8 for inference models(Qwen2.5-VL-72B-Instruct-quantized.w8a8); ## Start Service： ```Bash vllm serve "/data/Qwen2.5-VL-72B-Instruct-quantized.w8a8" \ --port 8000 \ --tensor-parallel-size 4 \ --trust-remote-code \ --max-model-len 98304 \ --max-num-seqs 8 \ --limit_mm_per_prompt '{"image":5}' \ --gpu-memory-utilization 0.95 ``` ## Send Request： ```Python import requests from PIL import Image import io import base64 url = "http://127.0.0.1:8000/v1/chat/completions" headers = {"Content-Type": "application/json"} data = { "model": "/data/Qwen2.5-VL-72B-Instruct-quantized.w8a8", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "What do you see in this image?" }, { "type": "image_url", "image_url": { "url": "http://images.cocodataset.org/train2017/000000000025.jpg" } } ] } ] } response = requests.post(url, json=data, headers=headers) if response.status_code == 200: result = response.json() print("模型输出：", result["choices"]) else: print("请求失败，状态码：", response.status_code) print("错误信息：", response.text) ``` Input Image： Return Results： ### Before submitting a new issue... - [x] Make sure you already sea...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: :5}' \ --gpu-memory-utilization 0.95 ``` ## Send Request： ```Python import requests from PIL import Image import io import base64 url = "http://127.0.0.1:8000/v1/chat/completions" headers = {"Content-Type": "application...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5-VL-72B-Instruct W8A8 Abnormal reasoning results bug ### Your current environment ### 🐛 Describe the bug I want to use W8A8 for inference models(Qwen2.5-VL-72B-Instruct-quantized.w8a8); ## Start Service： `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: er_prompt '{"image":5}' \ --gpu-memory-utilization 0.95 ``` ## Send Request： ```Python import requests from PIL import Image import io import base64 url = "http://127.0.0.1:8000/v1/chat/completions" headers = {"Content-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
