# vllm-project/vllm#3044: Support LoRA for Gemma

| 字段 | 值 |
| --- | --- |
| Issue | [#3044](https://github.com/vllm-project/vllm/issues/3044) |
| 状态 | closed |
| 标签 | good first issue |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support LoRA for Gemma

### Issue 正文摘录

I am getting the following error when loading a lora adaptor for Gemma model: ```bash python -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --model google/gemma-7b \ --enable-lora \ --lora-modules quote=/artifacts \ --max-model-len 1024 | tee ~/openai_api_server.log ``` ``` ValueError: Model GemmaForCausalLM does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Support LoRA for Gemma good first issue I am getting the following error when loading a lora adaptor for Gemma model: ```bash python -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --model google/gemma-7b \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. ```
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Support LoRA for Gemma good first issue I am getting the following error when loading a lora adaptor for Gemma model: ```bash python -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --model google/gemma-7b \...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
