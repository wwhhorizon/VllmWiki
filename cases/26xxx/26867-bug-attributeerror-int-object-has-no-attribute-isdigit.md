# vllm-project/vllm#26867: [Bug]: AttributeError: 'int' object has no attribute 'isdigit'

| 字段 | 值 |
| --- | --- |
| Issue | [#26867](https://github.com/vllm-project/vllm/issues/26867) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'int' object has no attribute 'isdigit'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve Qwen/Qwen2.5-1.5B-Instruct ``` (EngineCore_DP0 pid=80) File "/usr/local/lib/python3.12/dist-packages/flashinfer/jit/core.py", line 175, in gen_jit_spec (EngineCore_DP0 pid=80) check_cuda_arch() (EngineCore_DP0 pid=80) File "/usr/local/lib/python3.12/dist-packages/flashinfer/jit/core.py", line 55, in check_cuda_arch (EngineCore_DP0 pid=80) elif major == 7 and minor.isdigit(): (EngineCore_DP0 pid=80) ^^^^^^^^^^^^^ (EngineCore_DP0 pid=80) AttributeError: 'int' object has no attribute 'isdigit' [rank0]:[W1014 18:38:25.322942437 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator()) ``` I've tried adding environment variables to get around it. `VLLM_USE_FLASHINFER_SAMPLER=0` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: it/core.py", line 175, in gen_jit_spec (EngineCore_DP0 pid=80) check_cuda_arch() (EngineCore_DP0 pid=80) File "/usr/local/lib/python3.12/dist-packages/flashinfer/jit/core.py", line 55, in check_cuda_arch (EngineCore_DP0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: (EngineCore_DP0 pid=80) File "/usr/local/lib/python3.12/dist-packages/flashinfer/jit/core.py", line 175, in gen_jit_spec (EngineCore_DP0 pid=80) check_cuda_arch() (EngineCore_DP0 pid=80) File "/usr/local/lib/python3.12/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bug ### Your current environment ### 🐛 Describe the bug vllm serve Qwen/Qwen2.5-1.5B-Instruct ``` (EngineCore_DP0 pid=80) File "/usr/local/lib/python3.12/dist-packages/flashinfer/jit/core.py", line 175, in gen_jit_spec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
