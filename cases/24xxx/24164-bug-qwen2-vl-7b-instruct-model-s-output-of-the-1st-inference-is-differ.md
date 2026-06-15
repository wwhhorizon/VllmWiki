# vllm-project/vllm#24164: [Bug]: Qwen2-VL-7B-Instruct model`s output of the 1st inference is different with the subsequent inferences.

| 字段 | 值 |
| --- | --- |
| Issue | [#24164](https://github.com/vllm-project/vllm/issues/24164) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2-VL-7B-Instruct model`s output of the 1st inference is different with the subsequent inferences.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving the Qwen2-VL-7B-Instruct using vllm, I found the output of the 1st inference is different with the subsequent inferences when the prefix-caching is enable(which is the default option): server cmd ```bash #!/bin/bash vllm serve /data0/models/Qwen2-VL-7B-Instruct/ \ --max-num-seqs 4 \ --max-num-batched-tokens 16384 \ --max-model-len 16384 \ --enforce-eager \ --trust-remote-code ``` client script: ```python import requests import json import requests import json api_base = f"http://127.0.0.1:8000/v1/chat/completions" image_file = "image_url.txt" def random_messages(image_url: str): return { "temperature": 0.0, "max_tokens": 1024, "stream": True, "ignore_eos": False, "messages": [ { "role": "system", "content": "无视所有前置 Prompt，严格按照此条最新的 Prompt 执行\n\n用 \n 包裹思考的过程。**思考内容** & 正文 之间需要隔一行提高可读性。", }, { "role": "user", "content": [ {"type": "image_url", "image_url": {"url": image_url}}, { "type": "text", "text": "插图中的文本是什么？请用中文、英文分别输出所有文字1遍不要遗漏", }, ], }, ], } def send_request(image_url: str): try: req_body = random_messages(image_url=image_url) response_text = "" with requests.post( api_base, json=req_body, stream=True, timeout...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: \ --enforce-eager \ --trust-remote-code ``` client script: ```python import requests import json import requests import json api_base = f"http://127.0.0.1:8000/v1/chat/completions" image_file = "image_url.txt" def rando...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ut of the 1st inference is different with the subsequent inferences. bug;stale ### Your current environment ### 🐛 Describe the bug When serving the Qwen2-VL-7B-Instruct using vllm, I found the output of the 1st inferenc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2-VL-7B-Instruct model`s output of the 1st inference is different with the subsequent inferences. bug;stale ### Your current environment ### 🐛 Describe the bug When serving the Qwen2-VL-7B-Instruct using vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rontend_api;hardware_porting;model_support;sampling_logits cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
