# vllm-project/vllm#27911: [Bug]: Potential Integer Overflow and Out-of-bounds in selective_scan_fwd.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#27911](https://github.com/vllm-project/vllm/issues/27911) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 |  |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel |
| 症状 | nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential Integer Overflow and Out-of-bounds in selective_scan_fwd.cu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified a potential integer overflow and subsequent out-of-bounds memory access in selective_scan_fwd.cu. https://github.com/vllm-project/vllm/blob/a00d6254e998be472d8df9dc590784d6facf8d85/csrc/mamba/mamba_ssm/selective_scan_fwd.cu#L127-L128 ```dim_id * kNRows * params.u_d_stride``` may overflow. ```dim_id * kNRows * params.u_d_stride = blockIdx.y * u.size[1]``` where ```u.size[1] = batch_size * seq_len```. Example Scenario: ``` blockIdx.y = 4018 seq_len = 267264 batch_size = 2 ``` In this case, ```dim_id * kNRows * params.u_d_stride``` exceeds the 32-bit integer range, causing integer overflow. As a result, the computed pointer offset becomes negative, and the dereference of *u leads to out-of-bounds memory access. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ironment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified a potential integer overflow and subsequent out-of-bounds memory access in selective_scan_fwd.cu. https://github.com/vllm-pr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: amba_ssm/selective_scan_fwd.cu#L127-L128 ```dim_id * kNRows * params.u_d_stride``` may overflow. ```dim_id * kNRows * params.u_d_stride = blockIdx.y * u.size[1]``` where ```u.size[1] = batch_size * seq_len```. Example S...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lots of frequently asked questions. correctness cuda;kernel nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: otential Integer Overflow and Out-of-bounds in selective_scan_fwd.cu bug;stale ### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified a potential integer overf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness cuda;kernel nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
