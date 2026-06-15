# vllm-project/vllm#43738: [Bug]: AttributeError: module 'cutlass.cute.arch' has no attribute 'fmin'

| 字段 | 值 |
| --- | --- |
| Issue | [#43738](https://github.com/vllm-project/vllm/issues/43738) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: module 'cutlass.cute.arch' has no attribute 'fmin'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] Traceback (most recent call last): (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] File "/vllm/vllm/v1/executor/multiproc_executor.py", line 957, in worker_busy_loop (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] output = func(*args, **kwargs) (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^ (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] File "/vllm/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] return func(*args, **kwargs) (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^ (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] File "/vllm/vllm/v1/worker/gpu_worker.py", line 411, in determine_available_memory (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] cudagraph_memory_estimate = se...

## 现有链接修复摘要

#44236 fix: resolve CUTLASS fmin compatibility for DeepSeek-V4 init

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 16) ERROR 05-26 18:29:06 [multiproc_executor.py:962] return self.aot_compiled_fn(self, *args, **kwargs) (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ERROR 05-26 18:29:06 [multiproc_executor.py:962] ).launch(grid=grid, block=(self.tb_size, 1, 1), stream=stream) (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: AttributeError: module 'cutlass.cute.arch' has no attribute 'fmin' bug ### Your current environment ### 🐛 Describe the bug ``` (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] Traceba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 8:29:06 [multiproc_executor.py:962] cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory() (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: iproc_executor.py:962] cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory() (Worker_DP4_EP4 pid=2635016) ERROR 05-26 18:29:06 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44236](https://github.com/vllm-project/vllm/pull/44236) | mentioned | 0.6 | fix: resolve CUTLASS fmin compatibility for DeepSeek-V4 init | dule cutlass.cute.arch has no attribute fmin ``` Reported in #44210, #43738, and the original discussion on #43584. ## Fix `cutlass.min` is the canonical CuTe DSL API for element-… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
