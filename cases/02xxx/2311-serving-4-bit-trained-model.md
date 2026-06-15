# vllm-project/vllm#2311: serving 4-bit trained model

| 字段 | 值 |
| --- | --- |
| Issue | [#2311](https://github.com/vllm-project/vllm/issues/2311) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;operator;quantization |
| 症状 |  |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> serving 4-bit trained model

### Issue 正文摘录

I am training model based on "mistralai/Mistral-7B-Instruct-v0.1" but I am unable to serve it using docker image vllm/vllm-openai:latest I am exe using python3 -m vllm.entrypoints.openai.api_server --model --gpu-memory-utilization 0.90 I tried rebooting the instant and now I am getting only following error constantly repeating: ../aten/src/ATen/native/cuda/ScatterGatherKernel.cu:144: operator(): block: [8970,0,0], thread: [36,0,0] Assertion `idx_dim >= 0 && idx_dim = 0 && idx_dim < index_size && "index out of bounds"` failed. ... training parameters below: ################################################################################ # QLoRA parameters ################################################################################ # LoRA attention dimension lora_r = 64 # Alpha parameter for LoRA scaling lora_alpha = 16 # Dropout probability for LoRA layers lora_dropout = 0.1 ################################################################################ # bitsandbytes parameters ################################################################################ # Activate 4-bit precision base model loading use_4bit = True # Compute dtype for 4-bit base models bnb_4bit_compute_dty...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: # Activate 4-bit precision base model loading use_4bit = True # Compute dtype for 4-bit base models bnb_4bit_compute_dtype = "float16" # Quantization type (fp4 or nf4) bnb_4bit_quant_type = "nf4" # Activate nested quant...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: "mistralai/Mistral-7B-Instruct-v0.1" but I am unable to serve it using docker image vllm/vllm-openai:latest I am exe using python3 -m vllm.entrypoints.openai.api_server --model --gpu-memory-utilization 0.90 I tried rebo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ng: ../aten/src/ATen/native/cuda/ScatterGatherKernel.cu:144: operator(): block: [8970,0,0], thread: [36,0,0] Assertion `idx_dim >= 0 && idx_dim = 0 && idx_dim < index_size && "index out of bounds"` failed. ... training...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tting only following error constantly repeating: ../aten/src/ATen/native/cuda/ScatterGatherKernel.cu:144: operator(): block: [8970,0,0], thread: [36,0,0] Assertion `idx_dim >= 0 && idx_dim = 0 && idx_dim < index_size &&...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: v0.1" but I am unable to serve it using docker image vllm/vllm-openai:latest I am exe using python3 -m vllm.entrypoints.openai.api_server --model --gpu-memory-utilization 0.90 I tried rebooting the instant and now I am...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
