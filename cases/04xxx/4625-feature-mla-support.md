# vllm-project/vllm#4625: [Feature]:  MLA Support

| 字段 | 值 |
| --- | --- |
| Issue | [#4625](https://github.com/vllm-project/vllm/issues/4625) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  MLA Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch DeepSeek-V2 design **MLA (Multi-head Latent Attention)**, which utilizes low-rank key-value union compression to eliminate the bottleneck of inference-time key-value cache, thus supporting efficient inference. ![image](https://github.com/vllm-project/vllm/assets/12186261/8bad7132-ec0b-4abd-9300-efc9caf2c04e) Can VLLM support MLA for accelerated inference? @misc{deepseek-v2, author = {DeepSeek-AI}, title = {DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model}, year = {2024}, note = {GitHub repository}, url = {https://github.com/deepseek-ai/deepseek-v2} } https://huggingface.co/deepseek-ai/DeepSeek-V2-Chat https://github.com/deepseek-ai/DeepSeek-V2/blob/main/deepseek-v2-tech-report.pdf ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Seek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model}, year = {2024}, note = {GitHub repository}, url = {https://github.com/deepseek-ai/deepseek-v2} } https://huggingface.co/deepseek-ai/DeepSee...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: MLA Support feature request;stale ### 🚀 The feature, motivation and pitch DeepSeek-V2 design **MLA (Multi-head Latent Attention)**, which utilizes low-rank key-value union compression to eliminate the bottlen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: te the bottleneck of inference-time key-value cache, thus supporting efficient inference. ![image](https://github.com/vllm-project/vllm/assets/12186261/8bad7132-ec0b-4abd-9300-efc9caf2c04e) Can VLLM support MLA for acce...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: title = {DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model}, year = {2024}, note = {GitHub repository}, url = {https://github.com/deepseek-ai/deepseek-v2} } https://huggingface.co/deepse...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
