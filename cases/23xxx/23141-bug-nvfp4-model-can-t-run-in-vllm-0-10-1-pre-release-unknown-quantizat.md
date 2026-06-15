# vllm-project/vllm#23141: [Bug]: nvfp4 model can't run in vllm 0.10.1-pre release, "Unknown quantization method"

| 字段 | 值 |
| --- | --- |
| Issue | [#23141](https://github.com/vllm-project/vllm/issues/23141) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nvfp4 model can't run in vllm 0.10.1-pre release, "Unknown quantization method"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug RTX5090, PyTorch 2.8.0 + cu128 vllm version: compile from the branch releases/v0.10.1 run command: ```python vllm serve /root/autodl-fs/DeepSeek-R1-0528-Qwen3-8B-FP4 --host 0.0.0.0 --port 6006 --served-model-name DeepSeek-R1-0528-Qwen3-8B-FP4 ``` model weights download from https://huggingface.co/NVFP4/DeepSeek-R1-0528-Qwen3-8B-FP4 model config: ```json { "architectures": [ "Qwen3ForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "bos_token_id": 151643, "eos_token_id": 151645, "head_dim": 128, "hidden_act": "silu", "hidden_size": 4096, "initializer_range": 0.02, "intermediate_size": 12288, "max_position_embeddings": 131072, "max_window_layers": 36, "model_type": "qwen3", "num_attention_heads": 32, "num_hidden_layers": 36, "num_key_value_heads": 8, "rms_norm_eps": 1e-06, "rope_scaling": { "attn_factor": 0.8782488562869419, "factor": 4.0, "original_max_position_embeddings": 32768, "rope_type": "yarn" }, "rope_theta": 1000000, "sliding_window": null, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.51.3", "use_cache": true, "use_sliding_window": false, "vocab_size": 151936, "quantiz...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: nvfp4 model can't run in vllm 0.10.1-pre release, "Unknown quantization method" bug ### Your current environment ### 🐛 Describe the bug RTX5090, PyTorch 2.8.0 + cu128 vllm version: compile from the branch release...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ironment ### 🐛 Describe the bug RTX5090, PyTorch 2.8.0 + cu128 vllm version: compile from the branch releases/v0.10.1 run command: ```python vllm serve /root/autodl-fs/DeepSeek-R1-0528-Qwen3-8B-FP4 --host 0.0.0.0 --port...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: nvfp4 model can't run in vllm 0.10.1-pre release, "Unknown quantization method" bug ### Your current environment ### 🐛 Describe the bug RTX5090, PyTorch 2.8.0 + cu128 vllm version: compile from the branch release...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ion method" bug ### Your current environment ### 🐛 Describe the bug RTX5090, PyTorch 2.8.0 + cu128 vllm version: compile from the branch releases/v0.10.1 run command: ```python vllm serve /root/autodl-fs/DeepSeek-R1-052...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: Must be one of ['awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'ptpc_fp8', 'fbgemm_fp8', 'modelopt', 'modelopt_fp4', 'marlin', 'bitblas', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'gptq_bitblas', 'awq_marlin', 'gptq', 'compres...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
