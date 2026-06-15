# vllm-project/vllm#38077: [Bug]: Qwen3.5-9B answer !!!!!!!!!

| 字段 | 值 |
| --- | --- |
| Issue | [#38077](https://github.com/vllm-project/vllm/issues/38077) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-9B answer !!!!!!!!!

### Issue 正文摘录

### Your current environment my env cat vllm-a10.yaml # vllm-a10.yaml --- apiVersion: v1 kind: Namespace metadata: name: vllm --- apiVersion: apps/v1 kind: Deployment metadata: name: vllm-qwen3-5-9b namespace: vllm labels: app: vllm-qwen3-5-9b spec: replicas: 1 selector: matchLabels: app: vllm-qwen3-5-9b template: metadata: labels: app: vllm-qwen3-5-9b spec: restartPolicy: Always nodeName: adctrain2 containers: - name: vllm image: docker.xuanyuan.run/vllm/vllm-openai:v0.18.0 imagePullPolicy: IfNotPresent command: - python3 - -m - vllm.entrypoints.openai.api_server - --model - /data/Qwen3.5-9B - --served-model-name - Qwen3.5-9B - --host - "0.0.0.0" - --port - "8000" - --tensor-parallel-size - "4" - --dtype - auto - --max-model-len - "32768" - --gpu-memory-utilization - "0.85" - --trust-remote-code - --enable-auto-tool-choice - --reasoning-parser - qwen3 - --tool-call-parser - qwen3_coder - --enable-prefix-caching - --attention-backend - auto - --kv-cache-dtype - auto env: - name: VLLM_LOGGING_LEVEL value: "INFO" - name: HF_HUB_OFFLINE value: "1" - name: TRANSFORMERS_OFFLINE value: "1" - name: PYTORCH_CUDA_ALLOC_CONF value: "expandable_segments:True" # 优化显存碎片 ports: - containerPort:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment my env cat vllm-a10.yaml # vllm-a10.yaml --- apiVersion: v1 kind: Namespace metadata: name: vllm --- apiVersion: apps/v1 kind: Deployment metadata: name: vllm-qwen3-5-9b namespace: vllm labels: ap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5-9B answer !!!!!!!!! bug ### Your current environment my env cat vllm-a10.yaml # vllm-a10.yaml --- apiVersion: v1 kind: Namespace metadata: name: vllm --- apiVersion: apps/v1 kind: Deployment metadata: nam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e: TRANSFORMERS_OFFLINE value: "1" - name: PYTORCH_CUDA_ALLOC_CONF value: "expandable_segments:True" # 优化显存碎片 ports: - containerPort: 8000 name: http resources: requests: nvidia.com/gpu: "4"
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: qwen3_coder - --enable-prefix-caching - --attention-backend - auto - --kv-cache-dtype - auto env: - name: VLLM_LOGGING_LEVEL value: "INFO" - name: HF_HUB_OFFLINE value: "1" - name:
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: "8000" - --tensor-parallel-size - "4" - --dtype - auto - --max-model-len - "32768" - --gpu-memory-utilization - "0.85" - --trust-remote-code - --enable-auto-tool-choice - --reasoning

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
