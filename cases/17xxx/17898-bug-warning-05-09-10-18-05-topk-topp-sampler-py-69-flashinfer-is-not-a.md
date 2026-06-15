# vllm-project/vllm#17898: [Bug]: WARNING 05-09 10:18:05 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer.

| 字段 | 值 |
| --- | --- |
| Issue | [#17898](https://github.com/vllm-project/vllm/issues/17898) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: WARNING 05-09 10:18:05 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I got WARNING 05-09 10:18:05 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer. I found ![Image](https://github.com/user-attachments/assets/68147557-10f6-4220-92ea-eee023508fe9) and ![Image](https://github.com/user-attachments/assets/67f5f55f-ca50-4a44-a053-a0d342496dca) so it requries torch <=2.6 ,but the latest vllm use 2.7 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: plementation of top-p & top-k sampling. For the best performance, please install FlashInfer. bug ### Your current environment ### 🐛 Describe the bug when I got WARNING 05-09 10:18:05 [topk_topp_sampler.py:69] FlashInfer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: WARNING 05-09 10:18:05 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer. bug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2.7 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: WARNING 05-09 10:18:05 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer. bug...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
