# vllm-project/vllm#12233: [Bug]: RuntimeError: Error in model execution: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#12233](https://github.com/vllm-project/vllm/issues/12233) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Error in model execution: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I started 4 vllm Docker containers and set up NGINX as a load balancer, following [this](https://docs.vllm.ai/en/latest/deployment/nginx.html) guide. Under high load, one of the containers crashed. This also occurred when I deployed a single container on 2 GPUs. I searched for solutions, but I couldn’t find any. Most users experience this issue when deploying the Qwen model (AWQ) (#10389 , #11366, #), but I don’t think that’s the problem in my case. Since my container stopped and was removed, I was unable to provide the .pkl file. Here is the full log: ``` INFO 01-20 18:39:36 metrics.py:467] Avg prompt throughput: 2411.0 tokens/s, Avg generation throughput: 247.2 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.4%, CPU KV cache usage: 0.0%. INFO 01-20 18:39:36 metrics.py:483] Prefix cache hit rate: GPU: 79.73%, CPU: 0.00% INFO: 172.27.0.4:41468 - "POST /v1/chat/completions HTTP/1.0" 200 OK INFO: 172.27.0.4:41454 - "POST /v1/chat/completions HTTP/1.0" 200 OK INFO: 172.27.0.4:41502 - "POST /v1/chat/completions HTTP/1.0" 200 OK INFO 01-20 18:39:37 model_runner_bas...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: del Input Dumps _No response_ ### 🐛 Describe the bug I started 4 vllm Docker containers and set up NGINX as a load balancer, following [this](https://docs.vllm.ai/en/latest/deployment/nginx.html) guide. Under high load,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: RuntimeError: Error in model execution: CUDA error: an illegal memory access was encountered bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I started 4 vllm Docker con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: y", line 196, in run_engine_loop ERROR 01-20 18:39:37 engine.py:135] request_outputs = self.engine_step() ERROR 01-20 18:39:37 engine.py:135] ^^^^^^^^^^^^^^^^^^ ERROR 01-20 18:39:37 engine.py:135] File "/usr/local/lib/p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG ID 2 PG GUID 3 Rank 0] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: Error in model execution: CUDA error: an illegal memory access was encountered bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I started 4 vllm Docker con...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 0x94ac3 (0x7a6875a2bac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #4: <unknown function> + 0x126850 (0x7a6875abd850 in /usr/lib/x86_64-linux-gnu/libc.so.6) error 01-22 00:13:32 |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7a682a82c61d in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0x145c0 (0x7a68751d95c0 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorc… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
