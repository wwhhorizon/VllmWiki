# vllm-project/vllm#30958: [Bug]: Vllm Server stuck and automatically shutdown.

| 字段 | 值 |
| --- | --- |
| Issue | [#30958](https://github.com/vllm-project/vllm/issues/30958) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm Server stuck and automatically shutdown.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug import argparse import os import sys import subprocess import json from typing import List, Optional def start_vllm_server( model_path: str, model_name: str, port: int = 8000, host: str = "0.0.0.0", gpu_memory_utilization: float = 0.9, max_model_len: int = 8192, dtype: str = "bfloat16", tensor_parallel_size: Optional[int] = None, pipeline_parallel_size: Optional[int] = None, generation_config: Optional[str] = None, max_pixels: Optional[int] = None, enforce_eager: bool = True, ): """Start the vLLM server with the specified parameters.""" # Build the command print(max_model_len) cmd = [ "python", "-m", "vllm.entrypoints.openai.api_server", "--model", model_path, "--host", host, "--port", str(port), "--gpu-memory-utilization", str(gpu_memory_utilization), "--max-model-len", str(max_model_len), "--dtype", dtype, # "--enforce-eager", "--served-model-name", model_name, # "--limit-mm-per-prompt", "image=1,video=0", # "--mm-processor-kwargs", mm_kwargs_str, ] # if "Qwen2.5-VL" in model_name: # cmd += ["--limit-mm-per-prompt", "image=1,video=0" ] if enforce_eager: cmd.append("--enforce-eager") if max_pixels is not None: mm_kwargs_dict = {...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: mport json from typing import List, Optional def start_vllm_server( model_path: str, model_name: str, port: int = 8000, host: str = "0.0.0.0", gpu_memory_utilization: float = 0.9, max_model_len: int = 8192, dtype: str =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: y shutdown. bug ### Your current environment ### 🐛 Describe the bug import argparse import os import sys import subprocess import json from typing import List, Optional def start_vllm_server( model_path: str, model_name...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: "rb") as image_file: return base64.b64encode(image_file.read()).decode("utf-8") def PIL_to_base64(img: Image.Image, fmt: str = "PNG") -> str: """ Convert a PIL.Image to a base64‑encoded string. Parameters ---------- img...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: if retries , dtype='bfloat16', max_model_len=8192, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, te...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: gpu_memory_utilization: float = 0.9, max_model_len: int = 8192, dtype: str = "bfloat16", tensor_parallel_size: Optional[int] = None, pipeline_parallel_size: Optional[int] = None, generation_config: Optional[str] = None,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
