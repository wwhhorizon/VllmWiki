# vllm-project/vllm#22239: [Performance]: vllm v0.10.0 seems to be much slower than vllm v0.8.5 when using Qwen3-30B-A3B-int4

| 字段 | 值 |
| --- | --- |
| Issue | [#22239](https://github.com/vllm-project/vllm/issues/22239) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: vllm v0.10.0 seems to be much slower than vllm v0.8.5 when using Qwen3-30B-A3B-int4

### Issue 正文摘录

### Proposal to improve performance I am using vllm for LLM (Qwen3-30B-A3B-int4) inference and serving When testing with the same dataset and inference machine (GPU 4090, CUDA 12.4), I found that vllm v0.10.0 is much slower than v0.8.5 in inference time (1.6s vs. 0.95s) The inference of vllm v0.8.5 is using the docker: vllm/vllm-openai:v0.8.5, which is the open source version. The inference of vllm v0.10.0 is using the docker built according the Dockerfile in the https://github.com/vllm-project/vllm.git, And the cuda version is changed to 12.4 Does anynone know the reason for this inference time difference? Thank you. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nference time (1.6s vs. 0.95s) The inference of vllm v0.8.5 is using the docker: vllm/vllm-openai:v0.8.5, which is the open source version. The inference of vllm v0.10.0 is using the docker built according the Dockerfil...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0.10.0 seems to be much slower than vllm v0.8.5 when using Qwen3-30B-A3B-int4 performance;stale ### Proposal to improve performance I am using vllm for LLM (Qwen3-30B-A3B-int4) inference and serving When testing with th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ving When testing with the same dataset and inference machine (GPU 4090, CUDA 12.4), I found that vllm v0.10.0 is much slower than v0.8.5 in inference time (1.6s vs. 0.95s) The inference of vllm v0.8.5 is using the dock...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: I am using vllm for LLM (Qwen3-30B-A3B-int4) inference and serving When testing with the same dataset and inference machine (GPU 4090, CUDA 12.4), I found that vllm v0.10.0 is much slower than v0.8.5 in inference time (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mance]: vllm v0.10.0 seems to be much slower than vllm v0.8.5 when using Qwen3-30B-A3B-int4 performance;stale ### Proposal to improve performance I am using vllm for LLM (Qwen3-30B-A3B-int4) inference and serving When t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
