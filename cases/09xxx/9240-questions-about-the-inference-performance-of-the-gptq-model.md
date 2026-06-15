# vllm-project/vllm#9240: Questions about the inference performance of the GPTQ model

| 字段 | 值 |
| --- | --- |
| Issue | [#9240](https://github.com/vllm-project/vllm/issues/9240) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Questions about the inference performance of the GPTQ model

### Issue 正文摘录

**Why is it that when using a quantitative model for inference, the TTFT optimization is not obvious, but the overall inference efficiency is improved a lot? At the same time, the inference efficiency of gptq marlin is not as good as gptq? What is the reason?** Version Information: vLLM Version: 0.6.2 Start-up Commands: Non-quantized model: `python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 7807 --model /mnt/home/Qwen1.5_32B_Chat --trust-remote-code --served-model-name Qwen --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --enforce-eager --max-model-len 8192 --enable-prefix-caching` Quantized model using GPTQ (without GPTQ Marlin kernel): `python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 7807 --model /mnt/home/Qwen1.5-32B-Chat-GPTQ-Int4 --trust-remote-code --served-model-name Qwen --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --enforce-eager --max-model-len 8192 --enable-prefix-caching --quantization gptq` Quantized model using GPTQ Marlin kernel (automatic mode without specifying --quantization gptq): `python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 7807 --model /mnt/home/Qwen1.5-32B-Chat-GPTQ-Int4 --trust-remo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Questions about the inference performance of the GPTQ model performance;stale **Why is it that when using a quantitative model for inference, the TTFT optimization is not obvious, but the overall inference efficiency is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nce, the TTFT optimization is not obvious, but the overall inference efficiency is improved a lot? At the same time, the inference efficiency of gptq marlin is not as good as gptq? What is the reason?** Version Informat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rmance of the GPTQ model performance;stale **Why is it that when using a quantitative model for inference, the TTFT optimization is not obvious, but the overall inference efficiency is improved a lot? At the same time,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Questions about the inference performance of the GPTQ model performance;stale **Why is it that when using a quantitative model for inference, the TTFT optimization is not obvious, but the overall inference efficiency is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: lel-size 2 --enforce-eager --max-model-len 8192 --enable-prefix-caching` Test Setup: The test script uses 4 concurrent requests with the same prompt for evaluation. Metric Outputs: Non-quantized Model: Time to First Tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
