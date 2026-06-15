# vllm-project/vllm#31490: [Performance]: The prefill phase in the disaggregated_serving_p2p_nccl_xpyd example exhibits poor performance

| 字段 | 值 |
| --- | --- |
| Issue | [#31490](https://github.com/vllm-project/vllm/issues/31490) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: The prefill phase in the disaggregated_serving_p2p_nccl_xpyd example exhibits poor performance

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance 🔍 Issue Summary The prefill stage in PD (Prefill-Decode) separation setup is experiencing severe performance bottlenecks, significantly impacting overall inference throughput. 🖥️ Environment Information Hardware Configuration GPUs: 2x NVIDIA A100-SXM4-40GB with NVLink Driver Version: 570.86.15 CUDA Version: 12.8 NVCC Version: cuda_12.6.r12.6/compiler.35059454_0 Software Environment vLLM Version: 0.14.0rc1.dev48+gc02a2705f.d20251222.cu126 Model: Qwen3-4B Architecture: PD Separation (Prefill-Decode Separation) 🚀 Reproduction Steps Server Configuration # Prefill Server Launch CUDA_VISIBLE_DEVICES=$gpu_id vllm serve $MODEL \ --host 0.0.0.0 \ --port $port \ --max-model-len 8192 \ --max-num-seqs 100 \ --gpu-memory-utilization 0.9 \ --max_num_batched_tokens 100000 \ --kv-transfer-config \ "{\"kv_connector\":\"P2pNcclConnector\",\"kv_role\":\"kv_producer\",\"kv_buffer_size\":\"1e8\",\"kv_port\":\"$kv_port\",\"kv_connector_extra_config\":{\"proxy_ip\":\"0.0.0.0\",\"proxy_port\":\"$PROXY_PORT\",\"http_port\":\"$port\",\"send_type\":\"PUT_ASYNC\",\"nccl_num_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ary The prefill stage in PD (Prefill-Decode) separation setup is experiencing severe performance bottlenecks, significantly impacting overall inference throughput. 🖥️ Environment Information Hardware Configuration GPUs:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: significantly impacting overall inference throughput. 🖥️ Environment Information Hardware Configuration GPUs: 2x NVIDIA A100-SXM4-40GB with NVLink Driver Version: 570.86.15 CUDA Version: 12.8 NVCC Version: cuda_12.6.r12...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: The prefill phase in the disaggregated_serving_p2p_nccl_xpyd example exhibits poor performance performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance 🔍 Issue Summary The prefill stage in PD (Prefill-Decode) separation setup is experiencin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hput. 🖥️ Environment Information Hardware Configuration GPUs: 2x NVIDIA A100-SXM4-40GB with NVLink Driver Version: 570.86.15 CUDA Version: 12.8 NVCC Version: cuda_12.6.r12.6/compiler.35059454_0 Software Environment vLLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
