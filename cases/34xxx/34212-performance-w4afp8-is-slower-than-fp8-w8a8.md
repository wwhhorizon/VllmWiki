# vllm-project/vllm#34212: [Performance]: W4Afp8 is slower than FP8-W8A8

| 字段 | 值 |
| --- | --- |
| Issue | [#34212](https://github.com/vllm-project/vllm/issues/34212) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;multimodal_vlm;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: W4Afp8 is slower than FP8-W8A8

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression We recently tested your new W4Afp8 quantization method on a Qwen-VL model and observed a performance regression compared to FP8-W8A8 dynamic quantization. Specifically, W4Afp8 delivers about 10% slower end-to-end inference latency with fixed-length input and output and the same batch size. (length of input tokens + length of output tokens < 4k. ) We are confused why W4Afp8 currently underperforms FP8-W8A8 despite its more aggressive weight quantization? Is this expected due to dequantization overhead or some architectural factors? If this is just a temporary performance gap, do you have plans to optimize W4Afp8's inference performance in upcoming works? We're excited about the potential acceleration of W4 (if there're any) and would appreciate guidance on whether this performance gap is temporary or inherent to the quantization scheme. Thanks ahead! Here is some env info GPU H20 torch==2.9.1 CUDA==12.8 vllm: main branch llm-compressor: main branch ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: W4Afp8 is slower than FP8-W8A8 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression We recently tested your new W4Afp8 quantization method on a Qwen-VL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: regression We recently tested your new W4Afp8 quantization method on a Qwen-VL model and observed a performance regression compared to FP8-W8A8 dynamic quantization. Specifically, W4Afp8 delivers about 10% slower end-to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression We recently tested your new W4Afp8 quantization method on a Qwen-VL model and observed a performance regression compared to FP8-W8A8 dyna...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: a performance regression compared to FP8-W8A8 dynamic quantization. Specifically, W4Afp8 delivers about 10% slower end-to-end inference latency with fixed-length input and output and the same batch size. (length of inpu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ht quantization? Is this expected due to dequantization overhead or some architectural factors? If this is just a temporary performance gap, do you have plans to optimize W4Afp8's inference performance in upcoming works...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
