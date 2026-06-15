# vllm-project/vllm#7866: [Bug]: enable_prefix_caching error

| 字段 | 值 |
| --- | --- |
| Issue | [#7866](https://github.com/vllm-project/vllm/issues/7866) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: enable_prefix_caching error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use enable_prefix_machining=True, I encounter the following error when inferring 7 images(And the result of the previous inference is also incorrect)： ``` [rank0]: File "/home/hadoop-platcv/vllm/vllm/model_executor/models/minicpmv.py", line 563, in _get_image_bounds [rank0]: return torch.hstack([ [rank0]: RuntimeError: Sizes of tensors must match except in dimension 1. Expected size 8 but got size 9 for tensor number 1 in the list. Processed prompts: 0%| | 0/1 [00:00 ', ' '] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens] messages = [{ 'role': 'user', 'content': f'( ./ )\n{question}' }] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) return llm, prompt, stop_token_ids def profile_model_on_business_datasets(): data_dir = '/home/hadoop-platcv/minicpm-v-v2_6/images' res_dict = {} question = '请描述图片内容' llm, prompt, stop_token_ids = run_minicpmv(question) sampling_params = SamplingParams(temperature=1.0, max_tokens=16, stop_token_ids=stop_token_ids) total_tokens = 0 t1 = time.time() for img in os.listdir(data_dir): img_path = os.path.join(data_dir, img) imag...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits cuda;fp8;operator;quantizati...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: uted_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits cuda;fp8;operator;quantization;triton build_error;mismatch dtype;env_dependency;shape Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e is also incorrect)： ``` [rank0]: File "/home/hadoop-platcv/vllm/vllm/model_executor/models/minicpmv.py", line 563, in _get_image_bounds [rank0]: return torch.hstack([ [rank0]: RuntimeError: Sizes of tensors must match...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: add_generation_prompt=True) return llm, prompt, stop_token_ids def profile_model_on_business_datasets(): data_dir = '/home/hadoop-platcv/minicpm-v-v2_6/images' res_dict = {} question = '请描述图片内容' llm, prompt, stop_token_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
