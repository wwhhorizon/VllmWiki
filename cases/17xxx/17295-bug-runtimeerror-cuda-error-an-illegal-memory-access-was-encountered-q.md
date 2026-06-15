# vllm-project/vllm#17295: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered. Qwen2.5-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#17295](https://github.com/vllm-project/vllm/issues/17295) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered. Qwen2.5-VL

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to use vLLM for inferencing `Qwen/Qwen2.5-VL-7B-Instruct` with bitsandbytes quantization. Since there is no way to pass an already instantiated huggingface model, I have separately loaded and exported the model to a local path from where vLLM can load it. Here are the download and inference scripts: `download.py`: ```python import logging import os import shutil import torch from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration, BitsAndBytesConfig os.environ["HF_HOME"] = "/vmdata/manan/.cache/huggingface" CACHE_DIR = "/vmdata/manan/.cache/huggingface" # Configure logging logging.basicConfig( level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ) logger = logging.getLogger(__name__) MODEL_DIR_BASE = "/vmdata/manan/" def download_model(model_name: str, quantization: str = None): """Download and save model files under a subdirectory named after the given model name Args: model_name: The model name or path to download from quantization: The quantization type, e.g., "4bnb" for 4-bit bitsandbytes """ # Adjust target directory based on quantization target_suffix = f"-{quantiz...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: ug]: RuntimeError: CUDA error: an illegal memory access was encountered. Qwen2.5-VL bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to use vLLM for inferencing `Qwen/Qwen2.5-VL-7B-Instruct` wit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vironment ### 🐛 Describe the bug I am trying to use vLLM for inferencing `Qwen/Qwen2.5-VL-7B-Instruct` with bitsandbytes quantization. Since there is no way to pass an already instantiated huggingface model, I have sepa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered. Qwen2.5-VL bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to use vLLM for inferencing `Qwen/Qwen2.5-VL-7B-Instruct` w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: File "/opt/conda/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 745, in _fn return fn(*args, **kwargs)
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: "image": 0, "video": 1}, # enforce_eager=True, # need this if facing Triton kernel issues ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.05, max_tokens=256, stop_token_ids=[], ) #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
