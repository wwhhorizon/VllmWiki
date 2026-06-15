# vllm-project/vllm#30941: [Performance]: Why Does Latency Remain Unchanged in vLLM 0.11.0 When Input Token Count Decreases for qwen3-vl-30b-a3b?

| 字段 | 值 |
| --- | --- |
| Issue | [#30941](https://github.com/vllm-project/vllm/issues/30941) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Why Does Latency Remain Unchanged in vLLM 0.11.0 When Input Token Count Decreases for qwen3-vl-30b-a3b?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Using vLLM version 0.11.0 to run the qwen3-vl-30b-a3b model, the stress test results show that although the number of input tokens decreases, the latency does not change. The model is deployed on a single A800 GPU. The startup command is: vllm server --dtype bfloat16 --max-model-len 128000 --gpu-memory-utilization 0.95 --limit-mm-per-prompt.video 0 I performed a stress test using one image and a set of text prompts, with QPS set to 10. I resized the image to 0.25x and 0.7x of the original size while keeping everything else unchanged. The conclusions are as follows: qwen3-30b-a3b (single image *0.25) latency 3s qwen3-30b-a3b (single image *0.7) latency 5s qwen3-30b-a3b (single image) latency 5s Prior conditions: Input token scale / Output token scale Single image + text prompts: about 4200 / about 70 Single image *0.6 + text prompts: about 1900 / about 70 Single image *0.3 + text prompts: about 860 / about 70 ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new iss...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: is deployed on a single A800 GPU. The startup command is: vllm server --dtype bfloat16 --max-model-len 128000 --gpu-memory-utilization 0.95 --limit-mm-per-prompt.video 0 I performed a stress test using one image and a s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Why Does Latency Remain Unchanged in vLLM 0.11.0 When Input Token Count Decreases for qwen3-vl-30b-a3b? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regres...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ncy Remain Unchanged in vLLM 0.11.0 When Input Token Count Decreases for qwen3-vl-30b-a3b? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: egression _No response_ ### Misc discussion on performance Using vLLM version 0.11.0 to run the qwen3-vl-30b-a3b model, the stress test results show that although the number of input tokens decreases, the latency does n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
