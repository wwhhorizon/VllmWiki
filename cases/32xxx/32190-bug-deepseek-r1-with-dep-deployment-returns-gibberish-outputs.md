# vllm-project/vllm#32190: [Bug]: Deepseek-R1 with DEP deployment returns gibberish outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#32190](https://github.com/vllm-project/vllm/issues/32190) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek-R1 with DEP deployment returns gibberish outputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running Deepseek-R1 on 16xH200 using expert parallel deployment the model returns gibberish outputs. It happens with v0.12.0 and v0.13.0, v0.11.0 was working fine. Env variables: ``` - name: VLLM_USE_DEEP_GEMM value: "1" - name: VLLM_MOE_DP_CHUNK_SIZE value: "384" - name: VLLM_SKIP_P2P_CHECK value: "1" - name: VLLM_RANDOMIZE_DP_DUMMY_INPUTS value: "1" - name: VLLM_MOE_ROUTING_SIMULATION_STRATEGY value: "uniform_random" ``` Run cmd: ``` exec python3 -m vllm.entrypoints.openai.api_server \ --all2all-backend deepep_low_latency \ --model deepseek-ai/DeepSeek-R1 \ --served-model-name deepseek-ai/DeepSeek-R1 \ --data-parallel-hybrid-lb \ --tensor-parallel-size 1 \ --data-parallel-size 16 \ --data-parallel-size-local 8 \ --data-parallel-start-rank \ --data-parallel-address \ --data-parallel-rpc-port 13345 \ --enable-expert-parallel \ --no-enable-prefix-caching \ --max-model-len 16384 \ --enable-dbo \ --dbo-decode-token-threshold 32 \ --async-scheduling \ --enable-eplb \ --eplb-config '{"window_size":"1000","step_interval":"3000","num_redundant_experts":"32","log_balancedness":"False"}' \ --max-num-seqs 512 \ --compilation_config '{...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: nt ### 🐛 Describe the bug When running Deepseek-R1 on 16xH200 using expert parallel deployment the model returns gibberish outputs. It happens with v0.12.0 and v0.13.0, v0.11.0 was working fine. Env variables: ``` - nam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ZE_DP_DUMMY_INPUTS value: "1" - name: VLLM_MOE_ROUTING_SIMULATION_STRATEGY value: "uniform_random" ``` Run cmd: ``` exec python3 -m vllm.entrypoints.openai.api_server \ --all2all-backend deepep_low_latency \
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --max-num-seqs 512 \ --compilation_config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' ``` Example output: ``` ptarasiewicz@41df39f-lcedt:~/repo/dynamo$ curl -sS http://localhost:8000/v1/chat/completions -H 'Content-Type: ap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: When running Deepseek-R1 on 16xH200 using expert parallel deployment the model returns gibberish outputs. It happens with v0.12.0 and v0.13.0, v0.11.0 was working fine. Env variables: ``` - name: VLLM_USE_DEEP_GEMM valu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ypoints.openai.api_server \ --all2all-backend deepep_low_latency \ --model deepseek-ai/DeepSeek-R1 \ --served-model-name deepseek-ai/DeepSeek-R1 \ --data-parallel-hybrid-lb \ --tensor-parallel-size 1 \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
