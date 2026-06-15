# vllm-project/vllm#12346: [Usage]:  Why does it consume so much memory?

| 字段 | 值 |
| --- | --- |
| Issue | [#12346](https://github.com/vllm-project/vllm/issues/12346) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Why does it consume so much memory?

### Issue 正文摘录

### Your current environment Jetson Orin NX 16G jetpack 6.2 docker： [dustynv/vllm:0.6.3-r36.4.0](https://hub.docker.com/r/dustynv/vllm/tags) llm = LLM(model="./Qwen2-7B-Instruct.Q4_K_M.gguf",max_model_len = 200,max_num_seqs=1) Consume more than 16G of memory and terminate: INFO 01-23 07:32:01 model_runner.py:1060] Starting to load model ./Qwen2-7B-Instruct.Q4_K_M.gguf... /usr/local/lib/python3.10/dist-packages/torch/nested/__init__.py:226: UserWarning: The PyTorch API of nested tensors is in prototype stage and will change in the near future. (Triggered internally at /opt/pytorch/aten/src/ATen/NestedTensorImpl.cpp:178.) return _nested.nested_tensor( INFO 01-23 07:32:42 model_runner.py:1071] Loading model weights took 4.3752 GB INFO 01-23 07:34:26 gpu_executor.py:122] # GPU blocks: 11836, # CPU blocks: 4681 INFO 01-23 07:34:26 gpu_executor.py:126] Maximum concurrency for 200 tokens per request: 946.88x Killed ![Image](https://github.com/user-attachments/assets/a293e6ea-eae0-48a1-9713-18dbebe62b98) By ollama , I can run qwen2.5-7b on the same device. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: usage;stale ### Your current environment Jetson Orin NX 16G jetpack 6.2 docker： [dustynv/vllm:0.6.3-r36.4.0](https://hub.docker.com/r/dustynv/vllm/tags) llm = LLM(model="./Qwen2-7B-Instruct.Q4_K_M.gguf",max_model_len =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm:0.6.3-r36.4.0](https://hub.docker.com/r/dustynv/vllm/tags) llm = LLM(model="./Qwen2-7B-Instruct.Q4_K_M.gguf",max_model_len = 200,max_num_seqs=1) Consume more than 16G of memory and terminate: INFO 01-23 07:32:01 mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Why does it consume so much memory? usage;stale ### Your current environment Jetson Orin NX 16G jetpack 6.2 docker： [dustynv/vllm:0.6.3-r36.4.0](https://hub.docker.com/r/dustynv/vllm/tags) llm = LLM(model="./Qw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: el weights took 4.3752 GB INFO 01-23 07:34:26 gpu_executor.py:122] # GPU blocks: 11836, # CPU blocks: 4681 INFO 01-23 07:34:26 gpu_executor.py:126] Maximum concurrency for 200 tokens per request: 946.88x Killed ![Image]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
