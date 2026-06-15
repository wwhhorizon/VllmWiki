# vllm-project/vllm#19877: [Feature]: Support passing token-level schedules for temperature and other sampling parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#19877](https://github.com/vllm-project/vllm/issues/19877) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support passing token-level schedules for temperature and other sampling parameters

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It is extremely important for research in RL/GRPO to be able to research the effect of temperature and sampling in the model's ability to discover new information. There are many arguments in favor of it but fundamentally, spiking the temperature every random amount of token between let's say 128 and 256 could drastically improve the effect of RL, because the model would be forced to explore much more newer paths. But if we simply increase the temperature, we cannot explore both hot and cool distributions. The model should warm the distribution and be given some time to cool down or anneal. There are a number of possible research projects that can build on this, all very blue-sky in nature but I believe crucial nonetheless. For example the temperature can be made audio-reactive, tied to the loudness of awesome jazz music playing in memory and ticked forward for each token. We can certainly DIY this up in pytorch and try it out, but the true demonstration for any given technique is its amplification in reinforcement learning at scale, so we definitely want vLLM to have strong control features. I understand if there are optimization techniques...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e request;stale ### 🚀 The feature, motivation and pitch It is extremely important for research in RL/GRPO to be able to research the effect of temperature and sampling in the model's ability to discover new information....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: RPO to be able to research the effect of temperature and sampling in the model's ability to discover new information. There are many arguments in favor of it but fundamentally, spiking the temperature every random amoun...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en-level schedules for temperature and other sampling parameters feature request;stale ### 🚀 The feature, motivation and pitch It is extremely important for research in RL/GRPO to be able to research the effect of tempe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: or any given technique is its amplification in reinforcement learning at scale, so we definitely want vLLM to have strong control features. I understand if there are optimization techniques that need to be turned off to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: # 🚀 The feature, motivation and pitch It is extremely important for research in RL/GRPO to be able to research the effect of temperature and sampling in the model's ability to discover new information. There are many ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
