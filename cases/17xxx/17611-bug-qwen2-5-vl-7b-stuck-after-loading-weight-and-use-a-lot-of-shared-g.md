# vllm-project/vllm#17611: [Bug]: Qwen2.5-vl-7B stuck after loading weight and use a lot of shared GPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#17611](https://github.com/vllm-project/vllm/issues/17611) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-vl-7B stuck after loading weight and use a lot of shared GPU memory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrading to the latest version of vLLM, the inference process hangs indefinitely after successfully loading the qwen2.5-vl-7B model weights. The CUDA kernel continues running, and the shared GPU memory usage keeps increasing until the outof memery. (This issue did NOT occur in v0.7.3.) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt environment ### 🐛 Describe the bug After upgrading to the latest version of vLLM, the inference process hangs indefinitely after successfully loading the qwen2.5-vl-7B model weights. The CUDA kernel continues running...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: finitely after successfully loading the qwen2.5-vl-7B model weights. The CUDA kernel continues running, and the shared GPU memory usage keeps increasing until the outof memery. (This issue did NOT occur in v0.7.3.) ###...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5-vl-7B stuck after loading weight and use a lot of shared GPU memory bug;stale ### Your current environment ### 🐛 Describe the bug After upgrading to the latest version of vLLM, the inference process hangs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;quantization;sampling_logits cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
