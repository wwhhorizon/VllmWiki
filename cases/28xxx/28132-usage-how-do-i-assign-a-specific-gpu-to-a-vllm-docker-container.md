# vllm-project/vllm#28132: [Usage]: How do I assign a specific GPU to a vLLM docker container?

| 字段 | 值 |
| --- | --- |
| Issue | [#28132](https://github.com/vllm-project/vllm/issues/28132) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How do I assign a specific GPU to a vLLM docker container?

### Issue 正文摘录

### Your current environment stock vllm-openai:v0.11.0 docker image rootless Docker v.27.5.1 on Ubuntu 22.04.5 LTS on physical hardware Nvidia Driver Version: 570.133.20 CUDA Version: 12.8 GPUs: 4x H100 (NVLink), numbered 0,1,2,3 ### How would you like to use vllm I want to run inference of [SmolLM3-3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B). The exact model doesn't matter, this happens with other models as well. i want to run this model using Docker. This basically works. However, it alway picks a different GPU than what i specify in CUDA_VISIBLE_DEVICES. Out of my four GPUs, 0 and 1 are idle. I would like the container to use GPU 0. But no matter what I try, it always decides to run on GPU 1. I can verify this using `nvtop`. This is my compose file: ```yaml services: vllm-smol: container_name: smollm-3b image: vllm/vllm-openai:v0.11.0 volumes: - ./smollm-3b/models:/models gpus: "all" environment: HF_HOME: "/models" CUDA_VISIBLE_DEVICES: "0" command: > --model HuggingFaceTB/SmolLM3-3B --enable-auto-tool-choice --tool-call-parser=hermes --gpu-memory-utilization 0.1875 labels: ``` This way, the vLLM container starts and inferencing runs fine. But it decides to use GPU 1 i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Usage]: How do I assign a specific GPU to a vLLM docker container? usage ### Your current environment stock vllm-openai:v0.11.0 docker image rootless Docker v.27.5.1 on Ubuntu 22.04.5 LTS on physical hardware Nvidia Dr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: buntu 22.04.5 LTS on physical hardware Nvidia Driver Version: 570.133.20 CUDA Version: 12.8 GPUs: 4x H100 (NVLink), numbered 0,1,2,3 ### How would you like to use vllm I want to run inference of [SmolLM3-3B](https://hug...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ld you like to use vllm I want to run inference of [SmolLM3-3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B). The exact model doesn't matter, this happens with other models as well. i want to run this model using Do...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;model_support cuda env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
