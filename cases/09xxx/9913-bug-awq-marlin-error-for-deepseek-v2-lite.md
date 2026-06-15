# vllm-project/vllm#9913: [Bug]: awq marlin error for deepseek v2 lite

| 字段 | 值 |
| --- | --- |
| Issue | [#9913](https://github.com/vllm-project/vllm/issues/9913) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: awq marlin error for deepseek v2 lite

### Issue 正文摘录

### Your current environment vllm==0.6.3.post1 ### Model Input Dumps ```bash ValueError: Weight input_size_per_partition = 10944 is not divisible by min_thread_k = 128. Consider reducing tensor_parallel_size or running with --quantization gptq. ``` ### 🐛 Describe the bug When I run the command on one gpu: ```bash python -m vllm.entrypoints.openai.api_server --port 10086 --model TechxGenus/DeepSeek-Coder-V2-Lite-Instruct-AWQ --dtype float16 --gpu-memory-utilization 0.8 --max-model-len 8192 --enable-prefix-caching --disable-log-requests --trust-remote-code --enforce-eager ``` It raise the error: ``` ValueError: Weight input_size_per_partition = 10944 is not divisible by min_thread_k = 128. Consider reducing tensor_parallel_size or running with --quantization gptq. ``` Then I try to change the configuration of marlin kernel at https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/utils/marlin_utils.py#L14: ```diff -GPTQ_MARLIN_MIN_THREAD_K = 128 +GPTQ_MARLIN_MIN_THREAD_K = 64 ``` It run successfully, and the output also looks well. Will this have any other impact on the marlin kernel? If there is no other impact, I hope this change can be applied to s...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: thread_k = 128. Consider reducing tensor_parallel_size or running with --quantization gptq. ``` ### 🐛 Describe the bug When I run the command on one gpu: ```bash python -m vllm.entrypoints.openai.api_server --port 10086...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: k v2 lite bug;stale ### Your current environment vllm==0.6.3.post1 ### Model Input Dumps ```bash ValueError: Weight input_size_per_partition = 10944 is not divisible by min_thread_k = 128. Consider reducing tensor_paral...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: awq marlin error for deepseek v2 lite bug;stale ### Your current environment vllm==0.6.3.post1 ### Model Input Dumps ```bash ValueError: Weight input_size_per_partition = 10944 is not divisible by min_thread_k =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r_partition = 10944 is not divisible by min_thread_k = 128. Consider reducing tensor_parallel_size or running with --quantization gptq. ``` ### 🐛 Describe the bug When I run the command on one gpu: ```bash python -m vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
