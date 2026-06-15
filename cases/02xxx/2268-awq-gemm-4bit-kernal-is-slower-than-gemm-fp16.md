# vllm-project/vllm#2268: awq gemm 4bit kernal is slower than gemm fp16

| 字段 | 值 |
| --- | --- |
| Issue | [#2268](https://github.com/vllm-project/vllm/issues/2268) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> awq gemm 4bit kernal is slower than gemm fp16

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/44834482/184350b3-8181-4fbf-ae6b-812f2af995ca) time cost for each ops ![image](https://github.com/vllm-project/vllm/assets/44834482/a7e29482-741d-4e80-a1c6-9468abec16cc) When I was testing the llama-like model , I found that the model inference of awq int4 was slower than the fp16 version. The specific analysis was that the int4 gemm kernel was too slow. Is there any optimization plan for this part? Or are there any optimization ideas?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: , I found that the model inference of awq int4 was slower than the fp16 version. The specific analysis was that the int4 gemm kernel was too slow. Is there any optimization plan for this part? Or are there any optimizat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s/44834482/a7e29482-741d-4e80-a1c6-9468abec16cc) When I was testing the llama-like model , I found that the model inference of awq int4 was slower than the fp16 version. The specific analysis was that the int4 gemm kern...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s testing the llama-like model , I found that the model inference of awq int4 was slower than the fp16 version. The specific analysis was that the int4 gemm kernel was too slow. Is there any optimization plan for this p...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: awq gemm 4bit kernal is slower than gemm fp16 ![image](https://github.com/vllm-project/vllm/assets/44834482/184350b3-8181-4fbf-ae6b-812f2af995ca) time cost for each ops ![image](https://github.com/vllm-project/vllm/asse...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t/vllm/assets/44834482/a7e29482-741d-4e80-a1c6-9468abec16cc) When I was testing the llama-like model , I found that the model inference of awq int4 was slower than the fp16 version. The specific analysis was that the in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
