# vllm-project/vllm#12395: [Performance]: Unexpected performance of vLLM Cascade Attention

| 字段 | 值 |
| --- | --- |
| Issue | [#12395](https://github.com/vllm-project/vllm/issues/12395) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: Unexpected performance of vLLM Cascade Attention

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I noticed that vLLM has implemented Cascade Attention in this PR: [[V1] Implement Cascade Attention #11635 ](https://github.com/vllm-project/vllm/pull/11635). I conducted some benchmarks with the Qwen2-0.5B model on an A100, aiming to determine whether it would be beneficial when most requests in the batch share a long common prefix. I'm testing with `Qwen2-0.5B-Instruct`, using an input sequence length of `1024`, batch sizes of `8` and `7`, and an output length of `1`, vLLM main branch with commit id `1f1542afa915e0975d2b63559424403e5e8aae2c`. However, it turns out that Cascade Attention did not show much improvement, and the latency exhibited a large standard deviation compared to the vLLM v0 implementation. - The baseline: (v0 implementation) ![Image](https://github.com/user-attachments/assets/d5ffc472-8ab8-4893-9862-86ff52860d03) - Cascade Attention: (VLLM_USE_V1=1) ![Image](https://github.com/user-attachments/assets/a28d7e93-07b4-439f-99d1-d9df895ca158) And here is the benchmark script: ``` from vllm import LLM, SamplingParams import random import time import statistics import matplotlib.py...

## 现有链接修复摘要

#11635 [V1] Implement Cascade Attention

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: en2-0.5B model on an A100, aiming to determine whether it would be beneficial when most requests in the batch share a long common prefix. I'm testing with `Qwen2-0.5B-Instruct`, using an input sequence length of `1024`,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: pull/11635). I conducted some benchmarks with the Qwen2-0.5B model on an A100, aiming to determine whether it would be beneficial when most requests in the batch share a long common prefix. I'm testing with `Qwen2-0.5B-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: .com/vllm-project/vllm/pull/11635). I conducted some benchmarks with the Qwen2-0.5B model on an A100, aiming to determine whether it would be beneficial when most requests in the batch share a long common prefix. I'm te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: roposal to improve performance _No response_ ### Report of performance regression I noticed that vLLM has implemented Cascade Attention in this PR: [[V1] Implement Cascade Attention #11635 ](https://github.com/vllm-proj...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rformance]: Unexpected performance of vLLM Cascade Attention performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I noticed that vLLM has implemented Cascade Attention...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#11635](https://github.com/vllm-project/vllm/pull/11635) | mentioned | 0.45 | [V1] Implement Cascade Attention | nted cascade attention in this pr: [[v1] implement cascade attention #11635 ](https://github.com/vllm-project/vllm/pull/11635). i conducted some benchmarks with the qwen2-0.5b mod… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
