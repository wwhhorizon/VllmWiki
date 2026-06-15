# vllm-project/vllm#2304: Mistral 7B takes up 69GB of vRAM on A100

| 字段 | 值 |
| --- | --- |
| Issue | [#2304](https://github.com/vllm-project/vllm/issues/2304) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mistral 7B takes up 69GB of vRAM on A100

### Issue 正文摘录

I'm trying to run multiple instances of Mistral 7B on a A100 GPU. However it seems to be taking up 69GBs of vRAM on the A100. Command i'm using to run `@4xa100-node:~$ sudo docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model mistralai/Mistral-7B-v0.1` Output ![image](https://github.com/vllm-project/vllm/assets/34645607/c3e69e40-ecd3-4b11-9c2b-85027daf6a51) What seems to be the issue? Am i doing something wrong?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a100-node:~$ sudo docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model mistralai/Mistral-7B-v0.1` Output ![image](https://github...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: GBs of vRAM on the A100. Command i'm using to run `@4xa100-node:~$ sudo docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model mis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Mistral 7B takes up 69GB of vRAM on A100 I'm trying to run multiple instances of Mistral 7B on a A100 GPU. However it seems to be taking up 69GBs of vRAM on the A100. Command i'm using to run `@4xa100-node:~$ sudo docke...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model mistralai/Mistral-7B-v0.1` Output ![image](https://github.com/vllm-project/vllm/assets/34645607/c3e69e40-ecd3-4b11-9c2b-85027daf6a51) What seems...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
