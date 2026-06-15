# vllm-project/vllm#30083: [Bug]: B200 prefill performance with deepep HT is ~50% of H200

| 字段 | 值 |
| --- | --- |
| Issue | [#30083](https://github.com/vllm-project/vllm/issues/30083) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: B200 prefill performance with deepep HT is ~50% of H200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deploying the latest llm-d configuration for wide expert parallelism on B200s, the EP=16 prefill server appears to saturate at about 44k prefill tokens/s or about 5.7k prefill tokens/s/gpu: The [configuration here](https://github.com/llm-d/llm-d/blob/83dd587dd847498820314e8144aadb4fa90d451f/guides/wide-ep-lws/manifests/modelserver/base/prefill.yaml#L61) covers tuning parameters in use. DeepEP normal mode benchmarks (test inter node) show expected throughput and latency for CX7 RDMA NICs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: B200 prefill performance with deepep HT is ~50% of H200 bug;stale ### Your current environment ### 🐛 Describe the bug Deploying the latest llm-d configuration for wide expert parallelism on B200s, the EP=16 prefi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ### Your current environment ### 🐛 Describe the bug Deploying the latest llm-d configuration for wide expert parallelism on B200s, the EP=16 prefill server appears to saturate at about 44k prefill tokens/s or about 5.7k...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ## 🐛 Describe the bug Deploying the latest llm-d configuration for wide expert parallelism on B200s, the EP=16 prefill server appears to saturate at about 44k prefill tokens/s or about 5.7k prefill tokens/s/gpu: The [co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: B200 prefill performance with deepep HT is ~50% of H200 bug;stale ### Your current environment ### 🐛 Describe the bug Deploying the latest llm-d configuration for wide expert parallelism on B200s, the EP=16 prefi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
