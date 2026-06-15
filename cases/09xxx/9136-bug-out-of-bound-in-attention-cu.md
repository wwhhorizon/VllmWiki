# vllm-project/vllm#9136: [Bug]: out-of-bound in attention.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#9136](https://github.com/vllm-project/vllm/issues/9136) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | attention |
| 症状 | nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: out-of-bound in attention.cu

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/csrc/rocm/attention.cu#L199-L225 https://github.com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/csrc/rocm/attention.cu#L264 https://github.com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/csrc/rocm/attention.cu#L352-L359 https://github.com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/csrc/rocm/attention.cu#L914-L917 https://github.com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/csrc/rocm/attention.cu#L960-L973 So, for `alibi_slopes[wg_start_head_idx + qhead_idx]` in line 358: - `wg_start_head_idx = blockIdx.z * GQA_RATIO` - `blockIdx.z = num_kv_heads` - `GQA_RATIO = num_heads / num_kv_heads` Thus, `wg_start_head_idx = num_heads`. It appears that `alibi_slopes[wg_start_head_idx + qhead_idx]` may result in an overflow, as the size of `alibi_slopes` is only `num_heads`, and the computed index exceeds this limit. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at th...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/csrc/rocm/attention.cu#L199-L225 https://github.com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/csrc/rocm/attention.cu#L264 https:/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: attention_kv_cache;hardware_porting;model_support attention nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: opes[wg_start_head_idx + qhead_idx]` in line 358: - `wg_start_head_idx = blockIdx.z * GQA_RATIO` - `blockIdx.z = num_kv_heads` - `GQA_RATIO = num_heads / num_kv_heads` Thus, `wg_start_head_idx = num_heads`. It appears t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -of-bound in attention.cu bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/csrc/rocm/at...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: out-of-bound in attention.cu bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/c0d9a98d0c7182b73c2e7f88508e690a186bf0e3/cs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
