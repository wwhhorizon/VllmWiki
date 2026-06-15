# vllm-project/vllm#18819: [Bug]: Broken Structured Output (Guided Decoding) with Qwen3 models when `enable_thinking=False`

| 字段 | 值 |
| --- | --- |
| Issue | [#18819](https://github.com/vllm-project/vllm/issues/18819) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Broken Structured Output (Guided Decoding) with Qwen3 models when `enable_thinking=False`

### Issue 正文摘录

### Your current environment _Detailed env may not be needed for this issue_ vLLM 0.9.0 RTX A6000 Arguments: ``` --device cuda --served-model-name Qwen3-30B-A3B --quantization gptq_marlin --host 0.0.0.0 --port 8888 --max-model-len 32768 --gpu-memory-utilization 0.85 --disable-log-stats --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser qwen3 ``` ### 🐛 Describe the bug When serving Qwen3 series model on OpenAI compatible server mode, if `enable_thinking` is `false` and we specified a `guided_json`. The output json will most likely not a valid json. It can have an extra '{' or '[' or have "```" in the beginning, and can even be complete gibberish in some cases. However, if we switch `enable_thinking` to `true`, the model thinks and the output json will be valid. Furthermore, if leave `enable_thinking` as `true` and we append "/no_think" manually to user prompt, the model doesn't think and output json is also valid. If we straight up don't use any reasoning parser, the output json is also valid regardless of `enable_thinking` setting. Reproducible on both `Qwen3-32B-INT8` and `Qwen3-30B-A3B-INT4` models. Both `xgrammar` and `guidance` backend are tested. Minimum c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: OpenAI compatible server mode, if `enable_thinking` is `false` and we specified a `guided_json`. The output json will most likely not a valid json. It can have an extra '{' or '[' or have "```" in the beginning, and can...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: A6000 Arguments: ``` --device cuda --served-model-name Qwen3-30B-A3B --quantization gptq_marlin --host 0.0.0.0 --port 8888 --max-model-len 32768 --gpu-memory-utilization 0.85 --disable-log-stats --enable-auto-tool-choic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: environment _Detailed env may not be needed for this issue_ vLLM 0.9.0 RTX A6000 Arguments: ``` --device cuda --served-model-name Qwen3-30B-A3B --quantization gptq_marlin --host 0.0.0.0 --port 8888 --max-model-len 32768...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: the output json is also valid regardless of `enable_thinking` setting. Reproducible on both `Qwen3-32B-INT8` and `Qwen3-30B-A3B-INT4` models. Both `xgrammar` and `guidance` backend are tested. Minimum code to reproduce:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Broken Structured Output (Guided Decoding) with Qwen3 models when `enable_thinking=False` bug ### Your current environment _Detailed env may not be needed for this issue_ vLLM 0.9.0 RTX A6000 Arguments: ``` --dev...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
