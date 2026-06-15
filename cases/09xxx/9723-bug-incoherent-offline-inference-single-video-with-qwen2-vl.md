# vllm-project/vllm#9723: [Bug]: Incoherent Offline Inference Single Video with Qwen2-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#9723](https://github.com/vllm-project/vllm/issues/9723) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incoherent Offline Inference Single Video with Qwen2-VL

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I get incoherent generation outputs when using offline vLLM for inference with videos. This happens both when using URL or local paths, with 7B or 72B model, with or without tensor parallelism. The setup works well (provides coherent answers) when providing also text or text+image, but not video. This are also very different from the generated outputs when using transformers with the same arguments. The code below follows the example on the Qwen repo (https://github.com/QwenLM/Qwen2-VL?tab=readme-ov-file#inference-locally), but is also what seems to be recommended in vLLM docs ``` from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info MODEL_PATH = "Qwen/Qwen2-VL-7B-Instruct" llm = LLM( model=MODEL_PATH, limit_mm_per_prompt={"image": 10, "video": 10}, # tensor_parallel_size=4, tensor_parallel_size=1, ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.05, max_tokens=256, stop_token_ids=[], ) messages = [ {"role": "system", "content": "You are a helpful assistant."}, { "role": "user", "content":...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Incoherent Offline Inference Single Video with Qwen2-VL bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I get incoherent generation outputs when using offline vLL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: is also what seems to be recommended in vLLM docs ``` from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info MODEL_PATH = "Qwen/Qwen2-VL-7B-Instruct" ll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Incoherent Offline Inference Single Video with Qwen2-VL bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I get incoherent generation outputs when using offline vLL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
