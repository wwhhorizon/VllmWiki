# vllm-project/vllm#2460: Run local llm qwen-72b failed

| 字段 | 值 |
| --- | --- |
| Issue | [#2460](https://github.com/vllm-project/vllm/issues/2460) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Run local llm qwen-72b failed

### Issue 正文摘录

When I run local llm qwen-72b-chat, it can`t work normal, it will be stuck like this: ![image](https://github.com/vllm-project/vllm/assets/68416779/dee72595-700a-4085-9a6f-a1527b8f5362) **Command** ``` python -m vllm.entrypoints.openai.api_server --model /mnt/bynas/llms_store/Qwen-72B-Chat --trust-remote-code --tensor-parallel-size 4 --host 0.0.0.0 --port 5000 \ --served-model-name Qwen/Qwen-72B-Chat --gpu-memory-utilization 0.5 ``` **Environment** 4 * Nvidia A6000 48G cuda 12.3 python 3.11

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Run local llm qwen-72b failed When I run local llm qwen-72b-chat, it can`t work normal, it will be stuck like this: ![image](https://github.com/vllm-project/vllm/assets/68416779/dee72595-700a-4085-9a6f-a1527b8f5362) **C...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 12.3 python 3.11 performance distributed_parallel;model_support cuda env_dependency When I run local llm qwen-72b-chat, it can`t work normal, it will be stuck like this:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t --gpu-memory-utilization 0.5 ``` **Environment** 4 * Nvidia A6000 48G cuda 12.3 python 3.11 performance distributed_parallel;model_support cuda env_dependency When I run local llm qwen-72b-chat, it can`t work normal,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
