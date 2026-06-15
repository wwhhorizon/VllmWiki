# vllm-project/vllm#36821: [Bug]: No sm_121 (Blackwell) support on aarch64 — NVIDIA DGX Spark / Acer GN100

| 字段 | 值 |
| --- | --- |
| Issue | [#36821](https://github.com/vllm-project/vllm/issues/36821) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: No sm_121 (Blackwell) support on aarch64 — NVIDIA DGX Spark / Acer GN100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM's prebuilt container ships PyTorch binaries compiled with CUDA kernels for GPU architectures up to sm_120. The DGX Spark's Blackwell GPU requires sm_121. Since there are no matching kernels in the binary, vLLM crashes at startup. It's a compile-time gap — the fix has to come from rebuilding PyTorch and vLLM with sm_121 targets, not from runtime configuration. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#38484 [Build] Add SM121 (DGX Spark / GB10) to published build targets

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: No sm_121 (Blackwell) support on aarch64 — NVIDIA DGX Spark / Acer GN100 bug ### Your current environment ### 🐛 Describe the bug vLLM's prebuilt container ships PyTorch binaries compiled with CUDA kernels for GPU...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### 🐛 Describe the bug vLLM's prebuilt container ships PyTorch binaries compiled with CUDA kernels for GPU architectures up to sm_120. The DGX Spark's Blackwell GPU requires sm_121. Since there are no matching kernels i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e from rebuilding PyTorch and vLLM with sm_121 targets, not from runtime configuration. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;hardware_porting;model_support cuda;kernel build_error;crash env...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38484](https://github.com/vllm-project/vllm/pull/38484) | mentioned | 0.6 | [Build] Add SM121 (DGX Spark / GB10) to published build targets | d — to unblock SM121 in published artifacts independently. Addresses #36821. ## Test evidence Tested on NVIDIA DGX Spark: \| Component \| Value \| \|-----------\|-------\| \| GPU \| NVIDI… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
