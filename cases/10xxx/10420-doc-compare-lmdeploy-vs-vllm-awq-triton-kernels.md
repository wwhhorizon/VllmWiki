# vllm-project/vllm#10420: [Doc]: Compare LMDeploy vs vLLM AWQ Triton kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#10420](https://github.com/vllm-project/vllm/issues/10420) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Compare LMDeploy vs vLLM AWQ Triton kernels

### Issue 正文摘录

### 📚 The doc issue LMDeploy has their own Triton kernels implemented for AWQ. It would be interesting to know which Triton kernels are more efficient and if vLLM can improve the performance. Link to kernels: https://github.com/InternLM/lmdeploy/blob/0c80baa001e79d0b7d182b8a670190801d2d8d5b/lmdeploy/pytorch/kernels/cuda/awq_kernels.py ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r AWQ. It would be interesting to know which Triton kernels are more efficient and if vLLM can improve the performance. Link to kernels: https://github.com/InternLM/lmdeploy/blob/0c80baa001e79d0b7d182b8a670190801d2d8d5b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y/blob/0c80baa001e79d0b7d182b8a670190801d2d8d5b/lmdeploy/pytorch/kernels/cuda/awq_kernels.py ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searche...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Doc]: Compare LMDeploy vs vLLM AWQ Triton kernels documentation ### 📚 The doc issue LMDeploy has their own Triton kernels implemented for AWQ. It would be interesting to know which Triton kernels are more efficient and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: test/), which can answer lots of frequently asked questions. performance quantization cuda;kernel;quantization;triton 📚 The doc issue
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance quantization cuda;kernel;quantization;triton 📚 The doc issue

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
