# vllm-project/vllm#16359: [LLAMA 4 Scout] Can't make it work

| 字段 | 值 |
| --- | --- |
| Issue | [#16359](https://github.com/vllm-project/vllm/issues/16359) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [LLAMA 4 Scout] Can't make it work

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to deploy a LLama 4 Scout in a just created 8xH100 instance ```bash uv run vllm serve "unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth" --tensor-parallel-size 8 --max_model_len 35000 ``` The model downloads and all works well but i reach this error: ```bash CRITICAL 04-09 19:16:14 [multiproc_executor.py:49] MulitprocExecutor got fatal signal from worker processes, shutting down. See stack trace above for root cause issue. CRITICAL 04-09 19:16:14 [core_client.py:361] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue. (VllmWorker rank=3 pid=39041) Traceback (most recent call last): (VllmWorker rank=3 pid=39041) File "/home/opc/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (VllmWorker rank=3 pid=39041) self.run() (VllmWorker rank=3 pid=39041) File "/home/opc/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 108, in run (VllmWorker rank=3 pid=39041) self._target(*self._args, **self._kwargs) (VllmWorker rank=3 pid=39041) File "/home/opc/vllm/.venv/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ribe the bug I am trying to deploy a LLama 4 Scout in a just created 8xH100 instance ```bash uv run vllm serve "unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth" --tensor-parallel-size 8 --max_model_len 35000 ``` The mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [LLAMA 4 Scout] Can't make it work bug ### Your current environment ### 🐛 Describe the bug I am trying to deploy a LLama 4 Scout in a just created 8xH100 instance ```bash uv run vllm serve "unsloth/Llama-4-Scout-17
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: /llama4.py", line 447, in load_weights (VllmWorker rank=3 pid=39041) moe_loaded = self.load_moe_expert_weights( (VllmWorker rank=3 pid=39041) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=3 pid=39041) File "/home/opc/v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _support;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
