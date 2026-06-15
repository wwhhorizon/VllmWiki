# vllm-project/vllm#15094: [Usage]: set `do_rescale=False` to avoid rescaling them again.

| 字段 | 值 |
| --- | --- |
| Issue | [#15094](https://github.com/vllm-project/vllm/issues/15094) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: set `do_rescale=False` to avoid rescaling them again.

### Issue 正文摘录

### Your current environment ### How would you like to use vllm I want to run inference of Qwen/Qwen2.5-VL-72B-Instruct-AWQ. I get the warning: set `do_rescale=False` to avoid rescaling them again. How to set do_rescale？ the code is ` MODEL_PATH = "Qwen/Qwen2.5-VL-72B-Instruct-AWQ" CUDA_VISIBLE_DEVICES = os.getenv("CUDA_VISIBLE_DEVICES", None) tensor_parallel_size = torch.cuda.device_count() if CUDA_VISIBLE_DEVICES is None else len(CUDA_VISIBLE_DEVICES.split(",")) print(f"Automatically set tensor_parallel_size={tensor_parallel_size} based on the available devices.") llm = LLM( model=MODEL_PATH, limit_mm_per_prompt={"image": 1, "video": 2}, tensor_parallel_size=tensor_parallel_size, dtype="float16", ) print('sampling params') sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.05, max_tokens=512, stop_token_ids=[], ) # For video input, you can pass following values instead: # "type": "video", # "video": " ", video_messages = [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": [ {"type": "text", "text": "Describe this video."}, { "type": "video", "video": "UID245880831873709_2023-02-12-18.08.52_shot_001_000.mp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: sages processor = AutoProcessor.from_pretrained(MODEL_PATH) import time t = time.time() prompt = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) image_inputs, video_inputs, video_k...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: set `do_rescale=False` to avoid rescaling them again. usage ### Your current environment ### How would you like to use vllm I want to run inference of Qwen/Qwen2.5-VL-72B-Instruct-AWQ. I get the warning: set `d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ale？ the code is ` MODEL_PATH = "Qwen/Qwen2.5-VL-72B-Instruct-AWQ" CUDA_VISIBLE_DEVICES = os.getenv("CUDA_VISIBLE_DEVICES", None) tensor_parallel_size = torch.cuda.device_count() if CUDA_VISIBLE_DEVICES is None else len...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ment ### How would you like to use vllm I want to run inference of Qwen/Qwen2.5-VL-72B-Instruct-AWQ. I get the warning: set `do_rescale=False` to avoid rescaling them again. How to set do_rescale？ the code is ` MODEL_PA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
