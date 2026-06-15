# vllm-project/vllm#14583: [Bug]: ERROR 03-11 07:47:00 [engine.py:141] AttributeError: Invalid attention type encoder-only

| 字段 | 值 |
| --- | --- |
| Issue | [#14583](https://github.com/vllm-project/vllm/issues/14583) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ERROR 03-11 07:47:00 [engine.py:141] AttributeError: Invalid attention type encoder-only

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ERROR 03-11 07:47:00 [engine.py:141] AttributeError('Invalid attention type encoder_only') ERROR 03-11 07:47:00 [engine.py:141] Traceback (most recent call last): ERROR 03-11 07:47:00 [engine.py:141] File "/home/radmin/gitlab/vllm/vllm/engine/multiprocessing/engine.py", line 139, in start ERROR 03-11 07:47:00 [engine.py:141] self.run_engine_loop() ERROR 03-11 07:47:00 [engine.py:141] File "/home/radmin/gitlab/vllm/vllm/engine/multiprocessing/engine.py", line 202, in run_engine_loop ERROR 03-11 07:47:00 [engine.py:141] request_outputs = self.engine_step() ERROR 03-11 07:47:00 [engine.py:141] ^^^^^^^^^^^^^^^^^^ ERROR 03-11 07:47:00 [engine.py:141] File "/home/radmin/gitlab/vllm/vllm/engine/multiprocessing/engine.py", line 228, in engine_step ERROR 03-11 07:47:00 [engine.py:141] raise e ERROR 03-11 07:47:00 [engine.py:141] File "/home/radmin/gitlab/vllm/vllm/engine/multiprocessing/engine.py", line 211, in engine_step ERROR 03-11 07:47:00 [engine.py:141] return self.engine.step() ERROR 03-11 07:47:00 [engine.py:141] ^^^^^^^^^^^^^^^^^^ ERROR 03-11 07:47:00 [engine.py:141] File "/home/radmin/gitlab/vllm/vllm/engine/llm_engine.py", line...

## 现有链接修复摘要

#14664 [FEAT] [ROCm] [Embedding] Add encoder-only model support into ROCm Flash Attention to enable embedding models.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 07:47:00 [engine.py:141] File "/home/radmin/gitlab/vllm/vllm/attention/backends/rocm_flash_attn.py", line 667, in forward ERROR 03-11 07:47:00 [engine.py:141] causal_mask) = _get_seq_len_block_table_args( ERROR 03-11 07...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [engine.py:141] File "/home/radmin/gitlab/vllm/vllm/attention/backends/rocm_flash_attn.py", line 667, in forward ERROR 03-11 07:47:00 [engine.py:141] causal_mask) = _get_seq_len_block_table_args( ERROR 03-11 07:47:00 [e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 41] return self.impl.forward(self, query, key, value, kv_cache, attn_metadata) ERROR 03-11 07:47:00 [engine.py:141] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-11 07:47:00 [engine.py:141...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ", line 202, in run_engine_loop ERROR 03-11 07:47:00 [engine.py:141] request_outputs = self.engine_step() ERROR 03-11 07:47:00 [engine.py:141] ^^^^^^^^^^^^^^^^^^ ERROR 03-11 07:47:00 [engine.py:141] File "/home/radmin/g...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14664](https://github.com/vllm-project/vllm/pull/14664) | closes_keyword | 0.95 | [FEAT] [ROCm] [Embedding] Add encoder-only model support into ROCm Flash Attention to enable embedding models. | FIX #14583 # File changes: * `vllm/attention/backends/rocm_flash_attn.py`: Add ENCODER_ONLY code path * `tests/models/embedding/language/test_embedding.py`: Fix the code logic to |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
