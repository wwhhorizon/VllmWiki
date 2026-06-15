# vllm-project/vllm#41623: [Bug]: Decode Context Parallelism (`--decode-context-parallel-size`) output drift and gibberish in v0.21.0 and latest nightly

| 字段 | 值 |
| --- | --- |
| Issue | [#41623](https://github.com/vllm-project/vllm/issues/41623) |
| 状态 | open |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Decode Context Parallelism (`--decode-context-parallel-size`) output drift and gibberish in v0.21.0 and latest nightly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GPU: 8x A100 `vllm serve moonshotai/Kimi-K2.6 --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --api-server-count 8 --tensor-parallel-size 8 --decode-context-parallel-size 8 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 32 --gpu-memory-utilization 0.95 --max-model-len 262144 --enable-auto-tool-choice --tool-call-parser kimi_k2 --reasoning-parser kimi_k2 --mm-processor-cache-gb 8 --mm-processor-cache-type shm` Decode Context Parallelism (DCP, `--decode-context-parallel-size`) produces unrelated gibberish output in latest nightly. This is a regression. Happens somewhere between `a749a33d8d05acdd3ab346bd3f0c6b5c9c80474f` (works well) `01d4d1ad375dc5854779c593eee093bcebb0cada` (gibberish output). Only when `--decode-context-parallel-size` is set, Kimi-K2.6 leads to completely unrelated gibberish. Problematic commit is between the above commits. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer...

## 现有链接修复摘要

#42884 [WIP][Bugfix] Drop workspace allocation for DCP A2A send/recv buffers (#41623)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Decode Context Parallelism (`--decode-context-parallel-size`) output drift and gibberish in v0.21.0 and latest nightly bug ### Your current environment ### 🐛 Describe the bug GPU: 8x A100 `vllm serve moonshotai/K...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;samp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Decode Context Parallelism (`--decode-context-parallel-size`) output drift and gibberish in v0.21.0 and latest nightly bug ### Your current environment ### 🐛 Describe the bug GPU: 8x A100 `vllm serve moonshotai/K...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ai/Kimi-K2.6 --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --api-server-count 8 --tensor-parallel-size 8 --decode-context-parallel-size 8 --trust-remote-code --enable-chunked-prefill --enab...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: code-context-parallel-size`) output drift and gibberish in v0.21.0 and latest nightly bug ### Your current environment ### 🐛 Describe the bug GPU: 8x A100 `vllm serve moonshotai/Kimi-K2.6 --port 5000 --host 0.0.0.0 --do...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42884](https://github.com/vllm-project/vllm/pull/42884) | mentioned | 0.6 | [WIP][Bugfix] Drop workspace allocation for DCP A2A send/recv buffers (#41623) | WIP][Bugfix] Drop workspace allocation for DCP A2A send/recv buffers (#41623) ## Purpose PR #41160 made `_dcp_a2a_send_recv_buffers` allocate `send_buffer` and `recv_buffer` from… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
