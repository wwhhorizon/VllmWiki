# vllm-project/vllm#4160: [Feature]: Support Internlm2 Lora loading

| 字段 | 值 |
| --- | --- |
| Issue | [#4160](https://github.com/vllm-project/vllm/issues/4160) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Internlm2 Lora loading

### Issue 正文摘录

I tried to modify the source code to support Lora loading of the internlm2 model, load lora is fine, but inference result is not correct. the specific modifications include: **1. add supported_lora_modules:** models/internlm2.py: `class InternLM2ForCausalLM(nn.Module): packed_modules_mapping = { "wqkv":["wqkv"], "gate_up_proj": [ "w1", "w3", ], } # LoRA specific attributes supported_lora_modules = [ "wqkv", "wo", "gate_up_proj", "w2", ] embedding_modules = {} embedding_padding_modules = []` **2. add vocab_size 92544 support:** bgmv_config.h f(in_T, out_T, W_T, narrow, 92544) \ I don't know where the problem is，some one can help me? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tried to modify the source code to support Lora loading of the internlm2 model, load lora is fine, but inference result is not correct. the specific modifications include: **1. add supported_lora_modules:** models/inter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support Internlm2 Lora loading feature request;stale I tried to modify the source code to support Lora loading of the internlm2 model, load lora is fine, but inference result is not correct. the specific modi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 2 model, load lora is fine, but inference result is not correct. the specific modifications include: **1. add supported_lora_modules:** models/internlm2.py: `class InternLM2ForCausalLM(nn.Module): packed_modules_mapping...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: internlm2.py: `class InternLM2ForCausalLM(nn.Module): packed_modules_mapping = { "wqkv":["wqkv"], "gate_up_proj": [ "w1", "w3", ], } # LoRA specific attributes supported_lora_modules = [ "wqkv", "wo", "ga

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
