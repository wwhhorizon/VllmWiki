# vllm-project/vllm#28830: [Bug]: When the concurrency level is greater than 2, DeepSeek-V3.2 frequently generates nonsensical or corrupted responses.

| 字段 | 值 |
| --- | --- |
| Issue | [#28830](https://github.com/vllm-project/vllm/issues/28830) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When the concurrency level is greater than 2, DeepSeek-V3.2 frequently generates nonsensical or corrupted responses.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I served it using the command like this ```shell nohup vllm serve /data/models/DeepSeek-V3.2-Exp \ --served-model-name DeepSeek-V3.2-Exp \ --host 0.0.0.0 --port 6019 --gpu_memory_utilization 0.8 \ --max-model-len 131072 \ --trust-remote-code -tp 8 \ --enable-auto-tool-choice --tool-call-parser deepseek_v31 \ --chat-template /data/models/vllm/examples/tool_chat_template_deepseekv31.jinja & ``` test using the following script ```python import requests import json import random import string import time from concurrent.futures import ThreadPoolExecutor, as_completed from datetime import datetime import os API_URL = "http://localhost:6019/v1/chat/completions" MODEL_PATH = "DeepSeek-V3.2-Exp" CONCURRENCY = 3 REQUEST_COUNT = 6 SAVE_DIR = "./multi3_results" def random_question(): templates = [ "给我解释一下{}是什么？", "请用简单的方式告诉我{}。", "你能举例说明一下{}吗？", "为什么{}？", "{}对人类有什么意义？", "请详细分析一下{}的原理。", "有没有可能{}？", "{}有什么潜在风险？", ] topics = [ "量子计算", "深度学习", "人工智能", "黑洞", "时空弯曲", "强化学习", "癌细胞", "太阳能电池", "太空电梯", "区块链", "大模型推理", "线性注意力", "高维向量", "脑机接口", ''.join(random.choices(string.ascii_letters, k=8)) ] return random.choice(templates).format(random.choi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: epSeek-V3.2 frequently generates nonsensical or corrupted responses. bug;stale ### Your current environment ### 🐛 Describe the bug when I served it using the command like this ```shell nohup vllm serve /data/models/Deep...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: late_deepseekv31.jinja & ``` test using the following script ```python import requests import json import random import string import time from concurrent.futures import ThreadPoolExecutor, as_completed from datetime im...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e /data/models/vllm/examples/tool_chat_template_deepseekv31.jinja & ``` test using the following script ```python import requests import json import random import string import time from concurrent.futures import Thread...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: eration throughput: 23.2 tokens/s, Running: 3 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% (APIServer pid=2199314) INFO 11-15 22:31:56 [loggers.py:127] Engine 000: Avg prompt throughput:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
