# vllm-project/vllm#21438: [Bug]: vLLM Multinode Pipeline Error with pipeline parallelism using Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#21438](https://github.com/vllm-project/vllm/issues/21438) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM Multinode Pipeline Error with pipeline parallelism using Ray

### Issue 正文摘录

### 🐛 Describe the bug Hi! So I was trying to use vllm to serve a model in a multi-node setup, I'm basically using 2 PODS with 8 GPUs each. To do so I initialized a ray cluster following the recommendations in the documentation (https://docs.vllm.ai/en/latest/serving/distributed_serving.html#running-vllm-on-multiple-nodes) While the whole model setup worked fine, when I try to use the URL to perform inference through a request to the served model, the whole thing fails with the following error: ```bash INFO 07-23 07:15:34 [logger.py:43] Received request cmpl-9ab6810037a24c4e9c57e33827d212bf-0: prompt: 'Once upon a time,', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=50, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: [9297, 12683, 312, 1133, 30], prompt_embeds shape: None, lora_request: None, prompt_adapter_request: Non...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ax_tokens=50, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: [9297...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM Multinode Pipeline Error with pipeline parallelism using Ray bug;ray;stale ### 🐛 Describe the bug Hi! So I was trying to use vllm to serve a model in a multi-node setup, I'm basically using 2 PODS with 8 GPU...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=50, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: LLM Multinode Pipeline Error with pipeline parallelism using Ray bug;ray;stale ### 🐛 Describe the bug Hi! So I was trying to use vllm to serve a model in a multi-node setup, I'm basically using 2 PODS with 8 GPUs each....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: stale ### 🐛 Describe the bug Hi! So I was trying to use vllm to serve a model in a multi-node setup, I'm basically using 2 PODS with 8 GPUs each. To do so I initialized a ray cluster following the recommendations in the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
