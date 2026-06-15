# vllm-project/vllm#13346: For individual inference return expected result and batched inference returns different results for same prompts - Qwen2-VL-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#13346](https://github.com/vllm-project/vllm/issues/13346) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> For individual inference return expected result and batched inference returns different results for same prompts - Qwen2-VL-7B

### Issue 正文摘录

### Your current environment message = {{"role": "system", "content": system_prompt}, { "role": "user", "content": [ {"type": "image", "image": image_path, "min_pixels": mm_processor_kwargs['min_pixels'], "max_pixels": mm_processor_kwargs['max_pixels'] }, {"type": "text", "text": user_prompt} ] }} messages.append(message) messages_batch = prepare_messages(uploaded_files, user_prompt_list, system_prompt_list) # Start timing start_time = time.time() # Prepare batch inputs llm_inputs_batch = [] for messages in messages_batch: prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) image_inputs, _ = process_vision_info(messages) mm_data = {"image": image_inputs} if image_inputs else {} llm_inputs_batch.append({"prompt": prompt, "multi_modal_data": mm_data}) # Perform batch inference outputs = llm.generate(llm_inputs_batch, sampling_params=sampling_params) ### 🐛 Describe the bug def load_qwen2_vl_model(): llm = LLM( mm_processor_kwargs=mm_processor_kwargs, model=MODEL_PATH, trust_remote_code=True, gpu_memory_utilization=0.6, max_model_len=8192, tensor_parallel_size=2 ) processor = AutoProcessor.from_pretrained(MODEL_PATH) return llm, processor ### B...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: esult and batched inference returns different results for same prompts - Qwen2-VL-7B bug;stale ### Your current environment message = {{"role": "system", "content": system_prompt}, { "role": "user", "con
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sor ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s_batch: prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) image_inputs, _ = process_vision_info(messages) mm_data = {"image": image_inputs} if image_inputs else {} llm_inputs_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d inference returns different results for same prompts - Qwen2-VL-7B bug;stale ### Your current environment message = {{"role": "system", "content": system_prompt}, { "role": "user", "content": [
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
