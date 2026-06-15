# vllm-project/vllm#894: High latency when using llama-2-13b-chat-hf on AWS Sagemaker

| 字段 | 值 |
| --- | --- |
| Issue | [#894](https://github.com/vllm-project/vllm/issues/894) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> High latency when using llama-2-13b-chat-hf on AWS Sagemaker

### Issue 正文摘录

Hi Team, I am using `meta-llama/Llama-2-13b-chat-hf` with `tensor_parallel_size=4` on AWS Sagemaker notebook instance with `ml.g5.12xlarge` which has 4 NVIDIA A10G GPUs 23 GB memory each. With recent release it's taking longer time to generate the text. Here is the screenshot with the environment: ![image](https://github.com/vllm-project/vllm/assets/12952169/5178d59d-d1d9-4506-b932-ae5edef44b96) Here is the screenshot with prompt and timing and GPU consumption once I instantiated the model: ![image](https://github.com/vllm-project/vllm/assets/12952169/e06ae7c8-1cae-4515-a8ea-5617c1cca8e8) It took **41.6 seconds** which is way slow. I have tested earlier it's done within seconds. However, if I try it with `tensor_parallel_size=2`, the response time reduces to half around **`20.2 seconds`**. ![image](https://github.com/vllm-project/vllm/assets/12952169/27e16eca-85d9-46f7-b0fa-8a0c5816c777) I feel that something is weird happening with parallelization. Please help me fix this issue. Regards Priyanshu Sinha @WoosukKwon

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: High latency when using llama-2-13b-chat-hf on AWS Sagemaker Hi Team, I am using `meta-llama/Llama-2-13b-chat-hf` with `tensor_parallel_size=4` on AWS Sagemaker notebook instance with `ml.g5.12xlarge` which has 4 NVIDIA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: High latency when using llama-2-13b-chat-hf on AWS Sagemaker Hi Team, I am using `meta-llama/Llama-2-13b-chat-hf` with `tensor_parallel_size=4` on AWS Sagemaker notebook instance with `ml.g5.12xlarge` which has 4 NVIDIA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
