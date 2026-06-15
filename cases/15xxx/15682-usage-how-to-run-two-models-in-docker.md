# vllm-project/vllm#15682: [Usage]: how to run two models in Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#15682](https://github.com/vllm-project/vllm/issues/15682) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to run two models in Docker

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm docker run --runtime nvidia --gpus all \ -v /home/model-tran/models/DeepSeek-R1-Distill-Qwen-32B/:/models/deepseek-r1-32b \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HF_HUB_OFFLINE=1" \ -p 8000:8000 \ --ipc=host \ -d \ vllm/vllm-openai:latest \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 4 \ --model /models/deepseek-r1-32b I have successfully run my large model, but I want to run two. When I move my model files to my Docker execution directory and use VLLM serve, it prompts that CUDA is insufficient (my GPU has a total of 4, 160g. The other model is DeepSEEK-R1-1.5b). I tried switching to Docker to start both models ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: how to run two models in Docker usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm docker run --runtime nvidia --gpus all \ -v /home/model-tr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: how to run two models in Docker usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm docker run --runtime nvidia --gpus all \ -v /home/model-tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: les to my Docker execution directory and use VLLM serve, it prompts that CUDA is insufficient (my GPU has a total of 4, 160g. The other model is DeepSEEK-R1-1.5b). I tried switching to Docker to start both models ### Be...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 1" \ -p 8000:8000 \ --ipc=host \ -d \ vllm/vllm-openai:latest \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 4 \ --model /models/deepseek-r1-32b I have successfully run my large model, but I want to run two. Wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
