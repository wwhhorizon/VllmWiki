# vllm-project/vllm#33143: [Bug]: Triton MLIR Error when attempting to run gpt-oss-20b

| 字段 | 值 |
| --- | --- |
| Issue | [#33143](https://github.com/vllm-project/vllm/issues/33143) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton MLIR Error when attempting to run gpt-oss-20b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `openai/gpt-oss-20b` fails to launch with the `vllm/vllm-openai-rocm` docker image I have needed to cut out a lot of the output to fit under the character limit. I have attached the full logs to this issue [vllm.log](https://github.com/user-attachments/files/24873512/vllm.log) This is consistently reproducable, and occurs every time. This error only appears specifically with gpt-oss-20b. Please let me know if you would like me to provide any additional details, logging or tests. Since this is an MLIR error, perhaps this should be reported upstream to either Triton or LLVM instead? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g `openai/gpt-oss-20b` fails to launch with the `vllm/vllm-openai-rocm` docker image I have needed to cut out a lot of the output to fit under the character limit. I have attached the full logs to this issue [vllm.log](...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Triton MLIR Error when attempting to run gpt-oss-20b bug;rocm ### Your current environment ### 🐛 Describe the bug `openai/gpt-oss-20b` fails to launch with the `vllm/vllm-openai-rocm` docker image I have needed t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ectness ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;kernel;moe;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_depend...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Triton MLIR Error when attempting to run gpt-oss-20b bug;rocm ### Your current environment ### 🐛 Describe the bug `openai/gpt-oss-20b` fails to launch with the `vllm/vllm-openai-rocm` docker image I have needed t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Triton MLIR Error when attempting to run gpt-oss-20b bug;rocm ### Your current environment ### 🐛 Describe the bug `openai/gpt-oss-20b` fails to launch with the `vllm/vllm-openai-rocm` docker image I have needed to

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
