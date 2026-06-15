# vllm-project/vllm#7951: [Bug]: Mi300x x8 unable to lauch openai/api_server.py on rocm vllm branch.

| 字段 | 值 |
| --- | --- |
| Issue | [#7951](https://github.com/vllm-project/vllm/issues/7951) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mi300x x8 unable to lauch openai/api_server.py on rocm vllm branch.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run it with the last version of the vllm rocm ( https://github.com/ROCm/vllm ) torchrun --standalone --nnodes=1 --nproc_per_node=8 ./vllm/vllm/entrypoints/openai/api_server.py --model Meta-Llama-3.1-405B-Instruct --port 8010 I got: File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/utils/_device.py", line 77, in __torch_function__ return func(*args, **kwargs) torch.cuda.OutOfMemoryError: HIP out of memory. Tried to allocate 3.25 GiB. GPU 0 has a total capacity of 191.98 GiB of which 1.32 GiB is free. Of the allocated memory 5.01 GiB is allocated by PyTorch, and 0 bytes is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_HIP_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables) INFO 08-28 11:24:09 selector.py:56] Using ROCmFlashAttention backend. I used the docker from yesterday. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documenta...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Mi300x x8 unable to lauch openai/api_server.py on rocm vllm branch. bug;rocm ### Your current environment ### 🐛 Describe the bug When I run it with the last version of the vllm rocm ( https://github.com/ROCm/vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rent environment ### 🐛 Describe the bug When I run it with the last version of the vllm rocm ( https://github.com/ROCm/vllm ) torchrun --standalone --nnodes=1 --nproc_per_node=8 ./vllm/vllm/entrypoints/openai/api_server...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tml#environment-variables) INFO 08-28 11:24:09 selector.py:56] Using ROCmFlashAttention backend. I used the docker from yesterday. ### Before submitting a new issue... - [X] Make sure you already searched for relevant i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: odes=1 --nproc_per_node=8 ./vllm/vllm/entrypoints/openai/api_server.py --model Meta-Llama-3.1-405B-Instruct --port 8010 I got: File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/utils/_device.py", line 77, i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ons. correctness ci_build;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
