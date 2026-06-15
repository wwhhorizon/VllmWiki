# vllm-project/vllm#35287: [Bug]: An error occurred when Qwen3.5 started the model using --quantization fp8

| 字段 | 值 |
| --- | --- |
| Issue | [#35287](https://github.com/vllm-project/vllm/issues/35287) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: An error occurred when Qwen3.5 started the model using --quantization fp8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when i started https://huggingface.co/Qwen/Qwen3.5-27B with --quantization fp8, it occurred an error Process EngineCore_DP0: (EngineCore_DP0 pid=9429) Traceback (most recent call last): (EngineCore_DP0 pid=9429) File "/opt/conda310/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=9429) self.run() (EngineCore_DP0 pid=9429) File "/opt/conda310/lib/python3.10/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=9429) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=9429) File "/source/vllm/vllm/v1/engine/core.py", line 1033, in run_engine_core (EngineCore_DP0 pid=9429) raise e (EngineCore_DP0 pid=9429) File "/source/vllm/vllm/v1/engine/core.py", line 1019, in run_engine_core (EngineCore_DP0 pid=9429) engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore_DP0 pid=9429) File "/source/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore_DP0 pid=9429) return func(*args, **kwargs) (EngineCore_DP0 pid=9429) File "/source/vllm/vllm/v1/engine/core.py", line 763, in __init__ (EngineCore_DP0 pid=9429) super().__init__( (EngineCore_DP0 pid=94...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: An error occurred when Qwen3.5 started the model using --quantization fp8 bug ### Your current environment ### 🐛 Describe the bug when i started https://huggingface.co/Qwen/Qwen3.5-27B with --quantization fp8, it...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: An error occurred when Qwen3.5 started the model using --quantization fp8 bug ### Your current environment ### 🐛 Describe the bug when i started https://huggingface.co/Qwen/Qwen3.5-27B with --quantization fp8, it...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: p_rank, **kwargs) (EngineCore_DP0 pid=9429) File "/source/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore_DP0 pid=9429) return func(*args, **kwargs) (EngineCore_DP0 pid=9429) File "/source/vllm/vllm/v1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ad. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
