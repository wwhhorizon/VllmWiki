# vllm-project/vllm#42023: [Bug]: MooncakeConnector may auto-select the wrong host IP when VLLM_HOST_IP is unset on multi-homed hosts

| 字段 | 值 |
| --- | --- |
| Issue | [#42023](https://github.com/vllm-project/vllm/issues/42023) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MooncakeConnector may auto-select the wrong host IP when VLLM_HOST_IP is unset on multi-homed hosts

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary When using `MooncakeConnector` with disaggregated prefill/decode on a multi-homed machine, vLLM/Mooncake may auto-select the wrong local IP address if `VLLM_HOST_IP` is not set. This causes Mooncake KV transfer to fail even though the HTTP API endpoints are reachable and correctly configured. In my case: - Prefill HTTP API: `http://10.208.130.107:8010` - Decode HTTP API: `http://10.208.130.185:8020` However, on the decode host, Mooncake auto-selected `192.168.30.10` instead of `10.208.130.185`, and the KV transfer later failed with: ```text Mooncake transfer engine returned -1 ``` Setting: ```bash export VLLM_HOST_IP=10.208.130.185 ``` fixed the problem immediately. --- ### Reproduction #### Decode host `hostname -I` output: ```text 10.208.130.185 192.168.5.13 192.168.30.10 172.17.0.1 172.17.46.0 ``` Without setting `VLLM_HOST_IP`, the decode side started with logs like: ```text Transfer Engine parseHostNameWithPort. server_name: 192.168.30.10 port: 12001 Transfer Engine RPC using P2P handshake, listening on 192.168.30.10:15301 ``` But the intended reachable IP between prefill/decode nodes was: ```text 10.208.130.185...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ernal Mooncake transport to use the same reachable interface unless explicitly overridden. However, Mooncake/vLLM uses an auto-detected IP for worker-to-worker KV transfer, which may differ from the HTTP-facing IP on mu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: the bug ### Summary When using `MooncakeConnector` with disaggregated prefill/decode on a multi-homed machine, vLLM/Mooncake may auto-select the wrong local IP address if `VLLM_HOST_IP` is not set. This causes Mooncake...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --- ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r to fail even though the HTTP API endpoints are reachable and correctly configured. In my case: - Prefill HTTP API: `http://10.208.130.107:8010` - Decode HTTP API: `http://10.208.130.185:8020` However, on the decode ho...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
