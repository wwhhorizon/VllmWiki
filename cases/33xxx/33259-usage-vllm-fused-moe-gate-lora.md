# vllm-project/vllm#33259: [Usage]: vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？

| 字段 | 值 |
| --- | --- |
| Issue | [#33259](https://github.com/vllm-project/vllm/issues/33259) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;moe |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？

### Issue 正文摘录

### Your current environment 训练Qwen3 moe专家后的lora-adapter 支持用 vllm --lora-modules动态部署吗？ vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？ CUDA_VISIBLE_DEVICES=6,7 vllm serve merged-qwen3-coder-30b_case81_cp59_260120 --served-model-name model4 --host 0.0.0.0 --port 16384 --max-model-len 32768 --tensor-parallel-size 2 --disable-log-requests --enable-prefix-caching --enable-chunked-prefill --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-lora --lora-modules orpo_case9=train_adapters/moe_orpo_case9_260127/checkpoint-350 --disable-cuda-graph --disable-torch-compile --enforce-eager --max-num-batched-tokens 32768 --gpu-memory-utilization 0.8 要加的 lora adapter 是 Qwen3-Coder 的 融合后的 fused moe 的 lora weight ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: oe_orpo_case9_260127/checkpoint-350 --disable-cuda-graph --disable-torch-compile --enforce-eager --max-num-batched-tokens 32768 --gpu-memory-utilization 0.8 要加的 lora adapter 是 Qwen3-Coder 的 融合后的 fused moe 的 lora weight...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？ usage;stale ### Your current environment 训练Qwen3 moe专家后的lora-adapter 支持用 vllm --lora-modules动态部署吗？ vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？ CUDA_VISIBLE_DEVICES=6,7 vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 支持用 vllm --lora-modules动态部署吗？ vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？ CUDA_VISIBLE_DEVICES=6,7 vllm serve merged-qwen3-coder-30b_case81_cp59_260120 --served-model-name model4 --host 0.0.0.0 --port 16384 --max-model-len...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -moe 算子目前 只支持给 gate 加 LoRA吗？ usage;stale ### Your current environment 训练Qwen3 moe专家后的lora-adapter 支持用 vllm --lora-modules动态部署吗？ vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？ CUDA_VISIBLE_DEVICES=6,7 vllm serve merged-qwen3-c...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？ usage;stale ### Your current environment 训练Qwen3 moe专家后的lora-adapter 支持用 vllm --lora-modules动态部署吗？ vLLM 的 fused-moe 算子目前 只支持给 gate 加 LoRA吗？ CUDA_VISIBLE_DEVICES=6,7 vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
