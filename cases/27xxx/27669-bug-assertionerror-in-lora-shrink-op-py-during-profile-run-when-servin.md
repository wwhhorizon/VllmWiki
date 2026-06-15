# vllm-project/vllm#27669: [Bug]: AssertionError in lora_shrink_op.py during profile_run when serving Qwen3-VL-8B-Instruct with LoRA on v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#27669](https://github.com/vllm-project/vllm/issues/27669) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError in lora_shrink_op.py during profile_run when serving Qwen3-VL-8B-Instruct with LoRA on v0.11.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello vLLM Team, I am encountering an AssertionError when attempting to serve the multimodal model Qwen3-VL-8B-Instruct with a LoRA adapter using vLLM version 0.11.0. The base model runs correctly in pure text mode without LoRA, but when loading the LoRA adapter, the engine fails during initialization. Given that Qwen3-VL is a multimodal model, and my application requires image/video understanding capabilities, dynamically serving LoRA on this model is crucial. The issue appears to occur during the engine's memory profile run for the multimodal component, where it incorrectly enters the LoRA acceleration code path (lora_shrink_op) which expects certain mapping dimensions that are not present. Steps to Reproduce Start the vLLM server with the Qwen3-VL-8B-Instruct model and a LoRA adapter (assuming the command includes --enable-lora and the LoRA adapter is ready to be loaded via API or startup arguments): Bash vllm serve --model ./Qwen3-VL-8B-Instruct/ --lora-modules lora_name=./path/to/your/lora/adapter --enable-lora [other Qwen-VL args like --max-model-len] The engine core starts loading the model weights successfully. The engine...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the multimodal model Qwen3-VL-8B-Instruct with a LoRA adapter using vLLM version 0.11.0. The base model runs correctly in pure text mode without LoRA, but when loading the LoRA adapter, the engine fails during initializ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ug]: AssertionError in lora_shrink_op.py during profile_run when serving Qwen3-VL-8B-Instruct with LoRA on v0.11.0 bug;stale ### Your current environment ### 🐛 Describe the bug Hello vLLM Team, I am encountering an Asse...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: AssertionError in lora_shrink_op.py during profile_run when serving Qwen3-VL-8B-Instruct with LoRA on v0.11.0 bug;stale ### Your current environment ### 🐛 Describe the bug Hello vLLM Team, I am encountering an As...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: me/work/env/miniconda_qwen3vl/lib/python3.10/site-packages/vllm/lora/ops/triton_ops/lora_shrink_op.py", line 149, in _lora_shrink (EngineCore_DP0 pid=9785) ERROR 10-27 22:45:38 [v1/engine/core.py:708] assert token_lora_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
