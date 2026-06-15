# vllm-project/vllm#308: Support Multi-gpus inference on 3090s

| 字段 | 值 |
| --- | --- |
| Issue | [#308](https://github.com/vllm-project/vllm/issues/308) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> Support Multi-gpus inference on 3090s

### Issue 正文摘录

Hi, I can successfully infer with a single 3090, but setting tensor_parallel_size=2 throws the following error: Traceback (most recent call last): File "test_batch.py", line 78, in llm = LLM(model=args.model_path, tensor_parallel_size=2) File "/data/xuhao/xcxhy/vllm/vllm/entrypoints/llm.py", line 55, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/data/xuhao/xcxhy/vllm/vllm/engine/llm_engine.py", line 151, in from_engine_args engine = cls(*engine_configs, distributed_init_method, devices, File "/data/xuhao/xcxhy/vllm/vllm/engine/llm_engine.py", line 102, in __init__ self._init_cache() File "/data/xuhao/xcxhy/vllm/vllm/engine/llm_engine.py", line 114, in _init_cache num_blocks = self._run_workers( File "/data/xuhao/xcxhy/vllm/vllm/engine/llm_engine.py", line 317, in _run_workers all_outputs = ray.get(all_outputs) File "/data/anaconda3/envs/LLM-INFER/lib/python3.8/site-packages/ray/_private/client_mode_hook.py", line 105, in wrapper return func(*args, **kwargs) File "/data/anaconda3/envs/LLM-INFER/lib/python3.8/site- packages/ray/_private/worker.py", line 2523, in get raise value ray.exceptions.RayActorError: The actor died because of an error raised in...

## 现有链接修复摘要

#36522 [Docs] Add Apple MPS (Metal) GPU installation guide | #36523 [Platform] Add MPS (Apple Metal) platform support for macOS

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /csrc/distributed/c10d/ProcessGroup NCCL.cpp:1275, internal error, NCCL version 2.14.3 ncclInternalError: Internal check failed. Last error: Cuda failure 'peer access is not supported between these two devices' (Worker...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t recent call last): File "test_batch.py", line 78, in llm = LLM(model=args.model_path, tensor_parallel_size=2) File "/data/xuhao/xcxhy/vllm/vllm/entrypoints/llm.py", line 55, in __init__ self.llm_engine = LLMEngine.fro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ce work = default_pg.allreduce([tensor], opts) torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroup NCCL.cpp:1275, internal error, NCCL version 2.14.3 ncclInternalError: Interna...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _distributed_environment torch.distributed.all_reduce(torch.zeros(1).cuda()) File "/data/anaconda3/envs/LLM-INFER/lib/python3.8/site-packages/torch/distributed/distributed_c10d.py", line 1451, in wrapper return func(*ar...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: /xcxhy/vllm/vllm/engine/llm_engine.py", line 114, in _init_cache num_blocks = self._run_workers( File "/data/xuhao/xcxhy/vllm/vllm/engine/llm_engine.py", line 317, in _run_workers all_outputs = ray.get(all_outputs) File...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36522](https://github.com/vllm-project/vllm/pull/36522) | mentioned | 0.6 | [Docs] Add Apple MPS (Metal) GPU installation guide | `mps-platform-support` branch — Implementation - huggingface/kernels #308 — Metal kernel builder infrastructure |
| [#36523](https://github.com/vllm-project/vllm/pull/36523) | mentioned | 0.6 | [Platform] Add MPS (Apple Metal) platform support for macOS | ed - #1441 — Feature request: Apple Silicon support (86 reactions) - huggingface/kernels#308 — Metal kernel builder infrastructure - Metal compute kernels: [rotary-embedding](http… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
