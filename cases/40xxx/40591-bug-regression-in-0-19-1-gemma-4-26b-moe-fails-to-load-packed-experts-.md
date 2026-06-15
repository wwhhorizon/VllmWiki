# vllm-project/vllm#40591: [Bug]: Regression in 0.19.1 - Gemma 4 26B MoE fails to load packed experts (KeyError: down_proj_packed). Worked in dev6.

| 字段 | 值 |
| --- | --- |
| Issue | [#40591](https://github.com/vllm-project/vllm/issues/40591) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Regression in 0.19.1 - Gemma 4 26B MoE fails to load packed experts (KeyError: down_proj_packed). Worked in dev6.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to serve **cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit** using the stable vllm-openai:v0.19.1 Docker image with --quantization compressed-tensors, the engine core crashes during model loading with a KeyError: 'layers.0.moe.experts.0.down_proj_packed'. Note on regression: This exact configuration and model worked perfectly on a recent development build (v0.19.1.dev6+g6d4a8e6d2), indicating that the logic to unpack Gemma 4 MoE weights was broken or reverted between dev6 and the stable 0.19.1 release. Additionally, as a workaround, if I try to change the flag to --quantization awq, the API server fails to start entirely due to a Pydantic ValidationError, because the model's config.json specifies compressed-tensors. Error Logs Log 1 (Using --quantization compressed-tensors): (EngineCore pid=187) ERROR 04-21 14:28:35 [core.py:1108] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/gemma4.py", line 1388, in load_weights (EngineCore pid=187) ERROR 04-21 14:28:35 [core.py:1108] param = params_dict[name] (EngineCore pid=187) ERROR 04-21 14:28:35 [core.py:1108] ~~~~~~~~~~~^^^^^^ (EngineCore pid=187) ERROR 04...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nkiwi/gemma-4-26B-A4B-it-AWQ-4bit** using the stable vllm-openai:v0.19.1 Docker image with --quantization compressed-tensors, the engine core crashes during model loading with a KeyError: 'layers.0.moe.experts.0.down_pr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Regression in 0.19.1 - Gemma 4 26B MoE fails to load packed experts (KeyError: down_proj_packed). Worked in dev6. bug ### Your current environment ### 🐛 Describe the bug When attempting to serve **cyankiwi/gemma-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Regression in 0.19.1 - Gemma 4 26B MoE fails to load packed experts (KeyError: down_proj_packed). Worked in dev6. bug ### Your current environment ### 🐛 Describe the bug When attempting to serve **cyankiwi/gemma-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Regression in 0.19.1 - Gemma 4 26B MoE fails to load packed experts (KeyError: down_proj_packed). Worked in dev6. bug ### Your current environment ### 🐛 Describe the bug When attempting to serve **cyankiwi/gemma-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: B-it-AWQ-4bit** using the stable vllm-openai:v0.19.1 Docker image with --quantization compressed-tensors, the engine core crashes during model loading with a KeyError: 'layers.0.moe.experts.0.down_proj_packed'. Note on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
