# vllm-project/vllm#1419: Cannot find the config file for awq when load llm with LLaMA-2 + AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#1419](https://github.com/vllm-project/vllm/issues/1419) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Cannot find the config file for awq when load llm with LLaMA-2 + AWQ

### Issue 正文摘录

Hi，Does anyone know the reason for this? when I call awq as per the example, I get the error: File "/quantization/vllm/vllm/model_executor/weight_utils.py", line 108, in get_quant_config raise ValueError(f"Cannot find the config file for {quantization}") ValueError: Cannot find the config file for awq. vllm version: 0.2.1 (commit 651c614) **my code:** `llm = LLM(model="./models/llama-2-7b-hf",quantization="awq",dtype="half")`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Cannot find the config file for awq when load llm with LLaMA-2 + AWQ Hi，Does anyone know the reason for this? when I call awq as per the example, I get the error: File "/quantization/vllm/vllm/model_executor/weight_util...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: on for this? when I call awq as per the example, I get the error: File "/quantization/vllm/vllm/model_executor/weight_utils.py", line 108, in get_quant_config raise ValueError(f"Cannot find the config file for {quantiza...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: {quantization}") ValueError: Cannot find the config file for awq. vllm version: 0.2.1 (commit 651c614) **my code:** `llm = LLM(model="./models/llama-2-7b-hf",quantization="awq",dtype="half")`

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
