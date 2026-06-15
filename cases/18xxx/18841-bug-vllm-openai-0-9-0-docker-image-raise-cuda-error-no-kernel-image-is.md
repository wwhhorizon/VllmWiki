# vllm-project/vllm#18841: [Bug]: vllm-openai:0.9.0 docker image raise 'CUDA error: no kernel image is available for execution on the device' for Llama4 Maverick FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#18841](https://github.com/vllm-project/vllm/issues/18841) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm-openai:0.9.0 docker image raise 'CUDA error: no kernel image is available for execution on the device' for Llama4 Maverick FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to serve [Llama 4 Maverick FP8](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) checkpoint using [the official vllm-openai:0.9.0 container image](https://hub.docker.com/layers/vllm/vllm-openai/v0.9.0/images/sha256-df2c55e5107afea09ea1a50f9dd96c99ebf97a795334c4d08f691f3d79b2ab12) but face the following "no kernel image is available" error: vllm arguments in the form of deployment yaml is as follows: ```yaml ... containers: - name: kserve-container image: docker.io/vllm/vllm-openai:0.9.0 args: - "/mnt/models/llama-4-maverick-17b-128e-fp8/" - "--served-model-name" - "meta-llama/llama-4-maverick-17b-128e-instruct" - "--host" - "0.0.0.0" - "--port" - "8080" - "--gpu-memory-utilization" - "0.94" - "--tensor-parallel-size" - "8" - "--max-num-batched-tokens" - "16384" - "--max-num-seqs" - "16" - "--kv-cache-dtype" - "fp8" - "--enable-auto-tool-choice" - "--tool-call-parser" - "llama4_json" - "--limit-mm-per-prompt" - "image=5" - "--override-generation-config" - '{"attn_temperture_tuning":true}' ... ``` I have checked that removing the optional args on kv cache dtypes or generation configs or decreasin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: UDA error: no kernel image is available for execution on the device' for Llama4 Maverick FP8 bug ### Your current environment ### 🐛 Describe the bug I'm trying to serve [Llama 4 Maverick FP8](https://huggingface.co/meta...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vllm-openai:0.9.0 docker image raise 'CUDA error: no kernel image is available for execution on the device' for Llama4 Maverick FP8 bug ### Your current environment ### 🐛 Describe the bug I'm trying to serve [Lla...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rnel image is available for execution on the device' for Llama4 Maverick FP8 bug ### Your current environment ### 🐛 Describe the bug I'm trying to serve [Llama 4 Maverick FP8](https://huggingface.co/meta-llama/Llama-4-M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vllm-openai:0.9.0 docker image raise 'CUDA error: no kernel image is available for execution on the device' for Llama4 Maverick FP8 bug ### Your current environment ### 🐛 Describe the bug I'm trying to serve [Lla...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: - "16384" - "--max-num-seqs" - "16" - "--kv-cache-dtype" - "fp8" - "--enable-auto-tool-choice" - "--tool-call-parser" - "llama4_json" - "--limit-mm-per-prompt" - "image=5" - "--override-gener

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
