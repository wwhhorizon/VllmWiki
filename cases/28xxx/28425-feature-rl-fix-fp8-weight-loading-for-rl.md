# vllm-project/vllm#28425: [Feature][RL]: Fix Fp8 Weight Loading for RL

| 字段 | 值 |
| --- | --- |
| Issue | [#28425](https://github.com/vllm-project/vllm/issues/28425) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][RL]: Fix Fp8 Weight Loading for RL

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Feedback from RL community that vLLM weight loading in fp8 is bad for RL - https://vllm-dev.slack.com/archives/C07UUL8E61Z/p1762811441757529 The cause is clear: in [fp8.py](https://github.com/vllm-project/vllm/blob/bf6a3d0ff5a69e0a30567f2ad417530c002eaa4e/vllm/model_executor/layers/quantization/fp8.py#L490) in process_weights_after_loading there is a lot of parameter wrapping that drops .weight_loader attribute. There's a patch from the Moonshot team that fixes this issue and there's a [PR](https://github.com/vllm-project/vllm/pull/24488) with this patch that never got any comments. The [patch](https://github.com/MoonshotAI/checkpoint-engine/blob/main/patches/vllm_fp8.patch) only works on top of v0.10.2rc1. Shortly after that tag, this [PR](https://github.com/vllm-project/vllm/pull/23280) made fp8 weight updates even trickier by transposing weight_inv_scale parameter for CUTLASS. I don't know how to patch any vLLM version after this PR to be able to call model.load_weights after the engine has started. It is a bummer, because DeepSeek wide EP inference is quite a bit faster in v0.11.0. We need to fix this ASAP ### Alternatives _No response_...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature][RL]: Fix Fp8 Weight Loading for RL feature request;stale ### 🚀 The feature, motivation and pitch Feedback from RL community that vLLM weight loading in fp8 is bad for RL - https://vllm-dev.slack.com/archives/C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][RL]: Fix Fp8 Weight Loading for RL feature request;stale ### 🚀 The feature, motivation and pitch Feedback from RL community that vLLM weight loading in fp8 is bad for RL - https://vllm-dev.slack.com/archives/C...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ght updates even trickier by transposing weight_inv_scale parameter for CUTLASS. I don't know how to patch any vLLM version after this PR to be able to call model.load_weights after the engine has started. It is a bumme...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t_inv_scale parameter for CUTLASS. I don't know how to patch any vLLM version after this PR to be able to call model.load_weights after the engine has started. It is a bummer, because DeepSeek wide EP inference is quite...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at vLLM weight loading in fp8 is bad for RL - https://vllm-dev.slack.com/archives/C07UUL8E61Z/p1762811441757529 The cause is clear: in [fp8.py](https://github.com/vllm-project/vllm/blob/bf6a3d0ff5a69e0a30567f2ad417530c0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
