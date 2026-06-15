# vllm-project/vllm#19415: [Bug]: [V1][gpu_model_runner.py] CUDA memory error

| 字段 | 值 |
| --- | --- |
| Issue | [#19415](https://github.com/vllm-project/vllm/issues/19415) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [V1][gpu_model_runner.py] CUDA memory error

### Issue 正文摘录

### Your current environment I am using vllm docker image: docker pull vllm/vllm-openai:v0.9.1rc1 ### 🐛 Describe the bug Hi, I am making some changes to vllm/v1/worker/gpu_model_runner.py and trying to initialize some custom tensors inside the GPUModelRunner class. Specifically, I have added the following code: ```python self.query_first_loc = torch.zeros(self.max_num_reqs + 1, dtype=torch.int32, device=self.device) self.query_second_loc = torch.zeros(self.max_num_reqs + 1, dtype=torch.int32, device=self.device) self.seq_lens_first = torch.zeros(self.max_num_reqs, dtype=torch.int32, device=self.device) self.seq_lens_second = torch.zeros(self.max_num_reqs, dtype=torch.int32, device=self.device) ``` However, I am encountering the following error at runtime: ``` (VllmWorker rank=0 pid=76227) [rank2]:[W610 03:20:31.540991085 TCPStore.cpp:125] [c10d] recvValue failed on SocketImpl(fd=176, addr=[localhost]:45008, remote=[localhost]:60771): failed to recv, got 0 bytes Exception raised from recvBytes at /pytorch/torch/csrc/distributed/c10d/Utils.hpp:678 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string , std::allocator >) + 0x98 (0x7fff5...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: UDA memory error bug;stale ### Your current environment I am using vllm docker image: docker pull vllm/vllm-openai:v0.9.1rc1 ### 🐛 Describe the bug Hi, I am making some changes to vllm/v1/worker/gpu_model_runner.py and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: [V1][gpu_model_runner.py] CUDA memory error bug;stale ### Your current environment I am using vllm docker image: docker pull vllm/vllm-openai:v0.9.1rc1 ### 🐛 Describe the bug Hi, I am making some changes to vllm/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [V1][gpu_model_runner.py] CUDA memory error bug;stale ### Your current environment I am using vllm docker image: docker pull vllm/vllm-openai:v0.9.1rc1 ### 🐛 Describe the bug Hi, I am making some changes to vllm/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: [V1][gpu_model_runner.py] CUDA memory error bug;stale ### Your current environment I am using vllm docker image: docker pull vllm/vllm-openai:v0.9.1rc1 ### 🐛 Describe the bug Hi, I am making some changes to vllm/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _parallel;frontend_api;scheduler_memory cuda dtype;env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation Your curre...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | r/local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x7ffff5079253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | xdc253 (0x7ffff5079253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x7ffff7ceaac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown funct… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
