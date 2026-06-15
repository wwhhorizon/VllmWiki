# vllm-project/vllm#29266: [Bug]: A misc leads layers cannot be printed.

| 字段 | 值 |
| --- | --- |
| Issue | [#29266](https://github.com/vllm-project/vllm/issues/29266) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: A misc leads layers cannot be printed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug According to torch, nn.Module's `register_parameter` would drop the `param` if it's None, in other words, it won't be in state_dict of the obj. https://github.com/vllm-project/vllm/blob/6fb0215eee44cf5e4b28f57e6739ef4a51945127/vllm/model_executor/layers/linear.py#L577-L583 While printing it, self.bias is dropped. https://github.com/vllm-project/vllm/blob/6fb0215eee44cf5e4b28f57e6739ef4a51945127/vllm/model_executor/layers/linear.py#L497-L509 `self.bias = None` is enough. I believe not all such usages are meant to set it as `None`; sometimes the intention might be to drop it. I estimate that I need to review each instance of the call one by one to decide whether to make changes. I can help troubleshoot these calls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: estimate that I need to review each instance of the call one by one to decide whether to make changes. I can help troubleshoot these calls. ### Before submitting a new issue... - [x] Make sure you already searched for r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/6fb0215eee44cf5e4b28f57e6739ef4a51945127/vllm/model_executor/layers/linear.py#L577-L583 While printing it, self.bias is dropped. https://github.com/vllm-project/vllm/blob/6fb0215eee44cf5e4b28f...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
