# vllm-project/vllm#13272: [Bug]: Failed to python vllm/examples/offline_inference/whisper.py

| 字段 | 值 |
| --- | --- |
| Issue | [#13272](https://github.com/vllm-project/vllm/issues/13272) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to python vllm/examples/offline_inference/whisper.py

### Issue 正文摘录

### Your current environment The env is fine. ### 🐛 Describe the bug As listed above, running test cases for whisper have failed due to the type of model runner. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: orrectness activation_norm;attention_kv_cache;frontend_api;model_support;quantization attention;cache;cuda;fp8;quantization crash;oom dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t;quantization attention;cache;cuda;fp8;quantization crash;oom dtype;env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: i;model_support;quantization attention;cache;cuda;fp8;quantization crash;oom dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ted above, running test cases for whisper have failed due to the type of model runner. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
