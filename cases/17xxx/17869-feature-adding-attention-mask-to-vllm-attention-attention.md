# vllm-project/vllm#17869: [Feature]: Adding attention mask to vllm.attention.Attention

| 字段 | 值 |
| --- | --- |
| Issue | [#17869](https://github.com/vllm-project/vllm/issues/17869) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Adding attention mask to vllm.attention.Attention

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Right now, `vllm.attention.Attention` implements the standard self-attention operation: ```math \text{Attention}(Q, K, V) = \text{softmax}\left( \frac{QK^\top}{\sqrt{d_k}} \right) V ``` However, it is very common among models to include an attention mask $$M$$: ```math \text{Attention}(Q, K, V, M) = \text{softmax}\left( \frac{QK^\top + M}{\sqrt{d_k}} \right) V ``` Like the `attn_mask` parameter of [`torch.nn.functional.scaled_dot_product_attention`](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html). I am working on adding a new model, but found the lack of attention mask to be the biggest blocker. Are there any work-arounds at this moment? If not, what is the best way to add attention mask to vLLM? Any comments are appreciated! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Adding attention mask to vllm.attention.Attention feature request;stale ### 🚀 The feature, motivation and pitch Right now, `vllm.attention.Attention` implements the standard self-attention operation: ```math...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hat is the best way to add attention mask to vLLM? Any comments are appreciated! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: } \right) V ``` Like the `attn_mask` parameter of [`torch.nn.functional.scaled_dot_product_attention`](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html). I am working...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ding a new model, but found the lack of attention mask to be the biggest blocker. Are there any work-arounds at this moment? If not, what is the best way to add attention mask to vLLM? Any comments are appreciated! ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
