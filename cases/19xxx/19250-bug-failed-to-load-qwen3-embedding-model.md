# vllm-project/vllm#19250: [Bug]: Failed to load Qwen3-Embedding model.

| 字段 | 值 |
| --- | --- |
| Issue | [#19250](https://github.com/vllm-project/vllm/issues/19250) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to load Qwen3-Embedding model.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s] ERROR 06-06 11:53:56 [core.py:515] EngineCore failed to start. ERROR 06-06 11:53:56 [core.py:515] Traceback (most recent call last): ERROR 06-06 11:53:56 [core.py:515] File "/mnt/workspace/vllm/vllm/v1/engine/core.py", line 506, in run_engine_core ERROR 06-06 11:53:56 [core.py:515] engine_core = EngineCoreProc(*args, **kwargs) ERROR 06-06 11:53:56 [core.py:515] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-06 11:53:56 [core.py:515] File "/mnt/workspace/vllm/vllm/v1/engine/core.py", line 390, in __init__ ERROR 06-06 11:53:56 [core.py:515] super().__init__(vllm_config, executor_class, log_stats, ERROR 06-06 11:53:56 [core.py:515] File "/mnt/workspace/vllm/vllm/v1/engine/core.py", line 76, in __init__ ERROR 06-06 11:53:56 [core.py:515] self.model_executor = executor_class(vllm_config) ERROR 06-06 11:53:56 [core.py:515] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-06 11:53:56 [core.py:515] File "/mnt/workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__ ERROR 06-06 11:53:56 [core.py:515] self._init_executor() ERROR 06-06 11:53:56 [core.py:515] File "/mnt...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Failed to load Qwen3-Embedding model. bug ### Your current environment ### 🐛 Describe the bug ``` Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s] ERROR 06-06 11:53:56 [core.py:515] Engi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
