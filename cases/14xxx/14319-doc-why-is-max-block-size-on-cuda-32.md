# vllm-project/vllm#14319: [Doc]: Why is max block_size on CUDA 32?

| 字段 | 值 |
| --- | --- |
| Issue | [#14319](https://github.com/vllm-project/vllm/issues/14319) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Why is max block_size on CUDA 32?

### Issue 正文摘录

### 📚 The doc issue In the args: https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py#L454 it says about block_size parameter: > Token block size for contiguous chunks of tokens. This is ignored on neuron devices and set to --max-model-len. On CUDA devices, only block sizes up to 32 are supported. On HPU devices, block size defaults to 128. 1. Where is this requirement for <= 32 on CUDA devices coming from? 2. I was able to successfully run vLLM with block_size 128 on Hopper and see some minor performance improvement. Is the requirement up to date? 3. In flash attention docs I see that paged attention minimum block size is actually 256: https://github.com/Dao-AILab/flash-attention/blob/d82bbf26924c492064af8b27ab299ff4808d1bf6/hopper/flash_attn_interface.py#L662 Does vLLM use this interface? How does FA paged_block_size relates to vLLM block_size? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Doc]: Why is max block_size on CUDA 32? documentation;stale ### 📚 The doc issue In the args: https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py#L454 it says about block_size parameter: > Token bloc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Doc]: Why is max block_size on CUDA 32? documentation;stale ### 📚 The doc issue In the args: https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py#L454 it says about block_size parameter: > Token bloc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: some minor performance improvement. Is the requirement up to date? 3. In flash attention docs I see that paged attention minimum block size is actually 256: https://github.com/Dao-AILab/flash-attention/blob/d82bbf26924c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ous chunks of tokens. This is ignored on neuron devices and set to --max-model-len. On CUDA devices, only block sizes up to 32 are supported. On HPU devices, block size defaults to 128. 1. Where is this requirement for...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Why is max block_size on CUDA 32? documentation;stale ### 📚 The doc issue In the args: https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py#L454 it says about block_size parameter: > Token bloc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
