# vllm-project/vllm#6246: [Misc]: fp8 support

| 字段 | 值 |
| --- | --- |
| Issue | [#6246](https://github.com/vllm-project/vllm/issues/6246) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: fp8 support

### Issue 正文摘录

### Anything you want to discuss about vllm. when we use fp8 data type , we found ffn gemm/atten prj support real fp8 compute(this is supported on H20、L20), but Q*transopse(Key) or softmax * value in attention dosen't support fp8 compute, need to first dequantize fp8 to fp16/bf16, why? is there any plan to support attention fp8 compute?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Misc]: fp8 support ### Anything you want to discuss about vllm. when we use fp8 data type , we found ffn gemm/atten prj support real fp8 compute(this is supported on H20、L20), but Q*transopse(Key) or softmax * value in...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: u want to discuss about vllm. when we use fp8 data type , we found ffn gemm/atten prj support real fp8 compute(this is supported on H20、L20), but Q*transopse(Key) or softmax * value in attention dosen't support fp8 comp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
