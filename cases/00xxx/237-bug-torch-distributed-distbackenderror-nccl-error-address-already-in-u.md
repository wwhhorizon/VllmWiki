# vllm-project/vllm#237:  [Bug] torch.distributed.DistBackendError: NCCL error ....  Address already in use

| 字段 | 值 |
| --- | --- |
| Issue | [#237](https://github.com/vllm-project/vllm/issues/237) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

>  [Bug] torch.distributed.DistBackendError: NCCL error ....  Address already in use

### Issue 正文摘录

``` Traceback (most recent call last): File "test.py", line 14, in llm = LLM(model=path) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/llm.py", line 56, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 151, in from_engine_args engine = cls(*engine_configs, distributed_init_method, devices, File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 93, in __init__ worker = worker_cls( File "/usr/local/lib/python3.8/dist-packages/vllm/worker/worker.py", line 40, in __init__ _init_distributed_environment(parallel_config, rank, File "/usr/local/lib/python3.8/dist-packages/vllm/worker/worker.py", line 302, in _init_distributed_environment torch.distributed.all_reduce(torch.zeros(1).cuda()) File "/usr/local/lib/python3.8/dist-packages/torch/distributed/distributed_c10d.py", line 1451, in wrapper return func(*args, **kwargs) File "/usr/local/lib/python3.8/dist-packages/torch/distributed/distributed_c10d.py", line 1700, in all_reduce work = default_pg.allreduce([tensor], opts) torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1275, internal error, NCCL version 2.14.3 ncclInternalError: Internal check failed. Last error: Call to bind failed : Address already in use ``` Why is this? development dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: k (most recent call last): File "test.py", line 14, in llm = LLM(model=path) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/llm.py", line 56, in __init__ self.llm_engine = LLMEngine.from_engine_args(engin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug] torch.distributed.DistBackendError: NCCL error .... Address already in use ``` Traceback (most recent call last): File "test.py", line 14, in llm = LLM(model=path) File "/usr/local/lib/python3.8/dist-packages/vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _distributed_environment torch.distributed.all_reduce(torch.zeros(1).cuda()) File "/usr/local/lib/python3.8/dist-packages/torch/distributed/distributed_c10d.py", line 1451, in wrapper return func(*args, **kwargs) File "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: . Address already in use ``` Traceback (most recent call last): File "test.py", line 14, in llm = LLM(model=path) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/llm.py", line 56, in __init__ self.llm_engi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
