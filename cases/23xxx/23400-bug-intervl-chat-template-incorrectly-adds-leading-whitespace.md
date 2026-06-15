# vllm-project/vllm#23400: [Bug]: InterVL Chat Template Incorrectly Adds Leading Whitespace

| 字段 | 值 |
| --- | --- |
| Issue | [#23400](https://github.com/vllm-project/vllm/issues/23400) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InterVL Chat Template Incorrectly Adds Leading Whitespace

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary The InterVL multi-modal model has a bug where applying the chat template introduces an unwanted leading whitespace, causing incorrect tokenization and model failures with small images. ## Problem Description When processing multi-modal requests with images, the chat template generates a prompt with a leading whitespace before the ` ` token, resulting in incorrect tokenization where the first token ID is 262 (whitespace) instead of 1 (` ` token). ## Steps to Reproduce ### 1. Server Configuration (`server.sh`) ```bash python -m vllm.entrypoints.openai.api_server \ --model /data0/models/InternVL2_5-8B/ \ --no-enable-chunked-prefill \ --max-num-batched-tokens 16384 \ --port 8089 \ --host 0.0.0.0 \ --served-model-name InternVL2_5-8B \ --trust-remote-code \ --max-model-len 16384 \ --gpu-memory-utilization 0.95 ``` ### 2. Client Code (`client.py`) ```python #!/usr/bin/env python3 import requests import json data = { "model": "InternVL2_5-8B", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": [ { "type": "image_url", "image_url": {"url": "data:image/jpeg;base64,/9j/4AAQ...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 5 ``` ### 2. Client Code (`client.py`) ```python #!/usr/bin/env python3 import requests import json data = { "model": "InternVL2_5-8B", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ading whitespace, causing incorrect tokenization and model failures with small images. ## Problem Description When processing multi-modal requests with images, the chat template generates a prompt with a leading whitesp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vironment ### 🐛 Describe the bug ## Summary The InterVL multi-modal model has a bug where applying the chat template introduces an unwanted leading whitespace, causing incorrect tokenization and model failures with smal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s with small images. ## Problem Description When processing multi-modal requests with images, the chat template generates a prompt with a leading whitespace before the ` ` token, resulting in incorrect tokenization wher...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: irst token ID is 262 (whitespace) instead of 1 (` ` token). ## Steps to Reproduce ### 1. Server Configuration (`server.sh`) ```bash python -m vllm.entrypoints.openai.api_server \ --model /data0/models/InternVL2_5-8B/ \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
