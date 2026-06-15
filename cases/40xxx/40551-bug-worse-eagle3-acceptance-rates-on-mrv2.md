# vllm-project/vllm#40551: [Bug]: Worse EAGLE3 acceptance rates on MRV2

| 字段 | 值 |
| --- | --- |
| Issue | [#40551](https://github.com/vllm-project/vllm/issues/40551) |
| 状态 | closed |
| 标签 | bug;help wanted |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Worse EAGLE3 acceptance rates on MRV2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran MT-Bench with Temp=0 and Temp=1 and got better acceptance rates using MRV1 than MRV2. I would expect the opposite given the improvements to draft-prob-aware sampling in MRV2. launch script: ``` export VLLM_USE_V2_MODEL_RUNNER=1 python3 -m \ vllm.entrypoints.cli.main serve Qwen/Qwen3-8B --port 9000 --speculative-config '{"method": "eagle3", "model": "RedHatAI/Qwen3-8B-speculator.eagle3", "num_speculative_tokens": 7}' --max-num-batched-tokens 32768 ``` ### MRV1 Temp=0 ``` ============ Serving Benchmark Result ============ Successful requests: 80 Failed requests: 0 Benchmark duration (s): 5.20 Total input tokens: 6078 Total generated tokens: 20478 Request throughput (req/s): 15.38 Output token throughput (tok/s): 3936.20 Peak output token throughput (tok/s): 1840.00 Peak concurrent requests: 80.00 Total token throughput (tok/s): 5104.49 ---------------Time to First Token---------------- Mean TTFT (ms): 149.95 Median TTFT (ms): 165.88 P99 TTFT (ms): 171.82 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 17.57 Median TPOT (ms): 17.85 P99 TPOT (ms): 19.84 ---------------Inter-token Latency---------------- Mean...

## 现有链接修复摘要

#41281 [CI] Wire EAGLE3 acceptance length tests into spec_decode nightly lanes

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: -num-batched-tokens 32768 ``` ### MRV1 Temp=0 ``` ============ Serving Benchmark Result ============ Successful requests: 80 Failed requests: 0 Benchmark duration (s): 5.20 Total input tokens:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ng MRV1 than MRV2. I would expect the opposite given the improvements to draft-prob-aware sampling in MRV2. launch script: ``` export VLLM_USE_V2_MODEL_RUNNER=1 python3 -m \ vllm.entrypoints.cli.main serve Qwen/Qwen3-8B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: raft-prob-aware sampling in MRV2. launch script: ``` export VLLM_USE_V2_MODEL_RUNNER=1 python3 -m \ vllm.entrypoints.cli.main serve Qwen/Qwen3-8B --port 9000 --speculative-config '{"method": "eagle3", "model": "RedHatAI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41281](https://github.com/vllm-project/vllm/pull/41281) | mentioned | 0.6 | [CI] Wire EAGLE3 acceptance length tests into spec_decode nightly lanes | yaml. This gap allowed the Model Runner V2 acceptance regression (vllm#40551 / fix vllm#40656) to reach production undetected. Add H100 and B200 nightly lanes in spec_decode.yaml… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
