# vllm-project/vllm#20302: [Bug]: Wrong kv_cache_usage_perc metric

| 字段 | 值 |
| --- | --- |
| Issue | [#20302](https://github.com/vllm-project/vllm/issues/20302) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Wrong kv_cache_usage_perc metric

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am not sure if this should be titled a bug or if there is some issue with my config. But I am getting incorrect `vllm:kv_cache_usage_perc` and `vllm:gpu_cache_usage_perc`. I am running `vllm serve meta-llama/Llama-3.2-3B-Instruct` **Code** ``` import requests import time import json import random import string GATEWAY_URL = "http://localhost:8000/v1/chat/completions" HEADERS = { "accept": "application/json", "Content-Type": "application/json" } MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct" PROMPT_LENGTH = 500 NUMBER_OF_PROMPTS = 100 def generate_random_word(length=6): return ''.join(random.choices(string.ascii_lowercase, k=length)) def send_request(prompt_text, max_tokens=500): payload = { "model": MODEL_NAME, "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt_text} ], "max_tokens": max_tokens } start = time.time() try: res = requests.post(GATEWAY_URL, json=payload, headers=HEADERS) latency = time.time() - start return latency, res.status_code, res.text except Exception as e: return -1, None, str(e) if __name__ == '__main__': for i in range(NUMBER_OF_PROMPTS): rand_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: I am running `vllm serve meta-llama/Llama-3.2-3B-Instruct` **Code** ``` import requests import time import json import random import string GATEWAY_URL = "http://localhost:8000/v1/chat/completions" HEADERS = { "accept":...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ot sure if this should be titled a bug or if there is some issue with my config. But I am getting incorrect `vllm:kv_cache_usage_perc` and `vllm:gpu_cache_usage_perc`. I am running `vllm serve meta-llama/Llama-3.2-3B-In...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: nning `vllm serve meta-llama/Llama-3.2-3B-Instruct` **Code** ``` import requests import time import json import random import string GATEWAY_URL = "http://localhost:8000/v1/chat/completions" HEADERS = { "accept": "appli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: re? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: res = requests.post(GATEWAY_URL, json=payload, headers=HEADERS) latency = time.time() - start return latency, res.status_code, res.text except Exception as e: return -1, None, str(e) if __name__ == '__main__': for i in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
