# vllm-project/vllm#20122: [Bug]:  Error in inspecting model architecture 'Qwen3ForCausalLM'

| 字段 | 值 |
| --- | --- |
| Issue | [#20122](https://github.com/vllm-project/vllm/issues/20122) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Error in inspecting model architecture 'Qwen3ForCausalLM'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The example usage from official site ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` > [INFO|image_processing_auto.py:315] 2025-06-26 17:40:50,424 >> Could not locate the image processor configuration file, will try to use the model config instead. ERROR 06-26 17:40:54 [registry.py:367] Error in inspecting model architecture 'Qwen3ForCausalLM' ERROR 06-26 17:40:54 [registry.py:367] Traceback (most recent call last): ERROR 06-26 17:40:54 [registry.py:367] File "/home/jitianbo/miniconda3/envs/llamafactory/lib/python3.10/site-packages/vllm/model_executor/models/registry.py", line 365, in _try_inspect_model_cls ERROR 06-26 17:40:54 [registry.py:367] return model.inspect_model_cls() ERROR 06-26 17:4...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Error in inspecting model architecture 'Qwen3ForCausalLM' bug;stale ### Your current environment ### 🐛 Describe the bug The example usage from official site ``` from vllm import LLM, SamplingParams prompts = [ "H...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rrent environment ### 🐛 Describe the bug The example usage from official site ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Error in inspecting model architecture 'Qwen3ForCausalLM' bug;stale ### Your current environment ### 🐛 Describe the bug The example usage from official site ``` from vllm import LLM, SamplingParams prompts = [ "H...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Error in inspecting model architecture 'Qwen3ForCausalLM' bug;stale ### Your current environment ### 🐛 Describe the bug The example usage from official site ``` from vllm import LLM, SamplingParams prompts = [ "H...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;multimodal_vlm;sampling_logits;speculative_decoding cuda;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
