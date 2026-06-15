# vllm-project/vllm#22882: [Bug]: Loading a quantized model from S3 fails

| 字段 | 值 |
| --- | --- |
| Issue | [#22882](https://github.com/vllm-project/vllm/issues/22882) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Loading a quantized model from S3 fails

### Issue 正文摘录

### Your current environment vLLM ignores the `--load_format=runai_streamer` argument when loading a quantized model from S3. It detects that the model is quantized and switches to the BitsAndBytes loader instead. I understand why it makes this switch, but shouldn’t it first download the model weights using Run:ai before switching? It would also be helpful if the logs stated the reason for overriding the loader, as that would make debugging easier. I am using [this](https://hub.docker.com/layers/vllm/vllm-openai/v0.10.0/images/sha256-05a31dc4185b042e91f4d2183689ac8a87bd845713d5c3f987563c5899878271) Docker image: v0.10.0. ### 🐛 Describe the bug Logs output ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: der, as that would make debugging easier. I am using [this](https://hub.docker.com/layers/vllm/vllm-openai/v0.10.0/images/sha256-05a31dc4185b042e91f4d2183689ac8a87bd845713d5c3f987563c5899878271) Docker image: v0.10.0. #...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Loading a quantized model from S3 fails bug;stale ### Your current environment vLLM ignores the `--load_format=runai_streamer` argument when loading a quantized model from S3. It detects that the model is quantiz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Loading a quantized model from S3 fails bug;stale ### Your current environment vLLM ignores the `--load_format=runai_streamer` argument when loading a quantized model from S3. It detects that the model is quantiz...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits attention;cuda;operator;quantization;sampling crash;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
