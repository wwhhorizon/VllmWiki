# vllm-project/vllm#4547: [Bug]: v0.4.1 The output results of the MoE kinds models are incorrect on the V100

| 字段 | 值 |
| --- | --- |
| Issue | [#4547](https://github.com/vllm-project/vllm/issues/4547) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;moe;sampling_logits |
| 子分类 |  |
| Operator 关键词 | moe;sampling |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.4.1 The output results of the MoE kinds models are incorrect on the V100

### Issue 正文摘录

### Your current environment vllm: v0.4.1 GPU : V100 32G ### 🐛 Describe the bug on vllm v0.4.1 The output results of the MoE kinds model(like mixtral-8x7b ...etc ) are incorrect on the V100, but it is ok on A100. v0.4.0 is ok on V100. `curl http://10.106.124.150:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "/models/mixtral-8x7b/", "prompt": " [INST] 巴黎天氣如何? [/INST]", "max_tokens":500, "temperature": 0.5, "repetition_penalty":1.0, "presence_penalty":0.0, "top_k":50 }'` result is totally non-sense. `{"id":"cmpl-228918e446254295b9c68d7d5abfc07b","object":"text_completion","created":1714613213,"model":"/models/mixtral-8x7b-36k-ft-0428/","choices":[{"index":0,"text":" Covid in 2年2月1日，勛 Home Park 小學校，被一名女子在校內自殺。 4月1日，同一名女子再次在校內自殺。 同月1日，一名 10 歲男童在校內自殺。 同月1日，一名 8 歲女童在校內自殺。 5月19日，一名 1 歲女童在校內自殺。 同月20日，一名 1 歲男 童在校內自殺。 6月12日，一名 1 歲女童在校內自殺。 同月16日，一名 1 歲男童在校內自殺。 同月28日，一名 1 歲男童在校內自殺。 同月28日，一名 1 歲女童在校內自殺。 同月30日，一名 1 歲女童在校內自殺。 同月30日，一名 1 歲男童在校內自殺。 同月31日，一名 1 歲女童在校內自殺。 同月31日，一名 1 歲男童在校內自殺。 同月31日，一名 1 歲女童在校內自殺。 同月31日，一名 1 歲男童在校內自殺。 同月31日，一名 1 歲女 童在校內自殺。 同月31日，一名 1 歲男童在校內自殺。\nBucheng Subdistrict 15-year-old girl, 7th suicide.\nA 15-year-old girl in Bucheng Subdistrict commit...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: el(like mixtral-8x7b ...etc ) are incorrect on the V100, but it is ok on A100. v0.4.0 is ok on V100. `curl http://10.106.124.150:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "/models/mixtral-8x...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: okens":500}}` correctness model_support;moe;sampling_logits moe;sampling mismatch Your current environment
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 校內自殺。 同月31日，一名 1 歲男童在校內自殺。\nBucheng Subdistrict 15-year-old girl, 7th suicide.\nA 15-year-old girl in Bucheng Subdistrict committed suicide.\nA 15-year-old girl in Bucheng Subdistrict committed suicide.\nA 15-year-old g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: v0.4.1 The output results of the MoE kinds models are incorrect on the V100 bug;stale ### Your current environment vllm: v0.4.1 GPU : V100 32G ### 🐛 Describe the bug on vllm v0.4.1 The output results of the MoE k...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: v0.4.1 The output results of the MoE kinds models are incorrect on the V100 bug;stale ### Your current environment vllm: v0.4.1 GPU : V100 32G ### 🐛 Describe the bug on vllm v0.4.1 The output results of the MoE k...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
