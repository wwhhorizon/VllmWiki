# vllm-project/vllm#10432: [Bug]: vllm server crash when num-scheduler-steps > 1 and max_tokens=0

| 字段 | 值 |
| --- | --- |
| Issue | [#10432](https://github.com/vllm-project/vllm/issues/10432) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm server crash when num-scheduler-steps > 1 and max_tokens=0

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is how I am serving my model. While this works for most inputs It fails when my prompt has max_token is 0 ```bash vllm serve Qwen/Qwen2.5-72B-Instruct --tensor-parallel-size 8 --gpu-memory-utilization 0.9 --max-model-len 8192 --max-num-seqs 128 --max-num-batched-tokens 131072 --tokenizer-pool-size 128 --scheduling-policy fcfs --disable-log-stats --enable-prefix-caching --tokenizer-mode auto --swap-space 16 --enable-chunked-prefill --block-size 32 --num-scheduler-steps 8 --multi-step-stream-outputs False ``` prompt example ```bash from openai import OpenAI import socket import json import os import time # Determine the hostname start_time = time.time() hostname = socket.gethostname() os.environ['no_proxy'] = f"localhost,{hostname},127.0.0.1" # Construct the base_url base_url = f"http://127.0.0.1:8000/v1" client = OpenAI( base_url=base_url, api_key="cxvff_xxxx", ) completion = client.completions.create( model = "Qwen/Qwen2.5-72B-Instruct", prompt = "You are a friendly and helpful AI assistant. Please help me to answer the following question.\n\nQuestion What color is the sky\n\nAnswer:", max...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: vllm server crash when num-scheduler-steps > 1 and max_tokens=0 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is how I am serving my model. While this work...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: -multi-step-stream-outputs False ``` prompt example ```bash from openai import OpenAI import socket import json import os import time # Determine the hostname start_time = time.time() hostname = socket.gethostname() os....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: --tokenizer-mode auto --swap-space 16 --enable-chunked-prefill --block-size 32 --num-scheduler-steps 8 --multi-step-stream-outputs False ``` prompt example ```bash from openai import OpenAI import socket import json imp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ateway/envs/vllmv0.6.4.post1/lib/python3.11/site-packages/vllm/attention/backends/flash_attn.py", line 362, in advance_step ERROR 11-18 19:20:05 engine.py:135] ops.advance_step_flashattn(num_seqs=num_seqs, ERROR 11-18 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
