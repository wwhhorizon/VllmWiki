# vllm-project/vllm#6424: [Feature]: Return softmax of attention layer.

| 字段 | 值 |
| --- | --- |
| Issue | [#6424](https://github.com/vllm-project/vllm/issues/6424) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Return softmax of attention layer.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Feature I'm working on returning the softmax of the LLM's attention layer. As far as I know, only transformers support this [feature](https://huggingface.co/docs/transformers/v4.42.0/en/internal/generation_utils#generate-outputs). But transforms is not efficient enough. I saw "return_softmax" [vllm_flash_attn](https://github.com/vllm-project/flash-attention/blob/main/vllm_flash_attn/flash_attn_interface.py#L62), but seems it can't be used. Would you be able to add this feature? # Motivation Softmax of attention is important evidence for humans to understand how LLM works. Humans can determine which input token is important for the inference of the output token. And more features can be developed based on this feature such as visualization of LLM evidence. # Pitch For this RFC in particular, we propose the following changes: - Add a new function llm.forward(). This function receives requests to do prefill and return softmax. - Modify prefill kernels to support output softmax. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n/internal/generation_utils#generate-outputs). But transforms is not efficient enough. I saw "return_softmax" [vllm_flash_attn](https://github.com/vllm-project/flash-attention/blob/main/vllm_flash_attn/flash_attn_interf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Return softmax of attention layer. feature request ### 🚀 The feature, motivation and pitch # Feature I'm working on returning the softmax of the LLM's attention layer. As far as I know, only transformers supp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ayer. As far as I know, only transformers support this [feature](https://huggingface.co/docs/transformers/v4.42.0/en/internal/generation_utils#generate-outputs). But transforms is not efficient enough. I saw "return_sof...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
