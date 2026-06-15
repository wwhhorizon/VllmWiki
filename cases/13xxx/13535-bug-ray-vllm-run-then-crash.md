# vllm-project/vllm#13535: [Bug]: Ray+vllm run, then crash

| 字段 | 值 |
| --- | --- |
| Issue | [#13535](https://github.com/vllm-project/vllm/issues/13535) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Ray+vllm run, then crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run `python -m vllm.entrypoints.openai.api_server --disable-custom-all-reduce --gpu-memory-utilization 0.8 --dtype float16 --trust-remote-code --host 0.0.0.0 --served-model-name qwen_coder --tensor-parallel-size 4 --distributed-executor-backend ray --model /root/model/Qwen/Qwen2.5-7B-Instruct/` crash: ``` (RayWorkerWrapper pid=270291, ip=10.175.94.190) [rank3]:[E219 08:58:32.606233339 ProcessGroupNCCL.cpp:616] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=31, OpType=ALLREDUCE, NumelIn=117440512, NumelOut=117440512, Timeout(ms)=600000) ran for 600031 milliseconds before timing out. (RayWorkerWrapper pid=270291, ip=10.175.94.190) [rank3]:[E219 08:58:32.606667496 ProcessGroupNCCL.cpp:1785] [PG ID 2 PG GUID 3 Rank 3] Exception (either an error or timeout) detected by watchdog at work: 31, last enqueued NCCL work: 58, last completed NCCL work: 30. (RayWorkerWrapper pid=270291, ip=10.175.94.190) [rank3]:[E219 08:58:32.606693321 ProcessGroupNCCL.cpp:1834] [PG ID 2 PG GUID 3 Rank 3] Timeout at NCCL work: 31, last enqueued NCCL work: 58, last completed NCCL work: 30. (RayWorkerWrapper pid=270291, ip=10.175.94.190)...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: dom._sfc64, numpy.random._generator, torch._C, torch._C._dynamo.autograd_compiler, torch._C._dynamo.eval_frame, torch._C._dynamo.guards, torch._C._dynamo.utils, torch._C._fft, torch._C._linalg, torch._C._nested, torch._...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ed-model-name qwen_coder --tensor-parallel-size 4 --distributed-executor-backend ray --model /root/model/Qwen/Qwen2.5-7B-Instruct/` crash: ``` (RayWorkerWrapper pid=270291, ip=10.175.94.190) [rank3]:[E219 08:58:32.60623...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lization 0.8 --dtype float16 --trust-remote-code --host 0.0.0.0 --served-model-name qwen_coder --tensor-parallel-size 4 --distributed-executor-backend ray --model /root/model/Qwen/Qwen2.5-7B-Instruct/` crash: ``` (RayWo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ai.api_server --disable-custom-all-reduce --gpu-memory-utilization 0.8 --dtype float16 --trust-remote-code --host 0.0.0.0 --served-model-name qwen_coder --tensor-parallel-size 4 --distributed-executor-backend ray --mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: L operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data. (RayWorkerWrapper pid=270291, ip=10.175.94.190) [rank3]:[E219 08:5...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | -gnu/libc.so.6) (rayworkerwrapper pid=270291, ip=10.175.94.190) frame #4: <unknown function> + 0x126850 (0x7f249b7ae850 in /lib/x86_64-linux-gnu/libc.so.6) (rayworkerwrapper pid=2… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | -gnu/libc.so.6) (rayworkerwrapper pid=270291, ip=10.175.94.190) frame #6: <unknown function> + 0x126850 (0x7f249b7ae850 in /lib/x86_64-linux-gnu/libc.so.6) (rayworkerwrapper pid=2… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
