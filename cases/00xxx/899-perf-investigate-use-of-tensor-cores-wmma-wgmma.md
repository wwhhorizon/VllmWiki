# vllm-project/vllm#899: perf: investigate use of tensor cores (wmma, wgmma)?

| 字段 | 值 |
| --- | --- |
| Issue | [#899](https://github.com/vllm-project/vllm/issues/899) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> perf: investigate use of tensor cores (wmma, wgmma)?

### Issue 正文摘录

Seems that the implementation of dot product does not utilize tensor core. I wonder if there is possibility of using these? https://github.com/vllm-project/vllm/blob/d2b2eed67c49cdda3c1d6fa09ee2ec128b318138/csrc/attention/dtype_float32.cuh#L122 There may be some overhead but I understand that one already tries to tile Q along the HEAD_DIM. It may be an argument to try to use a higher level compiler (like triton) to manage the thread indices and tiling. Btw, why does this use uint16? I think this is the wrong file? Or simply because there is no C++ type for f16? 🤔 https://github.com/vllm-project/vllm/blob/d2b2eed67c49cdda3c1d6fa09ee2ec128b318138/csrc/attention/dtype_float16.cuh#L1

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: roject/vllm/blob/d2b2eed67c49cdda3c1d6fa09ee2ec128b318138/csrc/attention/dtype_float32.cuh#L122 There may be some overhead but I understand that one already tries to tile Q along the HEAD_DIM. It may be an argument to t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: D_DIM. It may be an argument to try to use a higher level compiler (like triton) to manage the thread indices and tiling. Btw, why does this use uint16? I think this is the wrong file? Or simply because there is no C++...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Q along the HEAD_DIM. It may be an argument to try to use a higher level compiler (like triton) to manage the thread indices and tiling. Btw, why does this use uint16? I think this is the wrong file? Or simply because t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
