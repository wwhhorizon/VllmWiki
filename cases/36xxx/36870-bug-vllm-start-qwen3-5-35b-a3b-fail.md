# vllm-project/vllm#36870: [Bug]: vllm  start Qwen3.5-35B-A3B fail

| 字段 | 值 |
| --- | --- |
| Issue | [#36870](https://github.com/vllm-project/vllm/issues/36870) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm  start Qwen3.5-35B-A3B fail

### Issue 正文摘录

### Your current environment start: vllm serve /data/models/Qwen3.5-35B-A3B --host 0.0.0.0 --port 8000 --trust-remote-code --served-model-name qwen3.5-35b-a3b ### 🐛 Describe the bug (EngineCore_DP0 pid=13824) Process EngineCore_DP0: (EngineCore_DP0 pid=13824) Traceback (most recent call last): (EngineCore_DP0 pid=13824) File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=13824) self.run() (EngineCore_DP0 pid=13824) File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=13824) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=13824) File "/usr/local/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1010, in run_engine_core (EngineCore_DP0 pid=13824) raise e (EngineCore_DP0 pid=13824) File "/usr/local/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 997, in run_engine_core (EngineCore_DP0 pid=13824) engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore_DP0 pid=13824) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=13824) File "/usr/local/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 751, in __i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm start Qwen3.5-35B-A3B fail bug ### Your current environment start: vllm serve /data/models/Qwen3.5-35B-A3B --host 0.0.0.0 --port 8000 --trust-remote-code --served-model-name qwen3.5-35b-a3b ### 🐛 Describe th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e/core.py", line 154, in __init__ (EngineCore_DP0 pid=13824) num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=13824) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=13824...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
