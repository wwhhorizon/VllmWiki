# vllm-project/vllm#7867: [Usage]: deploy qwen1.5-0.5B using docker

| 字段 | 值 |
| --- | --- |
| Issue | [#7867](https://github.com/vllm-project/vllm/issues/7867) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: deploy qwen1.5-0.5B using docker

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm docker run --runtime nvidia --gpus all \ -p 8002:8002 \ --ipc=host \ --name vllm_ch_test \ vllm/vllm-openai:latest \ --model ./checkpoint-300 checkpoint-300 folder: error: the checkpoint_300 folder is generated using ms-swift finetune ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: deploy qwen1.5-0.5B using docker usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm docker run --runtime nvidia --gpus all \ -p 8002:8002 \ -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: deploy qwen1.5-0.5B using docker usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm docker run --runtime nvidia --gpus all \ -p 8002:8002 \ -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: idia --gpus all \ -p 8002:8002 \ --ipc=host \ --name vllm_ch_test \ vllm/vllm-openai:latest \ --model ./checkpoint-300 checkpoint-300 folder: error: the checkpoint_300 folder is generated using ms-swift finetune ### Bef...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
