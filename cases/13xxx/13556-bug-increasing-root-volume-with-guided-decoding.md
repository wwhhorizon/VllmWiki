# vllm-project/vllm#13556: [Bug]: Increasing root volume with guided decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#13556](https://github.com/vllm-project/vllm/issues/13556) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Increasing root volume with guided decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug llm = LLM(model=model_id, quantization="bitsandbytes", load_format="bitsandbytes", # dtype='auto', max_lora_rank=32, max_model_len = 5192+64, gpu_memory_utilization=0.65, tensor_parallel_size=4, enforce_eager=True) for prompt, label, inv_list in tqdm(list(zip(prompts,true_label, inv_lists))): inv_list = inv_list + ['None'] guided_decoding_params = GuidedDecodingParams(choice=inv_list) params = SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1, max_tokens=64, stop=[tokenizer.eos_token, ' ', '### Instruction', '###']) params.guided_decoding = guided_decoding_params output = llm.generate(prompt, params) prompt = output[0].prompt generated_text = output[0].outputs[0].text.strip() print(f"Prompt: {prompt!r}, \n true text: {label!r}") print(f"investor list: {inv_list}") print(f"Generated text: {generated_text!r}") preds.append(generated_text) del guided_decoding_params del params It is increasing the root volume and causing out of disk space. Please suggest. cache is getting stored inside root/.cache/outlines/ cache.db cache.db-shm cache.db-wal ### Before submitting a new issue... - [x] Make sure you already searched for re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: nvironment ### 🐛 Describe the bug llm = LLM(model=model_id, quantization="bitsandbytes", load_format="bitsandbytes", # dtype='auto', max_lora_rank=32, max_model_len = 5192+64, gpu_memory_utilization=0.65, tensor_paralle...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: wal ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: stale ### Your current environment ### 🐛 Describe the bug llm = LLM(model=model_id, quantization="bitsandbytes", load_format="bitsandbytes", # dtype='auto', max_lora_rank=32, max_model_len = 5192+64, gpu_memory_utilizat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Increasing root volume with guided decoding bug;stale ### Your current environment ### 🐛 Describe the bug llm = LLM(model=model_id, quantization="bitsandbytes", load_format="bitsandbytes", # dtype='auto', max_lor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
