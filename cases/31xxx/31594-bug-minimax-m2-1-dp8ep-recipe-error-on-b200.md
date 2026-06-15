# vllm-project/vllm#31594: [Bug]: MiniMax-M2.1 DP8EP Recipe Error on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#31594](https://github.com/vllm-project/vllm/issues/31594) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniMax-M2.1 DP8EP Recipe Error on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The [MiniMax-M2.1 DP8EP recipe](https://docs.vllm.ai/projects/recipes/en/latest/MiniMax/MiniMax-M2.html#launching-minimax-m21m2-with-vllm) runs into the following error when the max concurrency exceeds 4: ```text File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/flashinfer.py", line 1508, in build assert num_decode_tokens % num_decodes == 0, ( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError: TRTLLM decode requires uniform query lengths per request. EngineCore encountered a fatal error. ``` Server command: ```bash vllm serve MiniMaxAI/MiniMax-M2.1 \ --download-dir /model_weights \ --trust-remote-code \ --data-parallel-size 8 \ --enable-expert-parallel \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2_append_think \ --enable-auto-tool-choice \ --host 0.0.0.0 \ --port 8000 ``` Client command: ```bash git clone -b warmup git@github.com:kimbochen/bench_serving.git python3 /bench_serving/benchmark_serving.py \ --model MiniMaxAI/MiniMax-M2.1 \ --backend openai \ --base-url http://0.0.0.0:8000 \ --dataset-name random \ --random-input-len 8192 \ --random-output-len 512 \ --random-range-ratio 0.2 \...

## 现有链接修复摘要

#31693 Fix TRTLLM decode assertion error when query lengths are non-uniform #31594

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: MiniMax-M2.1 DP8EP Recipe Error on B200 bug;stale ### Your current environment ### 🐛 Describe the bug The [MiniMax-M2.1 DP8EP recipe](https://docs.vllm.ai/projects/recipes/en/latest/MiniMax/MiniMax-M2.html#launch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ```text File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/flashinfer.py", line 1508, in build assert num_decode_tokens % num_decodes == 0, ( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError: TR...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: MiniMax-M2.1 DP8EP Recipe Error on B200 bug;stale ### Your current environment ### 🐛 Describe the bug The [MiniMax-M2.1 DP8EP recipe](https://docs.vllm.ai/projects/recipes/en/latest/MiniMax/MiniMax-M2.html#launch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: MiniMax-M2.1 DP8EP Recipe Error on B200 bug;stale ### Your current environment ### 🐛 Describe the bug The [MiniMax-M2.1 DP8EP recipe](https://docs.vllm.ai/projects/recipes/en/latest/MiniMax/MiniMax-M2.html#launch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ts \ --trust-remote-code \ --data-parallel-size 8 \ --enable-expert-parallel \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2_append_think \ --enable-auto-tool-choice \ --host 0.0.0.0 \ --port 8000 ``` Cl...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31693](https://github.com/vllm-project/vllm/pull/31693) | closes_keyword | 0.95 | Fix TRTLLM decode assertion error when query lengths are non-uniform #31594 | Fixes #31594 TRTLLM decode kernels require all requests in a batch to have exactly the same number of query tokens. However, vLLM's dynamic batching, especially under high concur |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
