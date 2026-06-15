# vllm-project/vllm#14647: [Bug]: EAGLE / DeepSeek MTP Handles First Input Token Incorrectly - 25% Acceptance Rate Drop

| 字段 | 值 |
| --- | --- |
| Issue | [#14647](https://github.com/vllm-project/vllm/issues/14647) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE / DeepSeek MTP Handles First Input Token Incorrectly - 25% Acceptance Rate Drop

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug According to its paper, EAGLE concatenates the hidden states of the current token with the embedding of the next token. The embedding of the first token in a sequence is not used, as shown in the diagram below (embedding of 'how'). Since MPT essentially has the same design in this regard, I will simply describe the bug for EAGLE. This design poses challenges in vLLM, as we need to obtain separate attention metadata for EAGLE. Currently, the EAGLE implementation in vLLM employs a hack to bypass this challenge via 1) obtaining a dummy first token by concatenating the last prompt token's hidden states (as a result of right shifting [here](https://github.com/vllm-project/vllm/blob/main/vllm/spec_decode/spec_decode_worker.py#L1317)) and the first prompt token's embedding, and 2) setting their projection to zero before passing to the main model layer. While this seems to be a smart trick and does not cause any errors, it has deep problems. This hack is currently used in both EAGLE [[line]](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/eagle.py#L134C9-L134C74) and DeepSeek MTP [[line]](https://github.com/vllm...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: MTP Handles First Input Token Incorrectly - 25% Acceptance Rate Drop bug;stale ### Your current environment ### 🐛 Describe the bug According to its paper, EAGLE concatenates the hidden states of the current token with t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;cuda;operato...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: to zero before passing to the main model layer. While this seems to be a smart trick and does not cause any errors, it has deep problems. This hack is currently used in both EAGLE [[line]](https://github.com/vllm-projec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n score will always be off by 1 for all tokens, which harms the drafting accuracy. On a less critical note, the position ids for EAGLE are also all off by 1. In fact, as a temporary solution, we might be better off remo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ogits;speculative_decoding attention;cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
