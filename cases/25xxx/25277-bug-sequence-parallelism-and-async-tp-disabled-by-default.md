# vllm-project/vllm#25277: [Bug]: Sequence Parallelism and Async TP disabled by default

| 字段 | 值 |
| --- | --- |
| Issue | [#25277](https://github.com/vllm-project/vllm/issues/25277) |
| 状态 | open |
| 标签 | bug;performance;torch.compile;keep-open |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Sequence Parallelism and Async TP disabled by default

### Issue 正文摘录

Currently, due to compilation issues, we only enable sequence parallelism (and the dependent AsyncTP) for static compile sizes (and not by default). That's because sequence parallelism splits the residual tensor into smaller pieces, which breaks with piecewise compilation and dynamic shapes. #21031 addressed this but got stuck on an Inductor bug that caused extreme memory pressure. That Inductor bug has since been resolved with PyTorch 2.9. The course of action: 1. [x] Pick up #21031 and verify that [torch==2.9](https://dev-discuss.pytorch.org/t/pytorch-2-9-rc1-produced-for-pytorch/3230) resolved the memory issue (compare end-to-end activation memory with pass disabled and enabled). 2. [x] Test #21031 with changes in #24281 and `-O. use_inductor_graph_partition=True` to check that Inductor partitioning full compilation works with sequence parallelism. 3. [x] Check end-to-end performance of sequence parallelism alone as well as async TP on a dense unquantized and dense quantized model (both Hopper and Blackwell). Make sure to use full cudagraphs where available. 4. [ ] Merge the PR guarding on torch 2.9 and enable seq par and async tp by default to get performance on day 0 of torch...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Sequence Parallelism and Async TP disabled by default bug;performance;torch.compile;keep-open Currently, due to compilation issues, we only enable sequence parallelism (and the dependent AsyncTP) for static compi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: are end-to-end activation memory with pass disabled and enabled). 2. [x] Test #21031 with changes in #24281 and `-O. use_inductor_graph_partition=True` to check that Inductor partitioning full compilation works with seq...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uence Parallelism and Async TP disabled by default bug;performance;torch.compile;keep-open Currently, due to compilation issues, we only enable sequence parallelism (and the dependent AsyncTP) for static compile sizes (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rformance of sequence parallelism alone as well as async TP on a dense unquantized and dense quantized model (both Hopper and Blackwell). Make sure to use full cudagraphs where available. 4. [ ] Merge the PR guarding on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ism alone as well as async TP on a dense unquantized and dense quantized model (both Hopper and Blackwell). Make sure to use full cudagraphs where available. 4. [ ] Merge the PR guarding on torch 2.9 and enable seq par...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
