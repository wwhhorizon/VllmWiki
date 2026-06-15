# vllm-project/vllm#14160: [Feature]: Support multi step drafting for DeepSeek MTP when k > n_predict

| 字段 | 值 |
| --- | --- |
| Issue | [#14160](https://github.com/vllm-project/vllm/issues/14160) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support multi step drafting for DeepSeek MTP when k > n_predict

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On top of #13626, it will be nice to support multi step drafting to improve drafting performance using existing TP1DraftModelRunner. Based on the [discussion](https://github.com/vllm-project/vllm/pull/13626#discussion_r1973891477), the main concern is compatibility of MLA backend and multi step runner's advance_step. I plan to add the support and verify the compatibility with - correctness test - quality eval cc @benchislett @luccafong @LiuXiaoxuanPKU let me know if you have any suggestions ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support multi step drafting for DeepSeek MTP when k > n_predict feature request;stale ### 🚀 The feature, motivation and pitch On top of #13626, it will be nice to support multi step drafting to improve drafti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: plan to add the support and verify the compatibility with - correctness test - quality eval cc @benchislett @luccafong @LiuXiaoxuanPKU let me know if you have any suggestions ### Alternatives _No response_ ### Additiona...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /13626#discussion_r1973891477), the main concern is compatibility of MLA backend and multi step runner's advance_step. I plan to add the support and verify the compatibility with - correctness test - quality eval cc @be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lti step drafting to improve drafting performance using existing TP1DraftModelRunner. Based on the [discussion](https://github.com/vllm-project/vllm/pull/13626#discussion_r1973891477), the main concern is compatibility...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
