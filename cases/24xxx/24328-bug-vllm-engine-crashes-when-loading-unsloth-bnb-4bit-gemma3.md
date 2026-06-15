# vllm-project/vllm#24328: [Bug]: vLLM engine crashes when loading unsloth bnb 4bit Gemma3

| 字段 | 值 |
| --- | --- |
| Issue | [#24328](https://github.com/vllm-project/vllm/issues/24328) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM engine crashes when loading unsloth bnb 4bit Gemma3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was trying to load `unsloth/gemma-3-1b-it-bnb-4bit` with vLLM like the documentation for loading bitsandbytes quantization here: https://docs.vllm.ai/en/latest/features/quantization/bnb.html#read-quantized-checkpoint. However, I ran into an error of the engine failing to initialize after the model has been downloaded. On the exact same setup, I tried loading `google/gemma-3-1b-it` which is the unquantised version and it works perfectly fine. Would appreciate if you can provide any info of if anything went wrong or if I'm not using it properly, thanks! EDIT: When I tried using other models from unsloth like `unsloth/tinyllama-bnb-4bit` shown on the docs, everything works fine, not sure if this is an issue specific to Gemma? However Gemma is indeed listed on the supported models ```python from vllm import LLM, SamplingParams import torch model_id = "unsloth/gemma-3-1b-it-bnb-4bit" llm = LLM( model=model_id, dtype=torch.bfloat16, trust_remote_code=True ) ``` Full traceback: ``` DEBUG 09-05 15:20:27 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 09-05 15:20:27 [__init__.py:34] Checking if TPU platform is a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e setup, I tried loading `google/gemma-3-1b-it` which is the unquantised version and it works perfectly fine. Would appreciate if you can provide any info of if anything went wrong or if I'm not using it properly, thank...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: b-it-bnb-4bit` with vLLM like the documentation for loading bitsandbytes quantization here: https://docs.vllm.ai/en/latest/features/quantization/bnb.html#read-quantized-checkpoint. However, I ran into an error of the en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 09-05 15:20:27 [__init__.py:58] Checking if CUDA platform is available. DEBUG 09-05 15:20:27 [__init__.py:78] Confirmed CUDA platform is available. DEBUG 09-05 15:20:27 [__init__.py:106] Chec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM engine crashes when loading unsloth bnb 4bit Gemma3 bug ### Your current environment ### 🐛 Describe the bug I was trying to load `unsloth/gemma-3-1b-it-bnb-4bit` with vLLM like the documentation for loading...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ion;sampling_logits;scheduler_memory cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
