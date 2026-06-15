# vllm-project/vllm#7011: [Bug] [ROCm]: ROCm fails to stop generating tokens on multiple GPTQ models

| 字段 | 值 |
| --- | --- |
| Issue | [#7011](https://github.com/vllm-project/vllm/issues/7011) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [ROCm]: ROCm fails to stop generating tokens on multiple GPTQ models

### Issue 正文摘录

### Your current environment [My Environment](https://github.com/vllm-project/vllm/files/14937936/env.txt) OpenAI API launched using this command: ``` VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_NCCL_SO_PATH=/opt/rocm/lib/librccl.so.1 python -m vllm.entrypoints.openai.api_server --gpu-memory-utilization 0.7 --tensor-parallel-size 4 --model --enforce-eager --swap-space 0 --port 5000 --quantization gptq --max-model-length 32768 --dtype half was used for Llama models --chat-template was used for Command-R models ``` Docker launched using this command: ``` sudo docker run -it --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device /dev/kfd --device /dev/dri -v :/vllm-workspace/model vllm: bash ``` ### 🐛 Describe the bug When loading these models [Command R Plus](https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ) [Llama 3.1 70B](https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4) [Llama 3.1 70B Alternate](https://huggingface.co/ModelCloud/Meta-Llama-3.1-70B-Instruct-gptq-4bit) using a docker image built from source as of 2024-07-24, every prompt continues to generate until (i assume) hitting the token limi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed for Llama models --chat-template was used for Command-R models ``` Docker launched using this command: ``` sudo docker run -it --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=u...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: r-parallel-size 4 --model --enforce-eager --swap-space 0 --port 5000 --quantization gptq --max-model-length 32768 --dtype half was used for Llama models --chat-template was used for Command-R models ``` Docker launched...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] [ROCm]: ROCm fails to stop generating tokens on multiple GPTQ models bug;stale ### Your current environment [My Environment](https://github.com/vllm-project/vllm/files/14937936/env.txt) OpenAI API launched using t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug] [ROCm]: ROCm fails to stop generating tokens on multiple GPTQ models bug;stale ### Your current environment [My Environment](https://github.com/vllm-project/vllm/files/14937936/env.txt) OpenAI API launched using t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [ROCm]: ROCm fails to stop generating tokens on multiple GPTQ models bug;stale ### Your current environment [My Environment](https://github.com/vllm-project/vllm/files/14937936/env.txt) OpenAI API launched using this co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
