# vllm-project/vllm#5634: [Usage]: I want to know how to use argument "--max-num-seqs".

| 字段 | 值 |
| --- | --- |
| Issue | [#5634](https://github.com/vllm-project/vllm/issues/5634) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: I want to know how to use argument "--max-num-seqs".

### Issue 正文摘录

### Your current environment ```text Versions of relevant libraries: [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.40.2 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0 pypi_0 pypi [conda] transformers 4.40.2 pypi_0 pypi [conda] triton 2.3.0 pypi_0 pypi [conda] vllm-nccl-cu12 2.18.1.0.4.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.2 I run the llama3-8b model on 2*A100s. ``` Hello! I am utilizing vLLM OpenAI-Compatible RESTful API server. I understand that argument "--max-num-seqs" means the sequences that the API server can process simultaneously. Changing it to 2 will process two requests at the same time, and the third request will be delayed. However, if I set the value to 256 (default) or a value higher than 6, it does not work. Did I understand something wrong? Even if GPU usage is reduced through --max-model-len or --gpu-memory-utilization, the same issue persists. Respectfully ### How would you like to use vllm I want to run inference of a [specific...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e argument "--max-num-seqs". usage ### Your current environment ```text Versions of relevant libraries: [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] trans...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: conda] vllm-nccl-cu12 2.18.1.0.4.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.2 I run the llama3-8b model on 2*A100s. ``` Hello! I am utilizing vLLM OpenAI-Compatible RESTful...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.2 I run the llama3-8b model on 2*A100s. ``` Hello! I am utilizing vLLM OpenAI-Compatible RESTful API server. I understand that argument "--max-num-seqs" means...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.40.2 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: I server can process simultaneously. Changing it to 2 will process two requests at the same time, and the third request will be delayed. However, if I set the value to 256 (default) or a value higher than 6, it does not...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
