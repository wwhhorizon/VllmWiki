# vllm-project/vllm#24694: [Bug]: RuntimeError: CUDASymmetricMemoryAllocator::rendezvous: detected allocations from overlapping devices from different ranks.

| 字段 | 值 |
| --- | --- |
| Issue | [#24694](https://github.com/vllm-project/vllm/issues/24694) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDASymmetricMemoryAllocator::rendezvous: detected allocations from overlapping devices from different ranks.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-V2-lite" --max-num-seqs 512 --data-parallel-size 2 --enable-expert-parallel --gpu-memory-utilization 0.9 --port 9256` Cause ```bash (EngineCore_DP0 pid=397122) Process EngineCore_DP0: (EngineCore_DP0 pid=397122) Traceback (most recent call last): (EngineCore_DP0 pid=397122) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=397122) self.run() (EngineCore_DP0 pid=397122) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=397122) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=397122) File "/data/vllm-community-homes/vllm-user-6/vllm/vllm/v1/engine/core.py", line 722, in run_engine_core (EngineCore_DP0 pid=397122) raise e (EngineCore_DP0 pid=397122) File "/data/vllm-community-homes/vllm-user-6/vllm/vllm/v1/engine/core.py", line 705, in run_engine_core (EngineCore_DP0 pid=397122) engine_core = DPEngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=397122) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=397122) File "/data/vllm-community-homes/vllm-user-6/vllm/vllm/v1/engine/core.py", l...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: CUDASymmetricMemoryAllocator::rendezvous: detected allocations from overlapping devices from different ranks. bug ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-V2-lite" --max-num-seqs 512 --data-parallel-size 2 --enable-expert-parallel --gpu-memory-utilization 0.9 --port 9256` Cause...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: -ai/DeepSeek-V2-lite" --max-num-seqs 512 --data-parallel-size 2 --enable-expert-parallel --gpu-memory-utilization 0.9 --port 9256` Cause ```bash (EngineCore_DP0 pid=397122) Process EngineCore_DP0: (EngineCore_DP0 pid=39...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
