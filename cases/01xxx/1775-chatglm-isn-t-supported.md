# vllm-project/vllm#1775: chatglm isn't supported.

| 字段 | 值 |
| --- | --- |
| Issue | [#1775](https://github.com/vllm-project/vllm/issues/1775) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> chatglm isn't supported.

### Issue 正文摘录

Trying to use AutoAWQ to quantize the chatglm pattern, the result is: chatglm isn't supported yet. Is there a solution? my code just like this: ``` model_path = '/home/incar/newdata2/tms/llm/chatglm3-6b-32k' quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM" } model = AutoAWQForCausalLM.from_pretrained(model_path, **{"low_cpu_mem_usage": True}) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m isn't supported yet. Is there a solution? my code just like this: ``` model_path = '/home/incar/newdata2/tms/llm/chatglm3-6b-32k' quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ' quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM" } model = AutoAWQForCausalLM.from_pretrained(model_path, **{"low_cpu_mem_usage": True}) ```
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: chatglm isn't supported. Trying to use AutoAWQ to quantize the chatglm pattern, the result is: chatglm isn't supported yet. Is there a solution? my code just like this: ``` model_path = '/home/incar/newdata2/tms/llm/cha...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: fig = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM" } model = AutoAWQForCausalLM.from_pretrained(model_path, **{"low_cpu_mem_usage": True}) ```

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
