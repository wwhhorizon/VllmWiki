# vllm-project/vllm#13751: [Usage]: in this PR(Refactor and Fix CUTLASS 2:4 Sparse Kernels)，fp8 sparse no = cutlass_scaled_sparse_mm(xxx)

| 字段 | 值 |
| --- | --- |
| Issue | [#13751](https://github.com/vllm-project/vllm/issues/13751) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: in this PR(Refactor and Fix CUTLASS 2:4 Sparse Kernels)，fp8 sparse no = cutlass_scaled_sparse_mm(xxx)

### Issue 正文摘录

### Your current environment ```text In FP8 sparse matrix multiplication, is the input row-first when weights are compressed? Another thing is that when I tested it, I found that act(mxk) w(kxn) equals cutlass_scaled_sparse_mm(act, cutlass_sparse_compress(w)) ``` @tlrmchlsmth ### How would you like to use vllm In FP8 sparse matrix multiplication, is the input row-first when weights are compressed? Another thing is that when I tested it, I found that act(mxk) w(kxn) equals cutlass_scaled_sparse_mm(act, cutlass_sparse_compress(w)) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Usage]: in this PR(Refactor and Fix CUTLASS 2:4 Sparse Kernels)，fp8 sparse no = cutlass_scaled_sparse_mm(xxx) usage ### Your current environment ```text In FP8 sparse matrix multiplication, is the input row-first when...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ls cutlass_scaled_sparse_mm(act, cutlass_sparse_compress(w)) ``` @tlrmchlsmth ### How would you like to use vllm In FP8 sparse matrix multiplication, is the input row-first when weights are compressed? Another thing is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: in this PR(Refactor and Fix CUTLASS 2:4 Sparse Kernels)，fp8 sparse no = cutlass_scaled_sparse_mm(xxx) usage ### Your current environment ```text In FP8 sparse matrix multiplication, is the input row-first when...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nput row-first when weights are compressed? Another thing is that when I tested it, I found that act(mxk) w(kxn) equals cutlass_scaled_sparse_mm(act, cutlass_sparse_compress(w)) ``` @tlrmchlsmth ### How would you like t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
