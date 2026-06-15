# vllm-project/vllm#8444: [Bug]: GPU can only load the model once, it gets stuck when loaded again

| 字段 | 值 |
| --- | --- |
| Issue | [#8444](https://github.com/vllm-project/vllm/issues/8444) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: GPU can only load the model once, it gets stuck when loaded again

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After every reboot of my GPU machine， 1. The NCCL test script on the official website [Getting Started/Debugging Tips] was successful when running. 2. Running scripts in the conda virtual environment ```bash python -m vllm.entrypoints.openai.api_server --model /data1/xinference/modelscope/hub/qwen/Qwen2-72B-Instruct-GPTQ-Int4 --served-model-name qwen2-72b --tensor-parallel-size 4 ``` Or run the container in Docker ```bash docker run --gpus all --name vllm \ -v /data1/xinference/modelscope:/root/model \ -v /data1/vllm:/root/vllm \ -p 8880:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model /root/model/hub/qwen/Qwen2-72B-Instruct-GPTQ-Int4 \ --gpu-memory-utilization 0.8 \ --tensor-parallel-size 4 \ --max-model-len 8129 \ --served-model-name Qwen2-72b-instruct ``` All of them are successful. 3. After exiting the running model, or exiting the Docker container, closing the container, or even shutting down the Docker service, when I want to run the script in the conda virtual environment or Docker as in the step 2 above, the model cannot load and the program get stuck. Among them, the console outpu...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: ]: GPU can only load the model once, it gets stuck when loaded again bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After every reboot of my GPU machine， 1. The NCCL te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: After every reboot of my GPU machine， 1. The NCCL test script on the official website [Getting Started/Debugging Tips] was successful when running. 2. Running scripts in the conda virtual environment ```bash python -m v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: er --model /data1/xinference/modelscope/hub/qwen/Qwen2-72B-Instruct-GPTQ-Int4 --served-model-name qwen2-72b --tensor-parallel-size 4 ``` Or run the container in Docker ```bash docker run --gpus all --name vllm \ -v /dat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: -p 8880:8000 \ -e VLLM_LOGGING_LEVEL=DEBUG \ -e CUDA_LAUNCH_BLOCKING=1 \ -e NCCL_DEBUG=TRACE \ -e VLLM_TRACE_FUNCTION=1 \ --ipc=host \ vllm/vllm-openai:latest \ --model /root/model/hub/qwen/Qwen2-72B-Instruct-GPTQ-Int4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: GPU can only load the model once, it gets stuck when loaded again bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After every reboot of my GPU machine， 1. The NCC...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | lmenv/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xdbbf4 (0x7f1f870dbbf4 in /usr/local/miniconda3/envs/vllmenv/bin/../lib/libstdc++.so… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | x9ca94 (0x7f1f8909ca94 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #6: <unknown function> + 0x129c3c (0x7f1f89129c3c in /usr/lib/x86_64-linux-gnu/libc.so.6) w0913 05:31:49.5620 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
