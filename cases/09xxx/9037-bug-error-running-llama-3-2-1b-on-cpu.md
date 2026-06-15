# vllm-project/vllm#9037: [Bug]: Error Running Llama 3.2 1B on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#9037](https://github.com/vllm-project/vllm/issues/9037) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error Running Llama 3.2 1B on CPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Installed vllm for CPU as mentioned in https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html# Error when running Llama-3.2-1B on CPU. Command: ``` vllm serve meta-llama/Llama-3.2-1B-Instruct --port 8080 --api-key qwerty123 --max-model-len=30000 ``` Error: ``` INFO 10-03 07:38:10 logger.py:36] Received request chat-3361fcfb910c48b08a00e19e7f79c6e0: prompt: ' system \n\nCutting Knowledge Date: December 2023\nToday Date: 03 Oct 2024\n\n user \n\nExplain the significance of AI in modern technology. assistant \n\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=0.9, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), guided_decoding=GuidedDecodingParams(json=None, regex=None, choice=None, grammar=None, json_object=None, b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: onment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Installed vllm for CPU as mentioned in https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html# Error when running Llama-3.2-1B on CPU. Comm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rams(json=None, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None), prompt_token_ids: [128000, 128006, 9125, 128007, 271, 38766, 1303, 33025, 2696, 25, 6790, 220, 2366, 18, 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , temperature=0.7, top_p=0.9, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Error Running Llama 3.2 1B on CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Installed vllm for CPU as mentioned in https://docs.vllm.ai/en/latest/getting_st...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Error Running Llama 3.2 1B on CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Installed vllm for CPU as mentioned in https://docs.vllm.ai/en/latest/getting_st...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
