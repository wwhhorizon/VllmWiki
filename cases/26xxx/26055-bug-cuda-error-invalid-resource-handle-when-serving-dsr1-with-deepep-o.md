# vllm-project/vllm#26055: [Bug]: CUDA error "invalid resource handle" when serving dsr1 with deepep on GB200

| 字段 | 值 |
| --- | --- |
| Issue | [#26055](https://github.com/vllm-project/vllm/issues/26055) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error "invalid resource handle" when serving dsr1 with deepep on GB200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving deepseek r1 model on GB200 using the deepep flags on 2 nodes, a cuda error occurs. I used the default deepgemm commit from vllm, and also tried to upgrade the deepgemm commit to `59495`, but still seeing the same cuda error. Commands to reproduce: ```bash # node 0 VLLM_ALL2ALL_BACKEND=deepep_low_latency VLLM_USE_DEEP_GEMM=1 VLLM_RANDOMIZE_DP_DUMMY_INPUTS=1 \ vllm serve deepseek-ai/DeepSeek-R1 --served-model-name deepseek-r1 --tensor-parallel-size 1 \ --enable-expert-parallel --data-parallel-size 8 --data-parallel-size-local 4 \ --data-parallel-address --data-parallel-rpc-port 13345 \ --api-server-count=8 --gpu-memory-utilization 0.95 --max-model-len 10240 --enforce-eager # node 1 VLLM_ALL2ALL_BACKEND=deepep_low_latency VLLM_USE_DEEP_GEMM=1 VLLM_RANDOMIZE_DP_DUMMY_INPUTS=1 \ vllm serve deepseek-ai/DeepSeek-R1 --served-model-name deepseek-r1 --tensor-parallel-size 1 \ --enable-expert-parallel --data-parallel-size 8 --data-parallel-size-local 4 \ --data-parallel-address --data-parallel-rpc-port 13345 --data-parallel-start-rank 4 \ --gpu-memory-utilization 0.95 --max-model-len 10240 --enforce-eager --headless ``` Full er...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: kwargs) (EngineCore_DP2 pid=196672) self.model_runner.load_model(eep_scale_up=eep_scale_up) (EngineCore_DP1 pid=196671) ^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP2 pid=196672) File "/opt/vllm/vllm/v1/worker/gpu_model_runner.p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits cuda;fp8;moe;operator;quantization;samp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA error "invalid resource handle" when serving dsr1 with deepep on GB200 bug;stale ### Your current environment ### 🐛 Describe the bug When serving deepseek r1 model on GB200 using the deepep flags on 2 nodes,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: he deepep flags on 2 nodes, a cuda error occurs. I used the default deepgemm commit from vllm, and also tried to upgrade the deepgemm commit to `59495`, but still seeing the same cuda error. Commands to reproduce: ```ba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e same cuda error. Commands to reproduce: ```bash # node 0 VLLM_ALL2ALL_BACKEND=deepep_low_latency VLLM_USE_DEEP_GEMM=1 VLLM_RANDOMIZE_DP_DUMMY_INPUTS=1 \ vllm serve deepseek-ai/DeepSeek-R1 --served-model-name deepseek-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
