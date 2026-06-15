# vllm-project/vllm#27034: [Bug]: Incorrect outputs with batch size > 1 on AArch64 CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#27034](https://github.com/vllm-project/vllm/issues/27034) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;mismatch;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect outputs with batch size > 1 on AArch64 CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Incorrect outputs with batch size > 1 on CPU I tested (see script below) a 1b llama instruct model (with greedy decoding - i.e. deterministic) and found out the following: - when prefix caching is disabled (not the default case): output from generating responses to a batch of 5 requests differs from generating the the output of these requests one at a time. Only the first request in the batch is correct. This is because we do prefill (for all but first prompt) over wrong query/key/value tensor - when prefix caching is enabled (default case): output from generating responses to a batch of 5 requests differs from generating the the output of these requests one at a time AND also different from the case where prefix caching is disabled this is because with prefix caching we cache the K/V of the prefix (which we prefilled for an earlier prompt) in the paged cache, which our prefill SDPA is not aware of - i.e. our prefill SDPA only runs over K/V from the suffix. Here are five prompts I tested: - Memorize this short fact for later: the verification passphrase is cobalt fig 41. Answer the following, with no explanation: what is the veri...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: see script below) a 1b llama instruct model (with greedy decoding - i.e. deterministic) and found out the following: - when prefix caching is disabled (not the default case): output from generating responses to a batch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bar on August 27, 1896, and lasted only 38 minutes."\nThis fact is often cited as the shortest war in recorded history. Here's a script to reproduce the issues: ``` # SPDX-FileCopyrightText: Copyright 2025 Arm Limited a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Incorrect outputs with batch size > 1 on AArch64 CPU bug ### Your current environment ### 🐛 Describe the bug Incorrect outputs with batch size > 1 on CPU I tested (see script below) a 1b llama instruct model (wit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ect outputs with batch size > 1 on CPU I tested (see script below) a 1b llama instruct model (with greedy decoding - i.e. deterministic) and found out the following: - when prefix caching is disabled (not the default ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: (not the default case): output from generating responses to a batch of 5 requests differs from generating the the output of these requests one at a time. Only the first request in the batch is correct. This is because w...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
