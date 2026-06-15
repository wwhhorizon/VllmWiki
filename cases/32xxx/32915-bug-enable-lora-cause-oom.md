# vllm-project/vllm#32915: [Bug]: Enable Lora cause OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#32915](https://github.com/vllm-project/vllm/issues/32915) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enable Lora cause OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deploy Qwen3-30B-A3B-AWQ usign v0.14.0 Docker image with these commands: cause OOM, while diabling Lora works ```yml vllm-Qwen3-30B-A3B-AWQ: container_name: vllm-Qwen3-30B-A3B-AWQ-2 image: vllm/vllm-openai:latest environment: - VLLM_BATCH_INVARIANT=1 command: - "ELVISIO/Qwen3-30B-A3B-Instruct-2507-AWQ" - "--served-model-name" - "Qwen3-30B-A3B" - "Qwen3-30B-A3B-Instruct-2507" - "--attention-backend" - "FLASH_ATTN" - "--api-key" - "hf_12345678" - "--max-model-len" - "40K" - "--enable-lora" - "--max-loras" - "10" - "--max-lora-rank" - "32" - "--lora-modules" - '{"name": "...., "base_model_name": "ELVISIO/Qwen3-30B-A3B-Instruct-2507-AWQ"}' ``` Note: It seems memory usage scales significantly with `max-loras`? (Each Lora adds ~ 3GB of VRAM usage even though they are not loaded. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nment ### 🐛 Describe the bug Deploy Qwen3-30B-A3B-AWQ usign v0.14.0 Docker image with these commands: cause OOM, while diabling Lora works ```yml vllm-Qwen3-30B-A3B-AWQ: container_name: vllm-Qwen3-30B-A3B-AWQ-2 image: v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: OOM bug ### Your current environment ### 🐛 Describe the bug Deploy Qwen3-30B-A3B-AWQ usign v0.14.0 Docker image with these commands: cause OOM, while diabling Lora works ```yml vllm-Qwen3-30B-A3B-AWQ: container_name: vl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: wen3-30B-A3B" - "Qwen3-30B-A3B-Instruct-2507" - "--attention-backend" - "FLASH_ATTN" - "--api-key" - "hf_12345678" - "--max-model-len" - "40K" - "--enable-lora" - "--max-loras" - "10" - "--max-lora-rank" - "32" - "-
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ISIO/Qwen3-30B-A3B-Instruct-2507-AWQ"}' ``` Note: It seems memory usage scales significantly with `max-loras`? (Each Lora adds ~ 3GB of VRAM usage even though they are not loaded. ### Before submitting a new issue... -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
