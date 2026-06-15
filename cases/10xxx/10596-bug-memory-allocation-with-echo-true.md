# vllm-project/vllm#10596: [Bug]: Memory allocation with echo=True

| 字段 | 值 |
| --- | --- |
| Issue | [#10596](https://github.com/vllm-project/vllm/issues/10596) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Memory allocation with echo=True

### Issue 正文摘录

### Your current environment ### Model Input Dumps [vllm_archive.tar.gz](https://github.com/user-attachments/files/17882221/vllm_archive.tar.gz) ### 🐛 Describe the bug Hello! First I bring up the API Server using the bash command below ```bash python -m vllm.entrypoints.openai.api_server --model openchat/openchat-3.6-8b-20240522 ``` Then I specifically send a query with a long prompt and `echo=True`. ```python import requests import json url = "http://localhost:8000/v1/completions" headers = {"Content-Type": "application/json"} data = { "model": "openchat/openchat-3.6-8b-20240522", "prompt": " " * 8000, "max_tokens": 1, "logprobs": 1, "echo": True } response = requests.post(url, headers=headers, data=json.dumps(data)) ``` VLLM starts allocating memory (on top of what it already allocated under KV-cache) and I am running short of memory on my NVIDIA A100 80GB. The server crashes with an error. I expected vllm to make better use of the memory it took under the KV-cache. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: enai.api_server --model openchat/openchat-3.6-8b-20240522 ``` Then I specifically send a query with a long prompt and `echo=True`. ```python import requests import json url = "http://localhost:8000/v1/completions" heade...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Memory allocation with echo=True bug;stale ### Your current environment ### Model Input Dumps [vllm_archive.tar.gz](https://github.com/user-attachments/files/17882221/vllm_archive.tar.gz) ### 🐛 Describe the bug H...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: bug;stale ### Your current environment ### Model Input Dumps [vllm_archive.tar.gz](https://github.com/user-attachments/files/17882221/vllm_archive.tar.gz) ### 🐛 Describe the bug Hello! First I bring up the API Server us...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: VLLM starts allocating memory (on top of what it already allocated under KV-cache) and I am running short of memory on my NVIDIA A100 80GB. The server crashes with an error. I expected vllm to make better use of the mem...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;oom dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
