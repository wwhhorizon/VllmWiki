# vllm-project/vllm#37909: [Bug]: "none" reasoning effort doesn't do what it says it does (and may break output)

| 字段 | 值 |
| --- | --- |
| Issue | [#37909](https://github.com/vllm-project/vllm/issues/37909) |
| 状态 | open |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "none" reasoning effort doesn't do what it says it does (and may break output)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Adding support for 'none' as reasoning_effort in chat completions API (introduced in [this PR](https://github.com/vllm-project/vllm/pull/36238)) was done by not sending back the reasoning to the client. I think this is not the proper way to do this, because this field is typically used to reduce token consumption, not hide it. Additionally, my as far as i can understand the implementation, it has a side effect. I believe it triggers a mechanism where the generated tokens are not kept until an "end reasoning" token is seen. I hit a bug where no output was kept at all when I used reasoning_effort to disable reasoning by starting and ending the reasoning in the chat template. ``` {%- if reasoning_effort is defined and reasoning_effort == "none" %} {{- ' \n\n \n\n' }} {%- else %} {{- ' \n' }} {%- endif %} ``` By doing so, the "end reasoning" token is never seen by the code looking for it at generation time, and thus, no token is kept and sent back to the client. ([introduced here I guess](https://github.com/vllm-project/vllm/pull/36238/changes#diff-03bcd8dfd3695a2e555a45115d075db3213ed3dc5356f12eda676be711614456R784)) I suggest we re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the implementation, it has a side effect. I believe it triggers a mechanism where the generated tokens are not kept until an "end reasoning" token is seen. I hit a bug where no output was kept at all when I used reasoni...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: troduce some new semantics to drop the reasoning from a chat completions request. @juliendenize I'd love to have your thoughts about this one. 🤗 Cheers! PS: I'm not very familiar with vLLM codebase and my understanding...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: d and reasoning_effort == "none" %} {{- ' \n\n \n\n' }} {%- else %} {{- ' \n' }} {%- endif %} ``` By doing so, the "end reasoning" token is never seen by the code looking for it at generation time, and thus, no token is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
