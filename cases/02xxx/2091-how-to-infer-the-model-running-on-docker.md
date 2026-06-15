# vllm-project/vllm#2091: How to infer the model running on Docker.

| 字段 | 值 |
| --- | --- |
| Issue | [#2091](https://github.com/vllm-project/vllm/issues/2091) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to infer the model running on Docker.

### Issue 正文摘录

Hi, I am running mistral-7B model on vllm docker image by using the following command: docker run --runtime nvidia --gpus all \ -v /model_data:/model_files \ --env "HUGGING_FACE_HUB_TOKEN=" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model mistralai/Mistral-7B-v0.1 and the model is successfully running. Now i want to use Gradio to build a chat interface to infer the mistral model.Can anyone help me on this how to do ?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: How to infer the model running on Docker. Hi, I am running mistral-7B model on vllm docker image by using the following command: docker run --runtime nvidia --gpus all \ -v /model_data:/model_files \ --env "HUGGING_FACE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How to infer the model running on Docker. Hi, I am running mistral-7B model on vllm docker image by using the following command: docker run --runtime nvidia --gpus all \ -v /model_data:/model_files \ --env "HUGGING_FACE...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: HUB_TOKEN=" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model mistralai/Mistral-7B-v0.1 and the model is successfully running. Now i want to use Gradio to build a chat interface to infer the mistral model....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
