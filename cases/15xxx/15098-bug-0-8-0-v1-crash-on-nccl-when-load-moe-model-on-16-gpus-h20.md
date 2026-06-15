# vllm-project/vllm#15098: [Bug]: 0.8.0(V1) crash on NCCL when load MoE model on 16 GPUs(H20)

| 字段 | 值 |
| --- | --- |
| Issue | [#15098](https://github.com/vllm-project/vllm/issues/15098) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.8.0(V1) crash on NCCL when load MoE model on 16 GPUs(H20)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run the vLLM 0.8.0 to serving the DeepSeek V3 on 2 nodes with 8 H20 GPUs each. I got the NCCL crash when loading the weights。 Firstly I follow the doc `https://docs.vllm.ai/en/latest/serving/distributed_serving.html` to setup the distributed environment, and then run the api_server as below: ```bash python3 -m vllm.entrypoints.openai.api_server --port 18011 --model /models/DeepSeek-V3 --tensor-parallel-size 16 --gpu-memory-utilization 0.92 --dtype auto --served-model-name deepseekv3 --max-num-seqs 50 --max-model-len 16384 --trust-remote-code --disable-log-requests --enable-chunked-prefill --enable-prefix-caching ``` Then I got the crash error after loading weights ```txt (RayWorkerWrapper pid=246, ip=10.99.48.141) *** SIGSEGV received at time=1742365186 on cpu 33 *** (RayWorkerWrapper pid=246, ip=10.99.48.141) PC: @ 0x7f32d184f03d (unknown) ncclLaunchPrepare() (RayWorkerWrapper pid=246, ip=10.99.48.141) @ 0x7f62fb1b8520 (unknown) (unknown) (RayWorkerWrapper pid=246, ip=10.99.48.141) [2025-03-19 06:19:46,956 E 246 246] logging.cc:484: *** SIGSEGV received at time=1742365186 on cpu 33 *** (RayWorkerWrapper pid=246, ip=10.99....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: yWorkerWrapper pid=246, ip=10.99.48.141) File "/root/.cache/vllm/torch_compile_cache/b992ff727f/rank_11_0/inductor_cache/lv/clvdad54qcohdrhrjm3cmhjc7bqh67lxjou7kqjvfpm33l3lobdr.py", line 487 in call (RayWorkerWrapper pi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: 0.8.0(V1) crash on NCCL when load MoE model on 16 GPUs(H20) bug;stale ### Your current environment ### 🐛 Describe the bug When I run the vLLM 0.8.0 to serving the DeepSeek V3 on 2 nodes with 8 H20 GPUs each. I go...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .48.141) File "/opt/venv/lib/python3.12/site-packages/vllm/compilation/backends.py", line 672 in __call__ (RayWorkerWrapper pid=246, ip=10.99.48.141) File " .66", line 248 in forward (RayWorkerWrapper pid=246, ip=10.99....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /venv/lib/python3.12/site-packages/vllm/distributed/device_communicators/cuda_communicator.py", line 63 in all_reduce (RayWorkerWrapper pid=246, ip=10.99.48.141) File "/opt/venv/lib/python3.12/site-packages/vllm/distrib...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: loading the weights。 Firstly I follow the doc `https://docs.vllm.ai/en/latest/serving/distributed_serving.html` to setup the distributed environment, and then run the api_server as below: ```bash python3 -m vllm.entrypo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
