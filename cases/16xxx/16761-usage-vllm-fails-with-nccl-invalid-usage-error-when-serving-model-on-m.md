# vllm-project/vllm#16761: [Usage]: vLLM fails with NCCL invalid usage error when serving model on multi-GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#16761](https://github.com/vllm-project/vllm/issues/16761) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vLLM fails with NCCL invalid usage error when serving model on multi-GPU

### Issue 正文摘录

### Your current environment When attempting to serve Qwen2.5-vl or Intern-vl model using vLLM with tensor parallelism (--tensor-parallel-size 4), the engine fails to initialize due to a NCCL error: invalid usage. The logs also suggest a mismatch between CUDA runtime and driver versions for NCCL graph capture. Error logs ` ERROR 04-17 14:15:53 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-17 14:15:53 [core.py:387] File "/mnt/petrelfs/zhupengyu1/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 378, in run_engine_core ERROR 04-17 14:15:53 [core.py:387] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-17 14:15:53 [core.py:387] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-17 14:15:53 [core.py:387] File "/mnt/petrelfs/zhupengyu1/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 320, in __init__ ERROR 04-17 14:15:53 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-17 14:15:53 [core.py:387] File "/mnt/petrelfs/zhupengyu1/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 71, in __init__ ERROR 04-17 14:15:53 [core.py:387] self._in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: usage. The logs also suggest a mismatch between CUDA runtime and driver versions for NCCL graph capture. Error logs ` ERROR 04-17 14:15:53 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ER...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: g to serve Qwen2.5-vl or Intern-vl model using vLLM with tensor parallelism (--tensor-parallel-size 4), the engine fails to initialize due to a NCCL error: invalid usage. The logs also suggest a mismatch between CUDA ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: vLLM fails with NCCL invalid usage error when serving model on multi-GPU usage;stale ### Your current environment When attempting to serve Qwen2.5-vl or Intern-vl model using vLLM with tensor parallelism (--ten...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: o initialize due to a NCCL error: invalid usage. The logs also suggest a mismatch between CUDA runtime and driver versions for NCCL graph capture. Error logs ` ERROR 04-17 14:15:53 [core.py:387] EngineCore hit an except...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ails with NCCL invalid usage error when serving model on multi-GPU usage;stale ### Your current environment When attempting to serve Qwen2.5-vl or Intern-vl model using vLLM with tensor parallelism (--tensor-parallel-si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
