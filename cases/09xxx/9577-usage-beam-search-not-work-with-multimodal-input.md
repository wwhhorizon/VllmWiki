# vllm-project/vllm#9577: [Usage]: beam_search not work with multimodal input

| 字段 | 值 |
| --- | --- |
| Issue | [#9577](https://github.com/vllm-project/vllm/issues/9577) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: beam_search not work with multimodal input

### Issue 正文摘录

### How would you like to use vllm I'm trying to do batch inference with multimodal input data like this: ``` llm = LLM(model='OpenGVLab/InternVL2-1B', trust_remote_code=True, max_num_seqs=5, enforce_eager=True) sampling_params = SamplingParams(max_tokens=128, temperature=0.0) beam_params = BeamSearchParams(beam_width=3, max_tokens=128, temperature=0.0) for image_file in image_files: input = { "prompt": prompt, "multi_modal_data": { "image": Image.open(image_file)}, } list_input.append(input) outputs = llm.generate(list_input, sampling_params) outputs = llm.beam_search(list_input, beam_params) ``` The model run perfectly with generate() method but when I call beam_search() method I got this error: TypeError: TextEncodeInput must be Union[TextInputSequence, Tuple[InputSequence, InputSequence]] ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#9427 [Frontend] re-enable multi-modality input in the new beam search implementation

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: beam_search not work with multimodal input usage ### How would you like to use vllm I'm trying to do batch inference with multimodal input data like this: ``` llm = LLM(model='OpenGVLab/InternVL2-1B', trust_rem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;triton...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: beam_search not work with multimodal input usage ### How would you like to use vllm I'm trying to do batch inference with multimodal input data like this: ``` llm = LLM(model='OpenGVLab/InternVL2-1B', trust_rem...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency;shape #9427 [Frontend] re-enable multi-modality input in the new beam search implementation <details>
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency;shape #9427 [Frontend] re-enable multi-modality input in the new beam search...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9427](https://github.com/vllm-project/vllm/pull/9427) | closes_keyword | 0.95 | [Frontend] re-enable multi-modality input in the new beam search implementation | FIX #9577 **Changes in this PR:** This PR introduces the following changes based on the updated beam search implementation: * Re-enable multi-modality input: Support for |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
