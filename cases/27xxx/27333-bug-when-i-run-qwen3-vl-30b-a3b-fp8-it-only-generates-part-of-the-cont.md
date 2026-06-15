# vllm-project/vllm#27333: [Bug]: When I run qwen3-vl-30b-a3b-fp8, it only generates part of the content

| 字段 | 值 |
| --- | --- |
| Issue | [#27333](https://github.com/vllm-project/vllm/issues/27333) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When I run qwen3-vl-30b-a3b-fp8, it only generates part of the content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run qwen3-vl-30b-a3b-fp8, it only generates part of the content and then displays: ``` (Worker_TP0 pid=193108) INFO 10-22 17:38:02 [multiproc_executor.py:558] Parent process exited, terminating worker (Worker_TP0 pid=193108) INFO 10-22 17:38:02 [multiproc_executor.py:599] WorkerProc shutting down. (Worker_TP1 pid=193109) INFO 10-22 17:38:02 [multiproc_executor.py:558] Parent process exited, terminating worker ``` this is my code: ```python # -*- coding: utf-8 -*- import torch from qwen_vl_utils import process_vision_info from modelscope import AutoProcessor from vllm import LLM, SamplingParams import os os.environ['VLLM_WORKER_MULTIPROC_METHOD'] = 'spawn' def prepare_inputs_for_vllm(messages, processor): text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) # qwen_vl_utils 0.0.14+ reqired image_inputs, video_inputs, video_kwargs = process_vision_info( messages, image_patch_size=processor.image_processor.patch_size, return_video_kwargs=True, return_video_metadata=True ) print(f"video_inputs: {video_inputs}") print(f"video_kwargs: {video_kwargs}") mm_data = {} if image_inputs is not None:...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: en I run qwen3-vl-30b-a3b-fp8, it only generates part of the content bug;stale ### Your current environment ### 🐛 Describe the bug When I run qwen3-vl-30b-a3b-fp8, it only generates part of the content and then displays...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: erminating worker ``` this is my code: ```python # -*- coding: utf-8 -*- import torch from qwen_vl_utils import process_vision_info from modelscope import AutoProcessor from vllm import LLM, SamplingParams import os os....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: When I run qwen3-vl-30b-a3b-fp8, it only generates part of the content bug;stale ### Your current environment ### 🐛 Describe the bug When I run qwen3-vl-30b-a3b-fp8, it only generates part of the content and then...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: on=0.95, enforce_eager=False, tensor_parallel_size=torch.cuda.device_count(), seed=0, max_model_len=63792, ) sampling_params = SamplingParams( temperature=0, max_tokens=2048, top_k=-1, stop_token_ids=[], ) outpu

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
