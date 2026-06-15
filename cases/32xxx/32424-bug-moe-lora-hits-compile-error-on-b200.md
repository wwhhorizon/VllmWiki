# vllm-project/vllm#32424: [Bug]: MoE LoRA hits compile error on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#32424](https://github.com/vllm-project/vllm/issues/32424) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MoE LoRA hits compile error on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The vLLM server is unable to start when an MoE model is used with lora enabled. The issue seems to be because of the use of `gdc_wait` in the fused_moe_lora_op which isn't supported by the triton pipeliner on sm100. ```text (EngineCore_DP0 pid=11124) WARNING 01-15 18:28:11 [fused_moe.py:888] Using default MoE config. Performance might be sub-optimal! Config file not found at /home/ubuntu/meow/.venv/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/configs/E=128,N=768,device_name=NVIDIA_B200.json /home/ubuntu/meow/.venv/lib/python3.12/site-packages/vllm/lora/ops/triton_ops/fused_moe_lora_op.py:168:12: error: 'tt.elementwise_inline_asm' op pipeliner doesn't know how to predicate this op. tl.extra.cuda.gdc_wait() ^ LLVM ERROR: Fatal pipeliner error ``` Serve command ```bash uv run vllm serve --model Qwen/Qwen3-30B-A3B --enable-lora --max-model-len 8192 --enforce-eager ``` Full error log: https://gist.github.com/Jackmin801/ffdf8e16cf10239ef69c22139add9576 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docume...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: MoE LoRA hits compile error on B200 bug ### Your current environment ### 🐛 Describe the bug The vLLM server is unable to start when an MoE model is used with lora enabled. The issue seems to be because of the use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: MoE LoRA hits compile error on B200 bug ### Your current environment ### 🐛 Describe the bug The vLLM server is unable to start when an MoE model is used with lora enabled. The issue seems to be because of the use...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### 🐛 Describe the bug The vLLM server is unable to start when an MoE model is used with lora enabled. The issue seems to be because of the use of `gdc_wait` in the fused_moe_lora_op which isn't supported by the triton...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: MoE LoRA hits compile error on B200 bug ### Your current environment ### 🐛 Describe the bug The vLLM server is unable to start when an MoE model is used with lora enabled. The issue seems to be because of the use...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: use of `gdc_wait` in the fused_moe_lora_op which isn't supported by the triton pipeliner on sm100. ```text (EngineCore_DP0 pid=11124) WARNING 01-15 18:28:11 [fused_moe.py:888] Using default MoE config. Performance might...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
