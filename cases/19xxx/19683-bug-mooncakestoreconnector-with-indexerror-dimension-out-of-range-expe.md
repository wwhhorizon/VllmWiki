# vllm-project/vllm#19683: [Bug]:MooncakeStoreConnector with IndexError('Dimension out of range (expected to be in range of [-2, 1], but got 2)') ,because the new cache_kernels.cu changed.

| 字段 | 值 |
| --- | --- |
| Issue | [#19683](https://github.com/vllm-project/vllm/issues/19683) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:MooncakeStoreConnector with IndexError('Dimension out of range (expected to be in range of [-2, 1], but got 2)') ,because the new cache_kernels.cu changed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When i use the Mooncakestoreconnector,there is a bug between Mooncake and cache_kernels.cu. `ERROR 06-16 11:58:22 [engine.py:166] IndexError('Dimension out of range (expected to be in range of [-2, 1], but got 2)') ERROR 06-16 11:58:22 [engine.py:166] Traceback (most recent call last): ERROR 06-16 11:58:22 [engine.py:166] File "/vllm/vllm/engine/multiprocessing/engine.py", line 164, in start ERROR 06-16 11:58:22 [engine.py:166] self.run_engine_loop() ERROR 06-16 11:58:22 [engine.py:166] File "/vllm/vllm/engine/multiprocessing/engine.py", line 227, in run_engine_loop ERROR 06-16 11:58:22 [engine.py:166] request_outputs = self.engine_step() ERROR 06-16 11:58:22 [engine.py:166] File "/vllm/vllm/engine/multiprocessing/engine.py", line 253, in engine_step ERROR 06-16 11:58:22 [engine.py:166] raise e ERROR 06-16 11:58:22 [engine.py:166] File "/vllm/vllm/engine/multiprocessing/engine.py", line 236, in engine_step ERROR 06-16 11:58:22 [engine.py:166] return self.engine.step() ERROR 06-16 11:58:22 [engine.py:166] File "/vllm/vllm/engine/llm_engine.py", line 1352, in step ERROR 06-16 11:58:22 [engine.py:166] outputs = self.model_executor.e...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: of [-2, 1], but got 2)') ,because the new cache_kernels.cu changed. bug;stale ### Your current environment ### 🐛 Describe the bug When i use the Mooncakestoreconnector,there is a bug between Mooncake and cache_kernels.c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cache;cuda;kernel;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 05) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ming to the new expected shape of the KV cache. The bug appears to be a regression, triggered by the following change: (https://github.com/vllm-project/vllm/pull/16605) ### Before submitting a new issue... - [x] Make su...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cache;cuda;kernel;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
