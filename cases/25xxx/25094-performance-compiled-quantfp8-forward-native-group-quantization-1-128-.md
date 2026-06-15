# vllm-project/vllm#25094: [Performance]: Compiled `QuantFP8.forward_native` group quantization (1, 128) slower than CUDA on H100/RTX5090

| 字段 | 值 |
| --- | --- |
| Issue | [#25094](https://github.com/vllm-project/vllm/issues/25094) |
| 状态 | open |
| 标签 | help wanted;performance;torch.compile;keep-open;needs reproduction |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Compiled `QuantFP8.forward_native` group quantization (1, 128) slower than CUDA on H100/RTX5090

### Issue 正文摘录

**EDIT**: These numbers should be collected again with torch==2.10 and torch==2.11 to check if the situation has improved. ### Your current environment ### 🐛 Describe the bug The recently added native torch implementation for group quantization (https://github.com/vllm-project/vllm/pull/24342) exhibits inconsistent performance across different GPUs, particularly for row-major layouts with a group shape of (1, 128). While it's faster (or on par with) CUDA on B200, it's slower on H100 and RTX 5090. _Benchmarks added below._ To reproduce, run: ``` python3 benchmarks/kernels/bench_per_token_quant_fp8.py --group-sizes 128 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: mpiled `QuantFP8.forward_native` group quantization (1, 128) slower than CUDA on H100/RTX5090 help wanted;performance;torch.compile;keep-open;needs reproduction **EDIT**: These numbers should be collected again with tor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Performance]: Compiled `QuantFP8.forward_native` group quantization (1, 128) slower than CUDA on H100/RTX5090 help wanted;performance;torch.compile;keep-open;needs reproduction **EDIT**: These numbers should be collect...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Performance]: Compiled `QuantFP8.forward_native` group quantization (1, 128) slower than CUDA on H100/RTX5090 help wanted;performance;torch.compile;keep-open;needs reproduction **EDIT**: These numbers should be collect...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: aster (or on par with) CUDA on B200, it's slower on H100 and RTX 5090. _Benchmarks added below._ To reproduce, run: ``` python3 benchmarks/kernels/bench_per_token_quant_fp8.py --group-sizes 128 ``` ### Before submitting...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
