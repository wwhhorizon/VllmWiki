# vllm-project/vllm#5781: [Feature]: Use 64-bit integers as indices in cuda kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#5781](https://github.com/vllm-project/vllm/issues/5781) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;quantization |
| 症状 | nan_inf |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Use 64-bit integers as indices in cuda kernels

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I found that some kernels use 32-bit integers as indices, which can easily lead to overflow. I think change them into int64_t (or other 64bit types) will be safer, and should have little impact on performance. For example, if some tensor's numel >= 2^31，the fp8 quantization will fail. https://github.com/vllm-project/vllm/blob/edd5fe5fa29b8f9cc5fa37a30cc7211e0ff37067/csrc/quantization/fp8/common.cu#L43 ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: impact on performance. For example, if some tensor's numel >= 2^31，the fp8 quantization will fail. https://github.com/vllm-project/vllm/blob/edd5fe5fa29b8f9cc5fa37a30cc7211e0ff37067/csrc/quantization/fp8/common.cu#L43 #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Use 64-bit integers as indices in cuda kernels feature request;stale ### 🚀 The feature, motivation and pitch I found that some kernels use 32-bit integers as indices, which can easily lead to overflow. I thin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n will fail. https://github.com/vllm-project/vllm/blob/edd5fe5fa29b8f9cc5fa37a30cc7211e0ff37067/csrc/quantization/fp8/common.cu#L43 ### Alternatives _No response_ ### Additional context _No response_ correctness fronten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Use 64-bit integers as indices in cuda kernels feature request;stale ### 🚀 The feature, motivation and pitch I found that some kernels use 32-bit integers as indices, which can easily lead to overflow. I thin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
