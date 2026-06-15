# vllm-project/vllm#40421: [Feature]: [parity with CUDA] PD disagg recipes on vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#40421](https://github.com/vllm-project/vllm/issues/40421) |
| 状态 | open |
| 标签 | feature request;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [parity with CUDA] PD disagg recipes on vllm

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hi @hongxiayang currently CUDA vLLM has easy to understand PD disagg recipes for popular models. can u add this for ROCm vLLM too (blocker is acutally get ROCm vLLM disagg to work with vllm router https://github.com/vllm-project/vllm/issues/38687 https://github.com/vllm-project/vllm/issues/38692) https://recipes.vllm.ai/moonshotai/Kimi-K2.5?strategy=pd_cluster&variant=nvfp4 +viz @powderluv @chunfangamd @andyluo7 ## prefill command ## decode command ## router command https://recipes.vllm.ai/moonshotai/Kimi-K2.5?strategy=pd_cluster ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: [parity with CUDA] PD disagg recipes on vllm feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang currently CUDA vLLM has easy to understand PD disagg recipes for popular models. can u...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: [parity with CUDA] PD disagg recipes on vllm feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang currently CUDA vLLM has easy to understand PD disagg recipes for popular models. can u...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: https://recipes.vllm.ai/moonshotai/Kimi-K2.5?strategy=pd_cluster&variant=nvfp4 +viz @powderluv @chunfangamd @andyluo7 ## prefill command ## decode command ## router command https://recipes.vllm.ai/moonshotai/Kimi-K2.5?s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: [parity with CUDA] PD disagg recipes on vllm feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang currently CUDA vLLM has easy to understand PD disagg recipes for popular models. can u...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: PD disagg recipes for popular models. can u add this for ROCm vLLM too (blocker is acutally get ROCm vLLM disagg to work with vllm router https://github.com/vllm-project/vllm/issues/38687 https://github.com/vllm-project...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
