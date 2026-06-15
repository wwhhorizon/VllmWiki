# vllm-project/vllm#12932: [Bug] ValueError: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected. Please check the logs for more details.

| 字段 | 值 |
| --- | --- |
| Issue | [#12932](https://github.com/vllm-project/vllm/issues/12932) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] ValueError: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected. Please check the logs for more details.

### Issue 正文摘录

### Your current environment I''m using two tesla t4 ```python from vllm import LLM from vllm.sampling_params import SamplingParams import torch MODEL_NAME = "Qwen/Qwen2-VL-7B-Instruct" # Define the model and sampling parameters MODEL_NAME = "Qwen/Qwen2.5-VL-7B-Instruct" sampling_params = SamplingParams(max_tokens=300, temperature=0.01, top_p=0.001) # Define context length and number of devices context_length = 3000 num_device = 2 # Initialize the LLM with the allowed local media path llm = LLM( model=MODEL_NAME, tokenizer=MODEL_NAME, speculative_max_model_len=context_length, max_seq_len_to_capture=context_length, max_model_len=context_length, tensor_parallel_size=num_device, trust_remote_code=True, # worker_use_ray=num_device, dtype=torch.float16, enable_chunked_prefill=True, gpu_memory_utilization=0.90, enforce_eager=True, max_num_batched_tokens=context_length, allowed_local_media_path="/kaggle/working/" # Add this line , # quantization="fp8" # enable_prefix_caching=True, mm_processor_kwargs={"max_dynamic_patch": 1} ) # Define the prompt and image path prompt = "Describe this image in one sentence." image_path = "file:///kaggle/working/dubu.png" # Convert local path to file:// U...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug] ValueError: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected. Please check the logs for more details. bug ### Your current environment I''m using two tesla t4 ```python from vllm i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: # Your current environment I''m using two tesla t4 ```python from vllm import LLM from vllm.sampling_params import SamplingParams import torch MODEL_NAME = "Qwen/Qwen2-VL-7B-Instruct" # Define the model and sampling par...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: device, trust_remote_code=True, # worker_use_ray=num_device, dtype=torch.float16, enable_chunked_prefill=True, gpu_memory_utilization=0.90, enforce_eager=True, max_num_batched_tokens=context_length, allowed_local_media_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug] ValueError: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected. Please check the logs for more details. bug ### Your current environment I''m using two tesla t4 ```python from vllm i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: edia path llm = LLM( model=MODEL_NAME, tokenizer=MODEL_NAME, speculative_max_model_len=context_length, max_seq_len_to_capture=context_length, max_model_len=context_length, tensor_parallel_size=num_device, trust_remote_c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
