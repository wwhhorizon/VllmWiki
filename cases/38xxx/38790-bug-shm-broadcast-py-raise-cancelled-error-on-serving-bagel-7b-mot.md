# vllm-project/vllm#38790: [Bug]: shm_broadcast.py raise cancelled error on serving BAGEL-7B-MoT

| 字段 | 值 |
| --- | --- |
| Issue | [#38790](https://github.com/vllm-project/vllm/issues/38790) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: shm_broadcast.py raise cancelled error on serving BAGEL-7B-MoT

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug shm_broadcast.py raise 'cancelled' error on serving BAGEL-7B-MoT **Reproduce Steps:** ``` vllm serve --omni ByteDance-Seed/BAGEL-7B-MoT ``` **Errors:** ``` (Worker pid=117944) INFO 04-02 06:20:51 [gpu_model_runner.py:4481] Starting to load model /nvme4n1/models/ByteDance-Seed/BAGEL-7B-MoT... (Worker pid=117944) INFO 04-02 06:20:52 [vllm.py:775] Asynchronous scheduling is enabled. (Worker pid=117944) WARNING 04-02 06:20:52 [vllm.py:809] Enforce eager set, disabling torch.compile and CUDAGraphs. This is equivalent to setting -cc.mode=none -cc.cudagraph_mode=none (Worker pid=117944) WARNING 04-02 06:20:52 [vllm.py:820] Inductor compilation was disabled by user settings, optimizations settings that are only active during inductor compilation will be ignored. (Worker pid=117944) INFO 04-02 06:20:52 [vllm.py:985] Cudagraph is disabled under eager mode (Worker pid=117944) INFO 04-02 06:20:52 [compilation.py:289] Enabled custom fusions: norm_quant, act_quant (Worker pid=117944) INFO 04-02 06:20:56 [cuda.py:317] Using TRITON_ATTN attention backend out of potential backends: ['TRITON_ATTN', 'FLEX_ATTENTION']. (Worker pid=117944) WARNING 04...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: oderAttention. ERROR 04-02 06:21:17 [kv_transfer_manager.py:426] Timeout waiting for KV cache for request dummy_req_id after 30.0s Loading safetensors checkpoint shards: 0% Completed | 0/2 [00:00<?, ?it/s] Loading safet...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: WARNING 04-02 06:20:52 [vllm.py:809] Enforce eager set, disabling torch.compile and CUDAGraphs. This is equivalent to setting -cc.mode=none -cc.cudagraph_mode=none (Worker pid=117944) WARNING 04-02 06:20:52 [vllm.py:820...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 7B-MoT ``` **Errors:** ``` (Worker pid=117944) INFO 04-02 06:20:51 [gpu_model_runner.py:4481] Starting to load model /nvme4n1/models/ByteDance-Seed/BAGEL-7B-MoT... (Worker pid=117944) INFO 04-02 06:20:52 [vllm.py:775] A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: t, act_quant (Worker pid=117944) INFO 04-02 06:20:56 [cuda.py:317] Using TRITON_ATTN attention backend out of potential backends: ['TRITON_ATTN', 'FLEX_ATTENTION']. (Worker pid=117944) WARNING 04-02 06:21:02 [bagel.py:3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 88] Encoder cache will be initialized with a budget of 32768 tokens, and profiled with 3 img2img items of the maximum feature size. INFO 04-02 06:21:32 [diffusion_model_runner.py:212] Peak GPU memory (this request): 30....

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
