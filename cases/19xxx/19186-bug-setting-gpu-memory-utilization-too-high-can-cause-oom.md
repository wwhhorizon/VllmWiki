# vllm-project/vllm#19186: [Bug]: Setting gpu-memory-utilization too high can cause OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#19186](https://github.com/vllm-project/vllm/issues/19186) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Setting gpu-memory-utilization too high can cause OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When gpu-memory-utilization is set to 0.95, OOM occurs. After reducing it to 0.9, it becomes normal. ```python vllm serve /input0/FairyR1-14B-Preview --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.95 --max-num-seqs 1 --tensor-parallel-size 4 --max-model-len 100 --served-model-name FairyR1-14B-Preview ``` ``` (VllmWorker rank=3 pid=1090) ERROR 06-05 06:18:13 [multiproc_executor.py:470] File "/usr/local/lib/python3.10/site-packages/vllm/compilation/backends.py", line 681, in __call__ (VllmWorker rank=3 pid=1090) ERROR 06-05 06:18:13 [multiproc_executor.py:470] with torch.cuda.graph(cudagraph, pool=self.graph_pool): (VllmWorker rank=3 pid=1090) ERROR 06-05 06:18:13 [multiproc_executor.py:470] File "/usr/local/lib/python3.10/site-packages/torch/cuda/graphs.py", line 186, in __exit__ (VllmWorker rank=3 pid=1090) ERROR 06-05 06:18:13 [multiproc_executor.py:470] self.cuda_graph.capture_end() (VllmWorker rank=3 pid=1090) ERROR 06-05 06:18:13 [multiproc_executor.py:470] File "/usr/local/lib/python3.10/site-packages/torch/cuda/graphs.py", line 84, in capture_end (VllmWorker rank=3 pid=1090) ERROR 06-05 06:18:13 [multiproc_executor.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e bug When gpu-memory-utilization is set to 0.95, OOM occurs. After reducing it to 0.9, it becomes normal. ```python vllm serve /input0/FairyR1-14B-Preview --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.95 --max-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: id=1090) ERROR 06-05 06:18:13 [multiproc_executor.py:470] with torch.cuda.graph(cudagraph, pool=self.graph_pool): (VllmWorker rank=3 pid=1090) ERROR 06-05 06:18:13 [multiproc_executor.py:470] File "/usr/local/lib/python...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: py:470] File "/usr/local/lib/python3.10/site-packages/vllm/compilation/backends.py", line 681, in __call__ (VllmWorker rank=3 pid=1090) ERROR 06-05 06:18:13 [multiproc_executor.py:470] with torch.cuda.graph(cudagraph, p...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: del_support;speculative_decoding cuda;kernel;operator;triton build_error;mismatch;oom env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Setting gpu-memory-utilization too high can cause OOM bug ### Your current environment ### 🐛 Describe the bug When gpu-memory-utilization is set to 0.95, OOM occurs. After reducing it to 0.9, it becomes normal. `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
