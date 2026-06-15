# vllm-project/vllm#14649: [Bug]: EAGLE / MTP Doesn't Overwrite Approximated Hidden States / KV Cache, 8%- 15% Acceptance Length Degradation

| 字段 | 值 |
| --- | --- |
| Issue | [#14649](https://github.com/vllm-project/vllm/issues/14649) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE / MTP Doesn't Overwrite Approximated Hidden States / KV Cache, 8%- 15% Acceptance Length Degradation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This bug, incurring significant degradations to EAGLE's acceptance rate, is actually quite subtle, so I would like to first provide some contexts. As described in its paper, EAGLE tries to predict the hidden states of future tokens, and uses them autoregressively during drafting. The important point is that these hidden states are approximated, rather than ground truths from the target model. As a result, even though some draft tokens are accepted, their corresponding KV cache is to some extent, not accurate. Let $h$ be the hidden state from the target model, $\hat{h}$ be the hidden state predicted by the EAGLE model during drafting, and $e$ be the embedding of the accepted draft token. Now, the KV cache should be from some transformation of the concatenation of ($h$, $e$), not ($\hat{h}$, $e$). This is not immediately clear solely from the EAGLE paper, but is quite evident if we look at the codebase. In EAGLE’s codebase, the authors keep track of [stable_kv](https://github.com/SafeAILab/EAGLE/blob/v1/eagle/model/cnets.py#L773) which are KV cache from hidden states of the target model, which are retrieved [here]( https://github.c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: es of future tokens, and uses them autoregressively during drafting. The important point is that these hidden states are approximated, rather than ground truths from the target model. As a result, even though some draft...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed Hidden States / KV Cache, 8%- 15% Acceptance Length Degradation bug;unstale ### Your current environment ### 🐛 Describe the bug This bug, incurring significant degradations to EAGLE's acceptance rate, is actually qui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tt ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: idden states are approximated, rather than ground truths from the target model. As a result, even though some draft tokens are accepted, their corresponding KV cache is to some extent, not accurate. Let $h$ be the hidde...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ng_logits;speculative_decoding cache;cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
