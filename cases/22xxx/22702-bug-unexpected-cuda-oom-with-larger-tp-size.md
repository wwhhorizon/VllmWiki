# vllm-project/vllm#22702: [Bug]: Unexpected CUDA OOM with larger TP size

| 字段 | 值 |
| --- | --- |
| Issue | [#22702](https://github.com/vllm-project/vllm/issues/22702) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator |
| 症状 | crash;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected CUDA OOM with larger TP size

### Issue 正文摘录

### Your current environment vllm 0.8.5.dev ### 🐛 Describe the bug I have the following vllm config: ```python disable_log_stats: false gpu_memory_utilization: 0.87 block_size: 16 max_model_len: 36000 enforce_eager: false tensor_parallel_size: 1 ``` and I use fixed context length 8K with batch size 512 to test the preemption during the rollout phase of RLVR workload, and I have the following experiment settings: ```bash EXPERIMENTS=( # [model, gpu_mem_util, track_name_prefix] [0]="Qwen/Qwen2.5-7B 0.87 qwen2_5-7B-1" [1]="Qwen/Qwen2.5-7B 0.85 qwen2_5-7B-2" [2]="Qwen/Qwen3-8B 0.83 qwen3-8B-3" [3]="Qwen/Qwen3-8B 0.78 qwen3-8B-4" ) ``` All these experiments runs well on `tensor_parallel_size` 1 and 2. However, when I further increase `tensor_parallel_size` to 4, cuda OOM happens for experiments [0, 1, 2], the following error is from experiment 0, all others are similiar ``` [36m(ActorWorker(actor_infer-0) pid=33521, ip=10.17.71.58)[0m ERROR 08-12 00:30:03 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): [36m(ActorWorker(actor_infer-0) pid=33521, ip=10.17.71.58)[0m ERROR 08-12 00:30:03 [core.py:387] File "/checkpoint/binary/vllm084/vllm/v1/engine/core.py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: :387] File "/root/.local/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 150, in get [36m(ActorWorker(actor_infer-0) pid=33521, ip=10.17.71.58)[0m ERROR 08-12 00:30:03 [core.py:387] return _pr...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Unexpected CUDA OOM with larger TP size bug;stale ### Your current environment vllm 0.8.5.dev ### 🐛 Describe the bug I have the following vllm config: ```python disable_log_stats: false gpu_memory_utilization: 0....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: e bug I have the following vllm config: ```python disable_log_stats: false gpu_memory_utilization: 0.87 block_size: 16 max_model_len: 36000 enforce_eager: false tensor_parallel_size: 1 ``` and I use fixed context length...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nment vllm 0.8.5.dev ### 🐛 Describe the bug I have the following vllm config: ```python disable_log_stats: false gpu_memory_utilization: 0.87 block_size: 16 max_model_len: 36000 enforce_eager: false tensor_parallel_size...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Unexpected CUDA OOM with larger TP size bug;stale ### Your current environment vllm 0.8.5.dev ### 🐛 Describe the bug I have the following vllm config: ```python disable_log_stats: false gpu_memory_utilization: 0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
