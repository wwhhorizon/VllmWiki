# vllm-project/vllm#30752: [Bug]: ` leaked shared_memory objects to clean up at shutdown` cause offline mode start failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#30752](https://github.com/vllm-project/vllm/issues/30752) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ` leaked shared_memory objects to clean up at shutdown` cause offline mode start failed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Offline mode start faild. the simple script to reproduce ```python #!/usr/bin/python import random import argparse import json from typing import Any, List, Dict from vllm import LLM, SamplingParams SYS_QUERY = [ { "role": "system", "content": "You are a helpful coding assistant. "} ] QUERY = { "messages": SYS_QUERY, "frequency_penalty": 1.0, "temperature": 0.0, "top_p": 0.95 } def generate_random_messages(base_message=SYS_QUERY, max_messages_per_conversation: int = 4, min_message_length: int = 1 * 1024, max_message_length: int = 10 * 1024) -> List[Dict[str, str]]: messages = [] num_messages = random.randint(1, max_messages_per_conversation) messages.append(base_message[0]) for i in range(num_messages): role = "user" if i % 2 == 0 else "assistant" content_length = random.randint(min_message_length, max_message_length) content = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz ', k=content_length)) messages.append({"role": role, "content": content.strip()}) return messages def generate_batch_messages(batch_size: int = 256) -> List[List[Dict[str, str]]]: batch_messages = [] for _ in range(batch_size): messages = generate_random_m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tart faild. the simple script to reproduce ```python #!/usr/bin/python import random import argparse import json from typing import Any, List, Dict from vllm import LLM, SamplingParams SYS_QUERY = [ { "role": "system",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: urn batch_messages def main(): query = QUERY llm = LLM( model="/ssd/1/xsank.mz/models/qwen3_coder_30b_a3b_instruct", tensor_parallel_size=2, #enable_expert_parallel=True, #data_parallel_size=2, #max_model_len=100, ) sam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: coder_30b_a3b_instruct", tensor_parallel_size=2, #enable_expert_parallel=True, #data_parallel_size=2, #max_model_len=100, ) sampling_params = SamplingParams( temperature=query.get("temperature"), top_p=query.get("top_p"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ry objects to clean up at shutdown` cause offline mode start failed. bug;stale ### Your current environment ### 🐛 Describe the bug Offline mode start faild. the simple script to reproduce ```python #!/usr/bin/python imp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
