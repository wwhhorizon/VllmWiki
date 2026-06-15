# vllm-project/vllm#41899: [Bug]: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet

| 字段 | 值 |
| --- | --- |
| Issue | [#41899](https://github.com/vllm-project/vllm/issues/41899) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using vLLM to serve a fine-tuned Qwen3-Omni model with LoRA enabled, inference fails during model initialization with: ```text ValueError: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet. ``` However, the same LoRA adapter works correctly after merging into the base model. This suggests that **LoRA merging is supported implicitly**, but **runtime LoRA injection via `--enable-lora` is not supported for this model class**. Serving command ```bash VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 vllm serve \ /Qwen3-Omni-30B-A3B-Instruct/ \ --port 8003 --host 0.0.0.0 \ --enable-lora \ --max-lora-rank 32 \ --max-loras 2 \ --lora-modules test_lora=/data/v2-20260416-101216/checkpoint-548/ \ --dtype bfloat16 \ --uvicorn-log-level debug \ --gpu-memory-utilization 0.95 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --trust_remote_code \ --enable-log-requests \ --enable-log-outputs \ --max-model-len 30720 \ --enable-prefix-caching ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](http...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nto the base model. This suggests that **LoRA merging is supported implicitly**, but **runtime LoRA injection via `--enable-lora` is not supported for this model class**. Serving command ```bash VLLM_USE_V1=1 CUDA_VISIB...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: \ --lora-modules test_lora=/data/v2-20260416-101216/checkpoint-548/ \ --dtype bfloat16 \ --uvicorn-log-level debug \ --gpu-memory-utilization 0.95 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --trust_remote...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: upported for this model class**. Serving command ```bash VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 vllm serve \ /Qwen3-Omni-30B-A3B-Instruct/ \ --port 8003 --host 0.0.0.0 \ --enable-lora \ --max-lora-rank 32 \ --max-loras 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet bug ### Your current environment ### 🐛 Describe the bug When using vLLM to serve a fine-tuned Qwen3-Omni model with LoRA enabled, inference fa...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet bug ### Your current environment ### 🐛 Describe the bug When using vLLM to serve a fine-tuned Qwen3-Omni model with LoRA enabled, inference fa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
