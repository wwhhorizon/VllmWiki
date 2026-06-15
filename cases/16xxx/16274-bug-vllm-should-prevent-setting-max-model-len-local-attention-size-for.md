# vllm-project/vllm#16274: [Bug]: vLLM should prevent setting max_model_len < local attention size for Llama-4 models

| 字段 | 值 |
| --- | --- |
| Issue | [#16274](https://github.com/vllm-project/vllm/issues/16274) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM should prevent setting max_model_len < local attention size for Llama-4 models

### Issue 正文摘录

### Your current environment A usual flow when running OpenLLM-Leaderboard-V1 is to set `max_model_len` to the smallest required value to reduce resource requirements. This is usually `4096`. However, for Llama-4 models, evaluation is going to crash with: ``` torch._dynamo.exc.InternalTorchDynamoError: RuntimeError: CUDA error: device-side assert triggered ``` The full trace is pretty verbose and available here: https://pastebin.com/SrY62uy7 I assume the error comes from max_model_len being smaller than local attention chunk, as rerunning the eval with `max_model_len=8192` works just fine. Perhaps vLLM should either throw an error when this configuration is detected, or just override max_model_len to `min(8192, max_model_len)`. ### 🐛 Describe the bug To reproduce run (`max_model_len=4096`): ```bash lm_eval --model vllm --model_args pretrained=meta-llama/Llama-4-Scout-17B-16E-Instruct,tensor_parallel_size=4,max_model_len=4096 --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto ``` To reproduce successful run (`max_model_len=8192`): ```bash lm_eval --model vllm --model_args pretrained=meta-llama/Llama-4-Scout-17B-16E-Instruct,tensor_parallel_size=4,max_model_len=8192...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: low when running OpenLLM-Leaderboard-V1 is to set `max_model_len` to the smallest required value to reduce resource requirements. This is usually `4096`. However, for Llama-4 models, evaluation is going to crash with: `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM should prevent setting max_model_len < local attention size for Llama-4 models bug ### Your current environment A usual flow when running OpenLLM-Leaderboard-V1 is to set `max_model_len` to the smallest requ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ource requirements. This is usually `4096`. However, for Llama-4 models, evaluation is going to crash with: ``` torch._dynamo.exc.InternalTorchDynamoError: RuntimeError: CUDA error: device-side assert triggered ``` The...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: max_model_len to `min(8192, max_model_len)`. ### 🐛 Describe the bug To reproduce run (`max_model_len=4096`): ```bash lm_eval --model vllm --model_args pretrained=meta-llama/Llama-4-Scout-17B-16E-Instruct,tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s. development attention_kv_cache;model_support attention;cuda crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
