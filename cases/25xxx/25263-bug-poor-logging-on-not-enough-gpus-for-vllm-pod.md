# vllm-project/vllm#25263: [Bug]: Poor logging on not enough GPUs for vLLM pod

| 字段 | 值 |
| --- | --- |
| Issue | [#25263](https://github.com/vllm-project/vllm/issues/25263) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | fp8;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Poor logging on not enough GPUs for vLLM pod

### Issue 正文摘录

### Your current environment This is running on K8s so all relevant ENV configurations will be passed this way instead: ``` ☁ tmp [main] ⚡ k get pods NAME READY STATUS RESTARTS AGE gaie-pd-epp-5f9ffd7bd5-r8grv 1/1 Running 0 15h infra-pd-inference-gateway-istio-c9859cdc4-wck2l 1/1 Running 0 7m19s interactive-pod 1/1 Running 0 2d12h ms-pd-llm-d-modelservice-decode-545d5d4498-mr2s4 2/2 Running 22 (6m3s ago) 15h ms-pd-llm-d-modelservice-prefill-7c98f64d9-4c564 1/1 Running 0 15h ms-pd-llm-d-modelservice-prefill-7c98f64d9-9mm9p 1/1 Running 0 15h ms-pd-llm-d-modelservice-prefill-7c98f64d9-fmz5c 1/1 Running 0 15h ms-pd-llm-d-modelservice-prefill-7c98f64d9-h95q8 1/1 Running 0 15h ☁ tmp [main] ⚡ k get pod ms-pd-llm-d-modelservice-decode-545d5d4498-mr2s4 -o yaml | yq '.spec' containers: - args: - RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic - --port - "8200" - --served-model-name - RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic - --tensor-parallel-size - "4" - --block-size - "128" - --kv-transfer-config - '{"kv_connector":"NixlConnector", "kv_role":"kv_both"}' - --disable-log-requests - --disable-uvicorn-access-log - --max-model-len - "32000" command: - vllm - serve env: - name: VLLM_NIXL_SIDE_C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: _SIDE_CHANNEL_HOST valueFrom: fieldRef: apiVersion: v1 fieldPath: status.podIP - name: VLLM_LOGGING_LEVEL value: DEBUG - name: DP_SIZE value: "1" - name: TP_SIZE value: "1" - name: HF_HOME value:
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 1/1 Running 0 2d12h ms-pd-llm-d-modelservice-decode-545d5d4498-mr2s4 2/2 Running 22 (6m3s ago) 15h ms-pd-llm-d-modelservice-prefill-7c98f64d9-4c564 1/1 Running 0 15h ms-pd-llm-d-modelservice-prefill-7c98f64d9-9mm9p 1/1
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### Your current environment This is running on K8s so all relevant ENV configurations will be passed this way instead: ``` ☁ tmp [main] ⚡ k get pods NAME READY STATUS RESTARTS AGE gaie-pd-epp-5f9ffd7bd5-r8grv 1
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 1/1 Running 0 2d12h ms-pd-llm-d-modelservice-decode-545d5d4498-mr2s4 2/2 Running 22 (6m3s ago) 15h ms-pd-llm-d-modelservice-prefill-7c98f64d9-4c564 1/1 Running 0 15h ms-pd-llm-d-modelservice-prefill-7c98f64d9-9mm9p 1/1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: yq '.spec' containers: - args: - RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic - --port - "8200" - --served-model-name - RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic - --tensor-parallel-size - "4" - --block-size - "128" -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
