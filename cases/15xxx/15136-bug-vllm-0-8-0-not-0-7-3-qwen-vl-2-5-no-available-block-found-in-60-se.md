# vllm-project/vllm#15136: [Bug]: vllm 0.8.0 (not 0.7.3) Qwen VL 2.5 - `No available block found in 60 second.` for hours for a video of 300 frames (cpus 100%, gpu: 0%)

| 字段 | 值 |
| --- | --- |
| Issue | [#15136](https://github.com/vllm-project/vllm/issues/15136) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.8.0 (not 0.7.3) Qwen VL 2.5 - `No available block found in 60 second.` for hours for a video of 300 frames (cpus 100%, gpu: 0%)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm loads correctly, but it stucks at the `.generate` call, using the cpu significantly but not the gpu, which is used 0% (aside the memory allocated by vllm for the model + kv cache). I tested it with 300 frames of a video I here attach https://drive.google.com/file/d/1S48vGSnFROmit7hqZNa2_Wm41Z-Ps9FY/view?usp=sharing and it takes more than 2 hours (it has not finished yet though). I tried both decord and torchvision I see `No available block found in 60 second.` ``` import os os.environ["FORCE_QWENVL_VIDEO_READER"] = "torchvision" from vllm import LLM, SamplingParams from transformers import AutoProcessor from qwen_vl_utils import process_vision_info ORIGINAL_MODEL_PATH = "Qwen/Qwen2.5-VL-7B-Instruct" min_pixels = 240*426 max_pixels = 1280*28*28 llm = LLM( model=ORIGINAL_MODEL_PATH, limit_mm_per_prompt={"image": 1, "video": 1}, tensor_parallel_size=4, mm_processor_kwargs={"use_fast": True, "image_processor_type": "Qwen2VLImageProcessorFast", "min_pixels": min_pixels, "max_pixels": max_pixels,}, # I get the warning that none of these params are used disable_mm_preprocessor_cache=True, enforce_eager=True, enable_chunked_prefill=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ord and torchvision I see `No available block found in 60 second.` ``` import os os.environ["FORCE_QWENVL_VIDEO_READER"] = "torchvision" from vllm import LLM, SamplingParams from transformers import AutoProcessor from q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: vllm 0.8.0 (not 0.7.3) Qwen VL 2.5 - `No available block found in 60 second.` for hours for a video of 300 frames (cpus 100%, gpu: 0%) bug;stale ### Your current environment ### 🐛 Describe the bug vllm loads corr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 60 second.` for hours for a video of 300 frames (cpus 100%, gpu: 0%) bug;stale ### Your current environment ### 🐛 Describe the bug vllm loads correctly, but it stucks at the `.generate` call, using the cpu significantly...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=128000, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
