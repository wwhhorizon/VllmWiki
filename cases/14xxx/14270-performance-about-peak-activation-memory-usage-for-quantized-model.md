# vllm-project/vllm#14270: [Performance]: About peak activation memory usage for quantized model

| 字段 | 值 |
| --- | --- |
| Issue | [#14270](https://github.com/vllm-project/vllm/issues/14270) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: About peak activation memory usage for quantized model

### Issue 正文摘录

### Proposal to improve performance I'm a beginner, and I used llm-processor to quantize 7b and 14b models (weight quantization per channel, activation quantization per token dynamically). Then, I performed inference using vllm and noticed that their peak activation memory usage differs. Specifically, fp16 and int8 are almost the same(~0.7GB), but fp8(~1.5GB) is significantly higher than the other two. I conducted the inference experiments on 4090 machines with CUDA version 12.4. I don't know why. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ing vllm and noticed that their peak activation memory usage differs. Specifically, fp16 and int8 are almost the same(~0.7GB), but fp8(~1.5GB) is significantly higher than the other two. I conducted the inference experi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: About peak activation memory usage for quantized model performance;stale ### Proposal to improve performance I'm a beginner, and I used llm-processor to quantize 7b and 14b models (weight quantization per...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e other two. I conducted the inference experiments on 4090 machines with CUDA version 12.4. I don't know why. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nes with CUDA version 12.4. I don't know why. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: About peak activation memory usage for quantized model performance;stale ### Proposal to improve performance I'm a beginner, and I used llm-processor to quantize 7b and 14b models (weight quantization per...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
