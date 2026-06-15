# vllm-project/vllm#2017: TypeError: PaddedGatherOp.forward() takes 6 positional arguments but 7 were given

| 字段 | 值 |
| --- | --- |
| Issue | [#2017](https://github.com/vllm-project/vllm/issues/2017) |
| 状态 | closed |
| 标签 |  |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: PaddedGatherOp.forward() takes 6 positional arguments but 7 were given

### Issue 正文摘录

I installed from latest main, installed stk, megablocks, latest flash_attn, transformers etc... And got following error: ```llm.engine.ray_utils.RayWorkerVllm object at 0x7f1657fe5bd0>) File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/vllm/engine/ray_utils.py", line 32, in execute_method return executor(*args, **kwargs) File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/vllm/worker/worker.py", line 88, in profile_num_available_blocks self.model_runner.profile_run() File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 321, in profile_run self.execute_model(seqs, kv_caches) File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 279, in execute_model hidd...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rward() takes 6 positional arguments but 7 were given I installed from latest main, installed stk, megablocks, latest flash_attn, transformers etc... And got following error: ```llm.engine.ray_utils.RayWorkerVllm object...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e[misc] File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/stk/backend/autocast.py", line 28, in decorate_fwd return fwd(*args, **kwargs) TypeError: PaddedGatherOp.forward() takes 6 positional arguments but 7 we...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: PaddedGatherOp.forward() takes 6 positional arguments but 7 were given I installed from latest main, installed stk, megablocks, latest flash_attn, transformers etc... And got following error: ```llm.engine.ray_utils.Ray...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: uments but 7 were given I installed from latest main, installed stk, megablocks, latest flash_attn, transformers etc... And got following error: ```llm.engine.ray_utils.RayWorkerVllm object at 0x7f1657fe5bd0>) File "/ho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: llm/worker/worker.py", line 88, in profile_num_available_blocks self.model_runner.profile_run() File "/home/ubuntu/mambaforge/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context retur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
