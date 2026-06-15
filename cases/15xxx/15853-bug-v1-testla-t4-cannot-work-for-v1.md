# vllm-project/vllm#15853: [Bug]: [V1] Testla T4 cannot work for V1

| 字段 | 值 |
| --- | --- |
| Issue | [#15853](https://github.com/vllm-project/vllm/issues/15853) |
| 状态 | closed |
| 标签 | usage;unstale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1] Testla T4 cannot work for V1

### Issue 正文摘录

### Your current environment Testla T4 run vllm v1 ### 🐛 Describe the bug ERROR 03-20 07:42:38 [utils.py:613] Cannot use FA version 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 and Blackwell archs (>=10) INFO 03-20 07:42:38 [topk_topp_sampler.py:36] Using FlashInfer for top-p & top-k sampling. INFO 03-20 07:42:39 [weight_utils.py:257] Using model weights format ['*.bin'] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 and Blackwell archs (>=10) INFO 03-20 07:42:38 [topk_topp_sampler.py:36] Using FlashInfer for top-p & top-k s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 07:42:38 [utils.py:613] Cannot use FA version 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 and Blackwell archs (>=10) INFO 03-20 07:42:38 [topk_topp_sampl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: top-p & top-k sampling. INFO 03-20 07:42:39 [weight_utils.py:257] Using model weights format ['*.bin'] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 8 excluding 8.6 and 8.9 and Blackwell archs (>=10) INFO 03-20 07:42:38 [topk_topp_sampler.py:36] Using FlashInfer for top-p & top-k sampling. INFO 03-20 07:42:39 [weight_utils.py:257] Using model weights format ['*.bin'...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ## 🐛 Describe the bug ERROR 03-20 07:42:38 [utils.py:613] Cannot use FA version 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 and Blackwell archs (>=10) IN...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
