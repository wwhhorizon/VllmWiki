# vllm-project/vllm#14986: [Bug]: vllm 0.7.3-0.8.0rc3 - QWEN2.5-VL: `video_grid_thw[video_index][0], [multiproc_executor.py:375] IndexError: list index out of range`

| 字段 | 值 |
| --- | --- |
| Issue | [#14986](https://github.com/vllm-project/vllm/issues/14986) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;quantization;sampling;triton |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.7.3-0.8.0rc3 - QWEN2.5-VL: `video_grid_thw[video_index][0], [multiproc_executor.py:375] IndexError: list index out of range`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have an error that appears whenever I run the inference multiple times. I tried: - having different videos as input - disable prefix caching - engine v1-> v0 - 0.7.3->getting the latest master vllm - using bigger gpus - flash attention vs xformers - ```python # Tried all these envs #import os #os.environ["VLLM_ATTENTION_BACKEND"] = "XFORMERS" #os.environ["VLLM_USE_V1"]="0" from vllm import LLM, SamplingParams from transformers import AutoProcessor from qwen_vl_utils import process_vision_info MODEL_PATH = "Qwen/Qwen2.5-VL-7B-Instruct" llm = LLM( model=MODEL_PATH, limit_mm_per_prompt={"image": 1, "video": 1}, tensor_parallel_size=2, max_num_seqs=1, #enable_prefix_caching=False, enable_chunked_prefill=False, max_model_len=80000, enforce_eager=True, #gpu_memory_utilization=0.6 ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.05, max_tokens=512, stop_token_ids=[], ) prompt = """ Describe the video """ for i in range(2): messages = [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": [ {"type": "text", "text": prompt}, { "type": "video", "video": f"/data/s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: gpus - flash attention vs xformers - ```python # Tried all these envs #import os #os.environ["VLLM_ATTENTION_BACKEND"] = "XFORMERS" #os.environ["VLLM_USE_V1"]="0" from vllm import LLM, SamplingParams from transformers i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: vllm 0.7.3-0.8.0rc3 - QWEN2.5-VL: `video_grid_thw[video_index][0], [multiproc_executor.py:375] IndexError: list index out of range` bug ### Your current environment ### 🐛 Describe the bug I have an error that app...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=80000, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: =2, max_num_seqs=1, #enable_prefix_caching=False, enable_chunked_prefill=False, max_model_len=80000, enforce_eager=True, #gpu_memory_utilization=0.6 ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ne v1-> v0 - 0.7.3->getting the latest master vllm - using bigger gpus - flash attention vs xformers - ```python # Tried all these envs #import os #os.environ["VLLM_ATTENTION_BACKEND"] = "XFORMERS" #os.environ["VLLM_USE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
