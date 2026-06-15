# vllm-project/vllm#22692: [Bug]: GLM4.5 infer speed slow

| 字段 | 值 |
| --- | --- |
| Issue | [#22692](https://github.com/vllm-project/vllm/issues/22692) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | fp8 |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM4.5 infer speed slow

### Issue 正文摘录

### Your current environment vllm 0.10.0 8*H100 CLI: ``` bash vllm serve /GLM-4.5-FP8 \ --tensor-parallel-size 8 \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --cpu-offload-gb 16 \ --served-model-name glm-4.5-fp8 ``` ### 🐛 Describe the bug Infer speed is: 6.4 Tokens/s Is this normal? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rent environment vllm 0.10.0 8*H100 CLI: ``` bash vllm serve /GLM-4.5-FP8 \ --tensor-parallel-size 8 \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --cpu-offload-gb 16 \ --served-mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GLM4.5 infer speed slow bug ### Your current environment vllm 0.10.0 8*H100 CLI: ``` bash vllm serve /GLM-4.5-FP8 \ --tensor-parallel-size 8 \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --enable-auto-tool-cho...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: --reasoning-parser glm45 \ --enable-auto-tool-choice \ --cpu-offload-gb 16 \ --served-model-name glm-4.5-fp8 ``` ### 🐛 Describe the bug Infer speed is: 6.4 Tokens/s Is this normal? ### Before submitting a new issue... -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: \ --enable-auto-tool-choice \ --cpu-offload-gb 16 \ --served-model-name glm-4.5-fp8 ``` ### 🐛 Describe the bug Infer speed is: 6.4 Tokens/s Is this normal? ### Before submitting a new issue... - [x] Make sure you alread...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;model_support;quantization fp8 slowdown dtype Your c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
