# vllm-project/vllm#7865: [Bug]: can recived request and no answer on device H20

| 字段 | 值 |
| --- | --- |
| Issue | [#7865](https://github.com/vllm-project/vllm/issues/7865) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can recived request and no answer on device H20

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug import pickle import pandas import json import requests import os import re from requests.adapters import HTTPAdapter import logging as logger import time prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] call_llm(prompts[0]) def call_llm(prompt, llm_url="http://127.0.0.1:7788/v1/chat/completions", model_name="Qwen1.5-14B-Chat-GPTQ-Int4"): headers = {"Content-Type": "application/json"} data = {"model": model_name, "top_k": 5, "top_p": 0.85,"max_tokens":100, "temperature": 0.3, "messages": [{"role": "user", "content": prompt}]} if model_name == "path-lora": data.update({"max_tokens": 8}) data = json.dumps(data) s = requests.Session() s.mount('http://', HTTPAdapter(max_retries=3)) try: res = s.post(llm_url, data=data, headers=headers, timeout=600) if res.status_code == 200: return res.json()['choices'][0]['message']['content'] else: logger.error(f"Request Failed statu_code:{res.status_code}, {res.content}") return None except requests.exceptions.RequestException as e: logger.error(f"Request execute Exceptions:{e}") return None =============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: can recived request and no answer on device H20 bug ### Your current environment ### 🐛 Describe the bug import pickle import pandas import json import requests import os import re from requests.adapters import HT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: //127.0.0.1:7788/v1/chat/completions", model_name="Qwen1.5-14B-Chat-GPTQ-Int4"): headers = {"Content-Type": "application/json"} data = {"model": model_name, "top_k": 5, "top_p": 0.85,"max_tokens":100, "temperature": 0.3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , temperature=0.3, top_p=0.85, top_k=5, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ef call_llm(prompt, llm_url="http://127.0.0.1:7788/v1/chat/completions", model_name="Qwen1.5-14B-Chat-GPTQ-Int4"): headers = {"Content-Type": "application/json"} data = {"model": model_name, "top_k": 5, "top_p": 0.85,"m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ========================= INFO 08-26 15:12:36 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
