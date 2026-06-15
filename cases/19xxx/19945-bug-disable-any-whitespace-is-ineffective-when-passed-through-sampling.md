# vllm-project/vllm#19945: [Bug]: disable_any_whitespace is ineffective when passed through SamplingParams' guided_decoding in the V1 engine.

| 字段 | 值 |
| --- | --- |
| Issue | [#19945](https://github.com/vllm-project/vllm/issues/19945) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: disable_any_whitespace is ineffective when passed through SamplingParams' guided_decoding in the V1 engine.

### Issue 正文摘录

### 🐛 Describe the bug ``` llm=LLM(**engine_args) results = llm.chat( messages_list, sampling_params, lora_request=lora_request, chat_template_kwargs={"enable_thinking": False } ) ``` 1. `disable_any_whitespace` seems to be accessible only from `vllm_config`, not from `SamplingParams`. https://github.com/vllm-project/vllm/blob/4c409cabc2c1c432ba670029990bd59e6bbf1479/vllm/v1/structured_output/backend_guidance.py#L63 2. Why is `validate_guidance_grammar` being executed for every input, even though the inputs all have the same `SamplingParams`, and `validate_guidance_grammar` seems to only be validating grammar? https://github.com/vllm-project/vllm/blob/2bb246b8f7b8dd220008ff7bd735249b362c799a/vllm/v1/engine/processor.py#L184 ### Your current environment

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lm/v1/engine/processor.py#L184 ### Your current environment development ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dep...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: hen passed through SamplingParams' guided_decoding in the V1 engine. bug;stale ### 🐛 Describe the bug ``` llm=LLM(**engine_args) results = llm.chat( messages_list, sampling_params, lora_request=lora_request, chat_templa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /blob/4c409cabc2c1c432ba670029990bd59e6bbf1479/vllm/v1/structured_output/backend_guidance.py#L63 2. Why is `validate_guidance_grammar` being executed for every input, even though the inputs all have the same `SamplingPa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ``` 1. `disable_any_whitespace` seems to be accessible only from `vllm_config`, not from `SamplingParams`. https://github.com/vllm-project/vllm/blob/4c409cabc2c1c432ba670029990bd59e6bbf1479/vllm/v1/structured_output/bac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency 🐛 Describe the bug

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
