# vllm-project/vllm#23249: [Bug]: vllm loading blocks on loading the model with torch.multiprocessing.

| 字段 | 值 |
| --- | --- |
| Issue | [#23249](https://github.com/vllm-project/vllm/issues/23249) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm loading blocks on loading the model with torch.multiprocessing.

### Issue 正文摘录

### Your current environment Here's the output of my code, after that the execution stucks . ```text python child_process_test.py main process pid: 37424 [W socket.cpp:464] [c10d] The server socket cannot be initialized on [::]:5556 (errno: 97 - Address family not supported by protocol). [W socket.cpp:697] [c10d] The client socket cannot be initialized to connect to [localhost]:5556 (errno: 97 - Address family not supported by protocol). [W socket.cpp:697] [c10d] The client socket cannot be initialized to connect to [localhost]:5556 (errno: 97 - Address family not supported by protocol). [DEBUG]: proccess with rank:1 and pid:37517 PG world size: 2 [DEBUG]: proccess with rank:0 and pid:37516 PG world size: 2 WARNING 08-20 11:57:51 config.py:1354] Casting torch.bfloat16 to torch.float16. INFO 08-20 11:57:51 llm_engine.py:169] Initializing an LLM engine (v0.5.1) with config: model='/beegfs/abouyghf/Mistral_7B/', speculative_config=None, tokenizer='/beegfs/abouyghf/Mistral_7B/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, l...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 6 PG world size: 2 WARNING 08-20 11:57:51 config.py:1354] Casting torch.bfloat16 to torch.float16. INFO 08-20 11:57:51 llm_engine.py:169] Initializing an LLM engine (v0.5.1) with config: model='/beegfs/abouyghf/Mistral_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm loading blocks on loading the model with torch.multiprocessing. bug;stale ### Your current environment Here's the output of my code, after that the execution stucks . ```text python child_process_test.py mai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None), see...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None), seed=0, served_model_name=/beegfs/abouyghf/Mistral_7B/,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: is successfully loaded in a single process. here's the code: ```python import os from vllm import LLM from multiprocessing import Process import time import sys import torch import torch.distributed as dist import torch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
