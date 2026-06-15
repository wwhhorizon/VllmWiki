# vllm-project/vllm#20816: [Bug]: Llama 4 Garbled Outputs on long prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#20816](https://github.com/vllm-project/vllm/issues/20816) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8 |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama 4 Garbled Outputs on long prompts

### Issue 正文摘录

### Your current environment ## 🐛Summary When running Llama 4 on Blackwell B200 or H200 nodes (both 4xB200 and 4xH200 configurations) using vLLM versions 0.9.1 and 0.9.2, we encounter incorrect and garbled outputs when processing prompts longer than 10,000 tokens. The model starts producing nonsense or corrupted tokens in its responses. --- ## Environment * **Hardware:** Blackwell B200 & H200 nodes (4xB200 and 4xH200) * **vLLM Version:** 0.9.1 and 0.9.2 * **Model:** meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --- ## Command Used ```bash vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 \ --max-model-len 131072 \ --tokenizer meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 \ --served-model-name meta-llama/Llama-4-Maverick-17B-128E-Instruct \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.9 ``` *Note: Same behavior observed for both vLLM 0.9.1 and 0.9.2 with this serve command, not on 0.8.5* --- ## Steps to Reproduce 1. Start the vLLM server with the command above. 2. Submit a prompt longer than 10,000 tokens. 3. Observe the model’s output degrading into nonsensical or garbled tokens. ## Observations * The problem only occurs with *very long* contexts (promp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ll B200 or H200 nodes (both 4xB200 and 4xH200 configurations) using vLLM versions 0.9.1 and 0.9.2, we encounter incorrect and garbled outputs when processing prompts longer than 10,000 tokens. The model starts producing...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 9.1 and 0.9.2 * **Model:** meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --- ## Command Used ```bash vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 \ --max-model-len 131072 \ --tokenizer meta-llama/Lla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: le ### Your current environment ## 🐛Summary When running Llama 4 on Blackwell B200 or H200 nodes (both 4xB200 and 4xH200 configurations) using vLLM versions 0.9.1 and 0.9.2, we encounter incorrect and garbled outputs wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama 4 Garbled Outputs on long prompts bug;stale ### Your current environment ## 🐛Summary When running Llama 4 on Blackwell B200 or H200 nodes (both 4xB200 and 4xH200 configurations) using vLLM versions 0.9.1 an...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 0.9.1 and 0.9.2 with this serve command, not on 0.8.5* --- ## Steps to Reproduce 1. Start the vLLM server with the command above. 2. Submit a prompt longer than 10,000 tokens. 3. Observe the model’s output degrading int...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
