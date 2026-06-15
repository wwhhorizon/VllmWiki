# vllm-project/vllm#8105: [Usage]: Can vLLM handle multi-turn and multi-instance at the same time?

| 字段 | 值 |
| --- | --- |
| Issue | [#8105](https://github.com/vllm-project/vllm/issues/8105) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Can vLLM handle multi-turn and multi-instance at the same time?

### Issue 正文摘录

### Environment Details: - OS: CentOS Linux 7 (Core) (x86_64) - GPU: Nvidia Quadro RTX 6000 - Pytorch Version: 2.4.0 - CUDA Version: 12.1 I'm currently serving my model with a provided docker image to enable multi instance using below command ``` docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN={hf_token}" \ --network host \ --ipc=host \ --name vllm_container \ vllm/vllm-openai:latest \ --model maywell/Llama-3-Ko-8B-Instruct \ --host 0.0.0.0 \ --port 8000 \ --dtype half \ --enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --served-model-name llama3 ``` The problem is although I enabled APC with `enable-prefix-caching` and eager mode with `enforce-eager` the vllm keeps forgetting what I said. So, here's the question. how can I enable multi-turn and multi-instance at the same time? I mean Is there any way to pass the user_id and make model to remember what's been said by whom? I don't want to pass the whole chat history because It costs too much resouces and vllm internally supports APC feature. It would be great if I could get the example code or command. Thank you.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: : CentOS Linux 7 (Core) (x86_64) - GPU: Nvidia Quadro RTX 6000 - Pytorch Version: 2.4.0 - CUDA Version: 12.1 I'm currently serving my model with a provided docker image to enable multi instance using below command ``` d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: - Pytorch Version: 2.4.0 - CUDA Version: 12.1 I'm currently serving my model with a provided docker image to enable multi instance using below command ``` docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nment Details: - OS: CentOS Linux 7 (Core) (x86_64) - GPU: Nvidia Quadro RTX 6000 - Pytorch Version: 2.4.0 - CUDA Version: 12.1 I'm currently serving my model with a provided docker image to enable multi instance using...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ll/Llama-3-Ko-8B-Instruct \ --host 0.0.0.0 \ --port 8000 \ --dtype half \ --enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --served-model-name llama3 ``` The problem is although I enabled APC with `enable-prefix...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Can vLLM handle multi-turn and multi-instance at the same time? usage;stale ### Environment Details: - OS: CentOS Linux 7 (Core) (x86_64) - GPU: Nvidia Quadro RTX 6000 - Pytorch Version: 2.4.0 - CUDA Version: 12.1 I'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
