# vllm-project/vllm#37080: [Bug]: qwen 3.5 memory requirement of int4 model is higher than fp8

| 字段 | 值 |
| --- | --- |
| Issue | [#37080](https://github.com/vllm-project/vllm/issues/37080) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | fp8;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen 3.5 memory requirement of int4 model is higher than fp8

### Issue 正文摘录

### Your current environment docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_27b_int4_v1 --restart unless-stopped -v ~/.cache/huggingface/hub:/models -v ~/.cache/vllm:/root/.cache/vllm -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 vllm/vllm-openai:v0.17.1 --model Qwen/Qwen3.5-27B-GPTQ-Int4 --served-model-name llm --max-model-len 512 --reasoning-parser qwen3 --language-model-only --quantization moe_wna16 --enforce-eager ### 🐛 Describe the bug Hi, I run these examples on Nvidia L40S. Following command (for model Qwen3.5-27B-FP8) runs the model without any problems: docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_27b_fp8_v1 --restart unless-stopped -v ~/.cache/huggingface/hub:/models -v ~/.cache/vllm:/root/.cache/vllm -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 vllm/vllm-openai:v0.17.1 --model Qwen/Qwen3.5-27B-FP8 --served-model-name llm --max-model-len 512 --reasoning-parser qwen3 --language-model-only --enforce-eager Following command (for model Qwen3.5-27B-GPTQ-Int4) crashes: docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_27b_int4_v1 --restart unless-stopped -v ~/.cache/huggingface/hub:/models -v ~/.cache/vl...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: qwen 3.5 memory requirement of int4 model is higher than fp8 bug ### Your current environment docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_27b_int4_v1 --restart unless-stopped -v ~/.cache/huggingf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ement of int4 model is higher than fp8 bug ### Your current environment docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_27b_int4_v1 --restart unless-stopped -v ~/.cache/huggingface/hub:/models -v ~/.cache/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen 3.5 memory requirement of int4 model is higher than fp8 bug ### Your current environment docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_27b_int4_v1 --restart unless-stopped -v ~/.cache/huggingf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: . performance ci_build;model_support;quantization fp8;quantization crash;oom dtype Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
