# vllm-project/vllm#13629: [Bug]: Errors Encountered While Running Qwen2.5-VL-72B Inference on 4xA800 GPUs with VLLM V1 (Works Fine with VLLM V0)

| 字段 | 值 |
| --- | --- |
| Issue | [#13629](https://github.com/vllm-project/vllm/issues/13629) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Errors Encountered While Running Qwen2.5-VL-72B Inference on 4xA800 GPUs with VLLM V1 (Works Fine with VLLM V0)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run inference on Qwen2.5-VL-72B for video processing using 4xA800 GPUs. However, I encountered errors when executing the code with VLLM V1, whereas it works correctly with VLLM V0 by setting VLLM_USE_V1=0. ```python llm = LLM( model=MODEL_PATH, limit_mm_per_prompt={"image": 10, "video": 10}, tensor_parallel_size=4, gpu_memory_utilization=0.7 ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.05, max_tokens=256, stop_token_ids=[], ) question = '' messages = [ {"role": "system", "content": "You are a good video analyst"}, { "role": "user", "content": [ { "type": "video", "video": file, }, {"type": "text", "text": question}, ], } ] prompt = self.processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True) mm_data = {} if image_inputs is not None: mm_data["image"] = image_inputs if video_inputs is not None: mm_data["video"] = video_inputs llm_inputs = { "prompt": prompt, "multi_modal_data": mm_data, # FPS will be returned in video_kwargs #"mm_processor_kwargs":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Errors Encountered While Running Qwen2.5-VL-72B Inference on 4xA800 GPUs with VLLM V1 (Works Fine with VLLM V0) bug ### Your current environment ### 🐛 Describe the bug I am trying to run inference on Qwen2.5-VL-7...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;crash;slowdo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;crash;slowdown env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rompt = self.processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True) mm_data = {} if imag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
