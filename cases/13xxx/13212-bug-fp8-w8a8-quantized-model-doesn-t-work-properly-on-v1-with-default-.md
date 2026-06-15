# vllm-project/vllm#13212: [Bug]: FP8 W8A8 quantized model doesn't work properly on V1 with default compilation_config (use_cudagraph = True)

| 字段 | 值 |
| --- | --- |
| Issue | [#13212](https://github.com/vllm-project/vllm/issues/13212) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 W8A8 quantized model doesn't work properly on V1 with default compilation_config (use_cudagraph = True)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - Using vLLM **V1** with **`enforce_eager=False`** - Model loaded and generate output without any error, but the output content is gibberish ### An temporary approach? Inspired by this comment, I turned `compilation_config.use_cudagraph` from `True` to `False` (diff: https://github.com/imkero/vllm/commit/92116c3ec0c0018e79665523f55d7e0b03ad28ef, should change the source code in `vllm/config.py` because it always override `compilation_config`), and then it works as expected. https://github.com/vllm-project/vllm/blob/009439caeb3ae27d1d6c94e550eee13bbd0520af/vllm/config.py#L3237-L3249 Should this problem be addressed by modifying `compilation_config`, or some bug should be fixed instead? ### Code and model to reproduce Model: [nm-testing/DeepSeek-R1-Distill-Qwen-14B-FP8-Dynamic](https://huggingface.co/nm-testing/DeepSeek-R1-Distill-Qwen-14B-FP8-Dynamic) Code: vLLM latest main: [0ccd876](https://github.com/vllm-project/vllm/commit/0ccd8769fbab6a22372dd77608293c1a80921812), and this script: ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" from vllm import LLM, SamplingParams from t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t/0ccd8769fbab6a22372dd77608293c1a80921812), and this script: ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" from vllm import LLM, SamplingParams from transformers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: FP8 W8A8 quantized model doesn't work properly on V1 with default compilation_config (use_cudagraph = True) bug ### Your current environment ### 🐛 Describe the bug - Using vLLM **V1** with **`enforce_eager=False`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 W8A8 quantized model doesn't work properly on V1 with default compilation_config (use_cudagraph = True) bug ### Your current environment ### 🐛 Describe the bug - Using vLLM **V1** with **`enforce_eager=False`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d model doesn't work properly on V1 with default compilation_config (use_cudagraph = True) bug ### Your current environment ### 🐛 Describe the bug - Using vLLM **V1** with **`enforce_eager=False`** - Model loaded and ge...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;quantization;sampling_logits cuda;fp8;operator;quantization;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
