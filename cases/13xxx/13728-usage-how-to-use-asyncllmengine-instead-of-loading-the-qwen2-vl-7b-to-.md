# vllm-project/vllm#13728: [Usage]: How to use "AsyncLLMEngine" instead of loading the "qwen2-vl-7b" to handle multiple (concurrent) request on single instance.

| 字段 | 值 |
| --- | --- |
| Issue | [#13728](https://github.com/vllm-project/vllm/issues/13728) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;multimodal_vlm |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use "AsyncLLMEngine" instead of loading the "qwen2-vl-7b" to handle multiple (concurrent) request on single instance.

### Issue 正文摘录

### Your current environment This is the code for qwen2 vl image and text inference for extracting data from the image. from vllm import LLM, SamplingParams from transformers import AutoProcessor, AutoTokenizer Model load: self.krypton_vlm_model = LLM( mm_processor_kwargs=self.mm_processor_kwargs, model=self.krypton_model_path, tensor_parallel_size=self.tensor_parallel_size, gpu_memory_utilization=self.gpu_memory_utilization, enforce_eager=self.enforce_eager, rope_scaling=self.rope_scaling, max_seq_len_to_capture=self.max_token, max_model_len=self.max_token ) self.auto_processor = AutoProcessor.from_pretrained(self.krypton_model_path) Inference: def inference_by_krypton(input_file_path, user_prompt, system_prompt, vision_model, vision_processor, input_params, sampling_params, model_sampling_params): llm_inputs, prompt, image_inputs = None, None, None try: logger.info(f"Processing X-Q-VLM... for the requested inputs {input_params}") messages = [ {"role": "system", "content": str(system_prompt)}, { "role": "user", "content": [ { "type": str(model_sampling_params['modality']), "image": str(input_file_path), "min_pixels": model_sampling_params['minPixels'], "max_pixels": model_samplin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: image and text inference for extracting data from the image. from vllm import LLM, SamplingParams from transformers import AutoProcessor, AutoTokenizer Model load: self.krypton_vlm_model = LLM( mm_processor_kwargs=self....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: How to use "AsyncLLMEngine" instead of loading the "qwen2-vl-7b" to handle multiple (concurrent) request on single instance. usage ### Your current environment This is the code for qwen2 vl image and text infer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: code handle only single request per instance. Even this deploy as NVIDIA Triton server based using python backend ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: }: {e}") raise e finally: gc.collect() torch.cuda.empty_cache() if image_inputs is not None: del image_inputs if llm_inputs is not None: del llm_inputs if prompt is not None: del prompt How can I use sync
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cessor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) logger.info(f"Prepared for prompt template X-Q-VLM... for the requested inputs {input_params}") logger.info( f"The Krypton X-Q-VLM model

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
