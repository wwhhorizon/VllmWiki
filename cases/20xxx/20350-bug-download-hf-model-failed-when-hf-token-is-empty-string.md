# vllm-project/vllm#20350: [Bug]: download HF model failed when HF_TOKEN is empty string

| 字段 | 值 |
| --- | --- |
| Issue | [#20350](https://github.com/vllm-project/vllm/issues/20350) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: download HF model failed when HF_TOKEN is empty string

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` ERROR 07-01 23:05:48 [config.py:103] Error retrieving file list: 401 Client Error: Unauthorized for url: https://huggingface.co/api/models/Qwen/Qwen2.5-1.5B-Instruct/tree/main?recursive=True&expand=False ``` https://github.com/huggingface/huggingface_hub/blob/99baddf1df46c073166b50962dfaeee4c1e28847/src/huggingface_hub/utils/_auth.py#L207 `huggingface_hub` will clean the empty string token when get from other source, should we keep doing the same thing ? Currently we only get it from the environment variable but do not handle the empty string scenario. https://github.com/vllm-project/vllm/blob/27b8017636c57f9d0cd182fb4287b798c4a7ef28/vllm/transformers_utils/config.py#L198 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: download HF model failed when HF_TOKEN is empty string bug ### Your current environment ### 🐛 Describe the bug ``` ERROR 07-01 23:05:48 [config.py:103] Error retrieving file list: 401 Client Error: Unauthorized f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 198 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: /api/models/Qwen/Qwen2.5-1.5B-Instruct/tree/main?recursive=True&expand=False ``` https://github.com/huggingface/huggingface_hub/blob/99baddf1df46c073166b50962dfaeee4c1e28847/src/huggingface_hub/utils/_auth.py#L207 `hugg...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
