# vllm-project/vllm#27642: [Bug]: SamplingParams.truncate_prompt_tokens has no effect in LLM.chat

| 字段 | 值 |
| --- | --- |
| Issue | [#27642](https://github.com/vllm-project/vllm/issues/27642) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SamplingParams.truncate_prompt_tokens has no effect in LLM.chat

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Setting `SamplingParams.truncate_prompt_tokens` has no effect in `LLM.chat`. According to the output, the prompt is not truncated to a specified length. Particularly, passing a longer prompt than `max_model_len` results in an error even if `(truncate_prompt_tokens + max_tokens)` is set to be smaller than `max_model_len`. While this behavior is mentioned in other issues (https://github.com/vllm-project/vllm/issues/17324, https://github.com/vllm-project/vllm/pull/3144#issuecomment-2044121238), it seems like it is not handled. I guess it is a bug as the docstring of `truncate_prompt_tokens` (https://docs.vllm.ai/en/latest/api/vllm/index.html#vllm.SamplingParams.truncate_prompt_tokens) does not mention such a limitation and it is natural to expect it to work in LLM.chat as well. ### case 1: `max_model_len` is large enough `RequestOutput.prompt_token_ids` seems not truncated to 10. ```python import vllm model = vllm.LLM(model="Qwen/Qwen3-0.6B", max_model_len=1000) ret = model.chat([{"role": "user", "content": " " * 200}], vllm.SamplingParams( truncate_prompt_tokens=10, max_tokens=10, )) print(ret[0]) ``` ``` INFO 10-28 16:13:52 [__ini...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: `LLM.chat`. According to the output, the prompt is not truncated to a specified length. Particularly, passing a longer prompt than `max_model_len` results in an error even if `(truncate_prompt_tokens + max_tokens)` is s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ug]: SamplingParams.truncate_prompt_tokens has no effect in LLM.chat bug;stale ### Your current environment ### 🐛 Describe the bug Setting `SamplingParams.truncate_prompt_tokens` has no effect in `LLM.chat`. According t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 8 16:14:05 [model.py:547] Resolved architecture: Qwen3ForCausalLM `torch_dtype` is deprecated! Use `dtype` instead! INFO 10-28 16:14:05 [model.py:1510] Using max model len 1000 INFO 10-28 16:14:07 [scheduler.py:205] Chu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: d to a specified length. Particularly, passing a longer prompt than `max_model_len` results in an error even if `(truncate_prompt_tokens + max_tokens)` is set to be smaller than `max_model_len`. While this behavior is m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
