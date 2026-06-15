# vllm-project/vllm#25919: [Feature]: Upstream some unsloth patches if possible

| 字段 | 值 |
| --- | --- |
| Issue | [#25919](https://github.com/vllm-project/vllm/issues/25919) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Upstream some unsloth patches if possible

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Unsloth adds vllm patches in https://github.com/unslothai/unsloth-zoo/blob/main/unsloth_zoo/vllm_utils.py - which looks extremely fragile wrt vllm updates Here are some things in there (mostly related to 4-bit / lora quite pertinent in the light of https://thinkingmachines.ai/blog/lora/, but also standby mode - quite useful): ``` patch_vllm_enable_sleep_mode() patch_vllm_graph_capture() patch_vllm_set_inductor_config() patch_bitsandbytes_quant_state() patch_vllm_bitsandbytes() patch_vllm_lora_tokenizer() patch_vllm_lora_load_tensors() ``` It is licensed under LGPLv3. Is it compatible with vllm license? It would be great to either upstream some of these or provide nicer extension points ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Upstream some unsloth patches if possible feature request;stale ### 🚀 The feature, motivation and pitch Unsloth adds vllm patches in https://github.com/unslothai/unsloth-zoo/blob/main/unsloth_zoo/vllm_utils.p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: llm_graph_capture() patch_vllm_set_inductor_config() patch_bitsandbytes_quant_state() patch_vllm_bitsandbytes() patch_vllm_lora_tokenizer() patch_vllm_lora_load_tensors() ``` It is licensed under LGPLv3. Is it compatibl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Upstream some unsloth patches if possible feature request;stale ### 🚀 The feature, motivation and pitch Unsloth adds vllm patches in https://github.com/unslothai/unsloth-zoo/blob/main/unsloth_zoo/vllm_utils.p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _enable_sleep_mode() patch_vllm_graph_capture() patch_vllm_set_inductor_config() patch_bitsandbytes_quant_state() patch_vllm_bitsandbytes() patch_vllm_lora_tokenizer() patch_vllm_lora_load_tensors() ``` It is licensed u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
