# vllm-project/vllm#41733: [Roadmap] 2026 Q2 vLLM × RL Roadmap

| 字段 | 值 |
| --- | --- |
| Issue | [#41733](https://github.com/vllm-project/vllm/issues/41733) |
| 状态 | open |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cache;fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Roadmap] 2026 Q2 vLLM × RL Roadmap

### Issue 正文摘录

# [Roadmap] 2026 Q2 vLLM × RL Roadmap This tracks the Q2 2026 vLLM-side work needed to make RL workloads (training & rollout) first-class. Each item links its own RFC / issue / PR — please discuss there, and use this thread for cross-cutting prioritization. ## Training-Inference Consistency - [x] Support R3 routing replay: #39568 - [ ] Support PD + R3 - [ ] Support flashinfer + R3 https://github.com/vllm-project/vllm/pull/42981/changes#diff-80ee7e2a62f9dcfbb8a312dc4e3948557e97ef187290daebbcae1e28596bda29 - [ ] Fix logprobs / logits surface consistency: https://github.com/vllm-project/vllm/issues/42259 ## Runtime State Switching - [ ] Standardize weight sync lifecycle: #31848 - [ ] Sparse weight updates support https://github.com/vllm-project/vllm/issues/39451 - [x] Make pause / resume coordinator-safe https://github.com/vllm-project/vllm/issues/32103 - [ ] NCCL context offload / resume to save the reconstruction time. https://github.com/NVIDIA/nccl/releases/tag/v2.29.7-1 @aoshen02 ## Rollout Performance / Efficiency - [x] Improve KV cache / prefix reuse: https://vllm.ai/blog/mooncake-store https://github.com/vllm-project/vllm/pull/42694/changes#diff-1f7101183bf6c2328171823032cc29e...

## 现有链接修复摘要

#39568 [RFC] Replace shared-memory routed experts with ModelRunnerOutput transfer and HTTP support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: needed to make RL workloads (training & rollout) first-class. Each item links its own RFC / issue / PR — please discuss there, and use this thread for cross-cutting prioritization. ## Training-Inference Consistency - [x...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: igs https://github.com/vllm-project/vllm/issues/41821 - [ ] More mature FP8 WA KV-cache rollout support - [ ] RDMA-based cross-cluster transport for vLLM intermediate results — vLLM internally produces large per-request...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: to dynamically switch between throughput-optimized and latency-optimized configs https://github.com/vllm-project/vllm/issues/41821 - [ ] More mature FP8 WA KV-cache rollout support - [ ] RDMA-based cross-cluster transpo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 23032cc29e8ba98087d03fef92993abc88716dbcf7c @aoshen02 - [ ] Stabilize prefill decode disaggregation rollout: [verl-project/verl#6243](https://github.com/verl-project/verl/pull/6243) - [ ] Add phase-aware performance mod...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: fe https://github.com/vllm-project/vllm/issues/32103 - [ ] NCCL context offload / resume to save the reconstruction time. https://github.com/NVIDIA/nccl/releases/tag/v2.29.7-1 @aoshen02 ## Rollout Performance / Efficien...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39568](https://github.com/vllm-project/vllm/pull/39568) | mentioned | 0.45 | [RFC] Replace shared-memory routed experts with ModelRunnerOutput transfer and HTTP support | ## training-inference consistency - [x] support r3 routing replay: #39568 - [ ] support pd + r3 - [ ] support flashinfer + r3 https://github.com/vllm-project/vllm/pull/42981/chang… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
