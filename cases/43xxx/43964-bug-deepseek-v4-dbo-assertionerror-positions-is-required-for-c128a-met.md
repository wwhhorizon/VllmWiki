# vllm-project/vllm#43964: [Bug][Deepseek v4][DBO]: AssertionError: positions is required for C128A metadata build File

| 字段 | 值 |
| --- | --- |
| Issue | [#43964](https://github.com/vllm-project/vllm/issues/43964) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Deepseek v4][DBO]: AssertionError: positions is required for C128A metadata build File

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving DeepSeek V4 Flash with DBO enabled on the prefill side, long-prompt requests can crash the prefill worker during attention metadata construction. The crash happens when a long prefill request triggers DBO ubatching. vLLM rebuilds `CommonAttentionMetadata` for each ubatch, but the rebuilt metadata on the DBO path drops the `positions` field. Later, DeepSeek V4 Flash MLA sparse hits the C128A metadata path, which requires `cm.positions`, and fails with: ```text AssertionError: positions is required for C128A metadata build File ".../vllm/v1/attention/backends/mla/flashmla_sparse.py", line 661 ``` ## Reproduction conditions This reproduces reliably in the following setup: - Model: DeepSeek V4 Flash - Deployment: PD-disaggregated deployment - Side: prefill - vLLM: 0.21.0 - DBO: enabled - `dboPrefillTokenThreshold`: configured low enough to trigger ubatching on long prompts - Workload: `lm_eval` on `gsm8k` ## Log ``` (Worker_DP1_EP1 pid=10457) ERROR 05-29 16:21:42 [multiproc_executor.py:962] WorkerProc hit an exception. (Worker_DP1_EP1 pid=10457) ERROR 05-29 16:21:42 [multiproc_executor.py:962] Traceback (most recent call...

## 现有链接修复摘要

#43966 [Bugfix]: preserve DeepSeek V4 ubatch metadata for DBO prefills

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: pseek v4][DBO]: AssertionError: positions is required for C128A metadata build File bug ### Your current environment ### 🐛 Describe the bug When serving DeepSeek V4 Flash with DBO enabled on the prefill side, long-promp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: w enough to trigger ubatching on long prompts - Workload: `lm_eval` on `gsm8k` ## Log ``` (Worker_DP1_EP1 pid=10457) ERROR 05-29 16:21:42 [multiproc_executor.py:962] WorkerProc hit an exception. (Worker_DP1_EP1 pid=1045...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Describe the bug When serving DeepSeek V4 Flash with DBO enabled on the prefill side, long-prompt requests can crash the prefill worker during attention metadata construction. The crash happens when a long prefill reque...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: sitions is required for C128A metadata build File ".../vllm/v1/attention/backends/mla/flashmla_sparse.py", line 661 ``` ## Reproduction conditions This reproduces reliably in the following setup: - Model: DeepSeek V4 Fl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oduction conditions This reproduces reliably in the following setup: - Model: DeepSeek V4 Flash - Deployment: PD-disaggregated deployment - Side: prefill - vLLM: 0.21.0 - DBO: enabled - `dboPrefillTokenThreshold`: confi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43966](https://github.com/vllm-project/vllm/pull/43966) | mentioned | 0.6 | [Bugfix]: preserve DeepSeek V4 ubatch metadata for DBO prefills | l continuations are not misclassified after ubatch splitting Issue #43964 is one example of this issue. ## Test Plan - Hardware: H20 * 8 - vLLM: 0.21.0 - CUDA: 13.0 - Model: |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
