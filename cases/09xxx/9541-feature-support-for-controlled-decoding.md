# vllm-project/vllm#9541: [Feature]: Support for Controlled Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#9541](https://github.com/vllm-project/vllm/issues/9541) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Controlled Decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Contrastive Decoding (Li et al., 2022) is a decoding strategy that contrasts the log probabilities of two or more models at each token to shift the token distribution for better performance or less harmful outputs (Liu et al., 2021). Similar works are seen in Proxy-tuning (Liu et al., 2024), Emulator on aligned models (Mitchell et al., 2023), improving reasoning tasks (O'Brien et al., 2023) and Test-time alignment (Zhu et al., 2024). This approach also facilitates the recent interest in test-time alignment (Xu et al., 2024), where a token-level reward model is used to generate partial rewards at each token decoding stage to assist generation. ### welcome for any contribution! I am currently working on the implementation, and any contributions would be highly appreciated. The initial idea is similar to the speculative decoding method under `spec_decode/`, where two or more models are loaded into the GPU and perform inference at each timestep. More details will be shared soon! ### Reference - Contrastive Decoding: Open-ended Text Generation as Optimization - DExperts: Decoding-Time Controlled Text Generation with Experts and Anti-Experts - Tun...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Support for Controlled Decoding feature request;stale ### 🚀 The feature, motivation and pitch Contrastive Decoding (Li et al., 2022) is a decoding strategy that contrasts the log probabilities of two or more...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: odels by Proxy - An Emulator for Fine-Tuning Large Language Models using Small Language Models - GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-time Alignment - Contrastive Decoding Improves...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , 2023) and Test-time alignment (Zhu et al., 2024). This approach also facilitates the recent interest in test-time alignment (Xu et al., 2024), where a token-level reward model is used to generate partial rewards at ea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a decoding strategy that contrasts the log probabilities of two or more models at each token to shift the token distribution for better performance or less harmful outputs (Liu et al., 2021). Similar works are seen in P...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ce - Contrastive Decoding: Open-ended Text Generation as Optimization - DExperts: Decoding-Time Controlled Text Generation with Experts and Anti-Experts - Tuning Language Models by Proxy - An Emulator for Fine-Tuning La...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
