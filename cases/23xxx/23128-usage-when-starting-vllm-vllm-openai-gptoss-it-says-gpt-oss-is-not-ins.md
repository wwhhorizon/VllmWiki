# vllm-project/vllm#23128: [Usage]: When starting vllm/vllm-openai:gptoss it says gpt_oss is not installed

| 字段 | 值 |
| --- | --- |
| Issue | [#23128](https://github.com/vllm-project/vllm/issues/23128) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: When starting vllm/vllm-openai:gptoss it says gpt_oss is not installed

### Issue 正文摘录

### Your current environment When starting docker to run **openai/gpt-oss-20b** as below, I get the following warnings and can't use websearch or code interpreter ``` (APIServer pid=1) WARNING 08-18 11:42:46 [tool.py:38] gpt_oss is not installed, browsing is disabled (APIServer pid=1) WARNING 08-18 11:42:46 [tool.py:69] gpt_oss is not installed, code interpreter is disabled ```` I inspected the docker and can see it is installed: ``` $ pip list | grep oss gpt-oss 0.1.0 vllm 0.10.1+gptoss ``` ``` docker run \ --env VLLM_USE_V1=1 \ --gpus all \ --ipc=host \ -p "8000:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 \ --env TORCH_CUDA_ARCH_LIST=8.9 \ --env TORCH_COMPILE_DISABLE=0 \ --env EXA_API_KEY=EXA_KEY \ -v /root/.cache/huggingface:/root/.cache/huggingface \ vllm/vllm-openai:gptoss \ --tool-server demo \ --model openai/gpt-oss-20b \ --async-scheduling \ --max-model-len 131072 \ --gpu-memory-utilization 0.95 \ --max-num-batched-tokens 1024 ``` ### How would you like to use vllm I want to run inference of a [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) and use code interpreter and web search in the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: When starting vllm/vllm-openai:gptoss it says gpt_oss is not installed usage;stale ### Your current environment When starting docker to run **openai/gpt-oss-20b** as below, I get the following warnings and can'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: stale ### Your current environment When starting docker to run **openai/gpt-oss-20b** as below, I get the following warnings and can't use websearch or code interpreter ``` (APIServer pid=1) WARNING 08-18 11:42:46 [tool...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 \ --env TORCH_CUDA_ARCH_LIST=8.9 \ --env TORCH_COMPILE_DISABLE=0 \ --env EXA_API_KEY=EXA_KEY \ -v /root/.cache/hugging...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /gpt-oss-20b** as below, I get the following warnings and can't use websearch or code interpreter ``` (APIServer pid=1) WARNING 08-18 11:42:46 [tool.py:38] gpt_oss is not installed, browsing is disabled (APIServer pid=1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: starting vllm/vllm-openai:gptoss it says gpt_oss is not installed usage;stale ### Your current environment When starting docker to run **openai/gpt-oss-20b** as below, I get the following warnings and can't use websearc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
