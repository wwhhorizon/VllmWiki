# vllm-project/vllm#28134: [Bug]: Streaming doesnt start until the response is completed

| 字段 | 值 |
| --- | --- |
| Issue | [#28134](https://github.com/vllm-project/vllm/issues/28134) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming doesnt start until the response is completed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems I am experiencing the same issue as #460 and #2694, but directly using `vllm/vllm-openai:latest` last published 4 days ago as of today. I am trying with `cpatonn/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit` but I have also tried with Gemma 3 27b IT non-quantized and see the same results. ```python import requests API_ADDRESS = "http://localhost:8001/v1/chat/completions" headers = {"Content-Type": "application/json"} response = requests.post( API_ADDRESS, json={ "model": "/models/Qwen3-30B-A3B-Instruct-2507-AWQ-4bit", "max_tokens": 1000, "temperature": 0.1, "top_p": 0.9, "top_k": 100, "presence_penalty": 1, "stream": True, "n": 1, "messages": [{ "role": "user", "content": "Tell me a story about a cat." }] }, stream=True, ) for x in response: print(x) ``` 8.0s later, I indeed get the output i expect, but i get it all at once. That is to say that all intermediate responses are streamed at the same time, after inference has fully completed. ``` vllm-1 | (APIServer pid=1) INFO 11-05 12:39:35 [logger.py:40] Received request chatcmpl-b87aa23d3945464d97fa892ff0d2d044: prompt: ' user\nTell me a story about a cat. \n assistant\n', params...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment ### 🐛 Describe the bug It seems I am experiencing the same issue as #460 and #2694, but directly using `vllm/vllm-openai:latest` last published 4 days ago as of today. I am trying with `cpatonn/Qw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Streaming doesnt start until the response is completed bug;stale ### Your current environment ### 🐛 Describe the bug It seems I am experiencing the same issue as #460 and #2694, but directly using `vllm/vllm-open...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t the windowpane of Mrs. Gable’s tiny flat, turning the city lights into smudged watercolor streaks. Inside, the air was thick with the scent of damp wool and old books. On the worn velvet armchair, curled like a questi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: latest` last published 4 days ago as of today. I am trying with `cpatonn/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit` but I have also tried with Gemma 3 27b IT non-quantized and see the same results. ```python import requests...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 80B-A3B-Instruct-AWQ-4bit` but I have also tried with Gemma 3 27b IT non-quantized and see the same results. ```python import requests API_ADDRESS = "http://localhost:8001/v1/chat/completions" headers = {"Content-Type":...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
