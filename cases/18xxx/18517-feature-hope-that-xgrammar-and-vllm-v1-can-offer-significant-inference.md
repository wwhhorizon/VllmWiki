# vllm-project/vllm#18517: [Feature]: hope that xgrammar and vLLM v1 can offer significant inference acceleration on the RTX 4090 as well

| 字段 | 值 |
| --- | --- |
| Issue | [#18517](https://github.com/vllm-project/vllm/issues/18517) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: hope that xgrammar and vLLM v1 can offer significant inference acceleration on the RTX 4090 as well

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Dear vLLM Team, We have been testing the acceleration performance of xgrammar and the latest version of vLLM across different hardware platforms. Currently, we have one question we would like to confirm: On H20, H100, and similar high-end hardware, both xgrammar and vLLM v1 demonstrate impressive acceleration performance. However, on the more cost-effective RTX 4090 GPU, xgrammar and vLLM v1 actually show a negative performance impact. As shown in the data below, vLLM 0.6.4 (which uses Outlines) outperforms vLLM 0.8.5 (which uses xgrammar), making the older version overall more advantageous in this context. instance | bs | E2E（s） | TTFT（s） | input | output | TPS -- | -- | -- | -- | -- | -- | -- 4090+vllm 0.6.4 | 15 | 19.6 | 0.26 | 900 | 402 | 20.51020408 4090+vllm 0.8.5 v0 | 15 | 24.1 | 0.483 | 813 | 414 | 17.17842324 4090+vllm 0.8.5 v1 | 15 | 31.7 | 0.335 | 637 | 323 | 10.18927445 I looked into this and found that the underlying Grammar Tree algorithm introduces additional overhead due to frequent CPU–GPU synchronization during the decoding phase. On the RTX 4090, which has lower concurrency, this leads to higher scheduling costs. In contra...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: xgrammar and vLLM v1 can offer significant inference acceleration on the RTX 4090 as well feature request;stale ### 🚀 The feature, motivation and pitch Dear vLLM Team, We have been testing the acceleration performance o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ave been testing the acceleration performance of xgrammar and the latest version of vLLM across different hardware platforms. Currently, we have one question we would like to confirm: On H20, H100, and similar high-end...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: offer significant inference acceleration on the RTX 4090 as well feature request;stale ### 🚀 The feature, motivation and pitch Dear vLLM Team, We have been testing the acceleration performance of xgrammar and the latest...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: , the RTX 4090 offers a very high cost-performance ratio when serving 8B-scale models. Therefore, we would like to kindly ask whether the vLLM team could look into optimizing xgrammar and vLLM v1 for better acceleration...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: RTX 4090 offers a very high cost-performance ratio when serving 8B-scale models. Therefore, we would like to kindly ask whether the vLLM team could look into optimizing xgrammar and vLLM v1 for better acceleration on th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
