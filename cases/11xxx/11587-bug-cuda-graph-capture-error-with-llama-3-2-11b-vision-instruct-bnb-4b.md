# vllm-project/vllm#11587: [Bug]: CUDA Graph Capture Error with Llama-3.2-11B-Vision-Instruct-bnb-4bit on RTX 4090

| 字段 | 值 |
| --- | --- |
| Issue | [#11587](https://github.com/vllm-project/vllm/issues/11587) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Graph Capture Error with Llama-3.2-11B-Vision-Instruct-bnb-4bit on RTX 4090

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Environment:** - GPU: RTX 4090 (24GB VRAM) - Model: unsloth/Llama-3.2-11B-Vision-Instruct-bnb-4bit - vLLM command: ```bash vllm serve unsloth/Llama-3.2-11B-Vision-Instruct-bnb-4bit \ --quantization="bitsandbytes" \ --load-format="bitsandbytes" \ --dtype=bfloat16 \ --trust_remote_code \ --gpu-memory-utilization=0.98 \ --max-model-len=9600 \ --max-num-seqs 4 ``` **Error Description:** The model fails during CUDA graph capture with the error: "CUDA error: operation failed due to a previous error during capture". Memory profile shows: - Total GPU Memory: 23.54GB - Model Weights: 6.72GB - PyTorch Activation Peak: 1.92GB - Non-Torch Memory: 0.11GB - KV Cache Reserved: 14.32GB **Stack Trace:** The error occurs in `mllama.py` during the forward pass: ```python skip_cross_attention = max(attn_metadata.encoder_seq_lens) == 0 ``` This operation is not permitted during stream capture. **Additional Context:** The error persists even with 4-bit quantization enabled. The model initialization completes successfully, but fails during the CUDA graph capture phase. **Question:** Is there a workaround to run thi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: CUDA Graph Capture Error with Llama-3.2-11B-Vision-Instruct-bnb-4bit on RTX 4090 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Environment:** - GPU: RTX 4090 (24GB...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ```bash vllm serve unsloth/Llama-3.2-11B-Vision-Instruct-bnb-4bit \ --quantization="bitsandbytes" \ --load-format="bitsandbytes" \ --dtype=bfloat16 \ --trust_remote_code \ --gpu-memory-utilization=0.98 \ --max-model-len...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding cache;c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA Graph Capture Error with Llama-3.2-11B-Vision-Instruct-bnb-4bit on RTX 4090 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Environment:** - GPU: RTX 4090 (24GB V
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: d due to a previous error during capture". Memory profile shows: - Total GPU Memory: 23.54GB - Model Weights: 6.72GB - PyTorch Activation Peak: 1.92GB - Non-Torch Memory: 0.11GB - KV Cache Reserved: 14.32GB **Stack Trac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
