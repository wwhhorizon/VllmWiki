# vllm-project/vllm#29904: [Bug]: Mistral Large 3 being detected as "PixtralForConditionalGeneration" in nightly container

| 字段 | 值 |
| --- | --- |
| Issue | [#29904](https://github.com/vllm-project/vllm/issues/29904) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral Large 3 being detected as "PixtralForConditionalGeneration" in nightly container

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the new Mistral large 3 using the nightly container with the following configuration in K8s: ```yaml apiVersion: apps/v1 kind: Deployment metadata: name: mistral-large-3-vllm spec: replicas: 1 selector: matchLabels: app: mistral-large-3-vllm template: metadata: labels: app: mistral-large-3-vllm spec: containers: - name: vllm-server image: vllm/vllm-openai:nightly args: - "--model" - "mistralai/Mistral-Large-3-675B-Instruct-2512" - "--tensor-parallel-size" - "8" - "--tokenizer-mode" - "mistral" - "--config-format" - "mistral" - "--load-format" - "mistral" - "--enable-auto-tool-choice" - "--tool-call-parser" - "mistral" ports: - containerPort: 8000 name: http volumeMounts: - name: model-storage mountPath: /root/.cache/huggingface resources: requests: nvidia.com/gpu: 8 memory: "500Gi" cpu: "32" limits: nvidia.com/gpu: 8 memory: "500Gi" env: - name: HF_HOME value: "/root/.cache/huggingface" volumes: - name: model-storage persistentVolumeClaim: claimName: mistral-large-model-storage ``` It runs into the following error: ```bash kubectl -n gpt-oss logs -f mistral-large-3-vllm-696df6455b-7dhtf (APIServer pid=1) INFO 12-02 0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: g the new Mistral large 3 using the nightly container with the following configuration in K8s: ```yaml apiVersion: apps/v1 kind: Deployment metadata: name: mistral-large-3-vllm spec: replicas: 1 selector: matchLabels: a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: (APIServer pid=1) INFO 12-02 09:01:49 [model.py:2086] Downcasting torch.float32 to torch.bfloat16. (APIServer pid=1) INFO 12-02 09:01:49 [model.py:1750] Using max model len 294912 (APIServer pid=1) INFO 12-02 09:01:50 [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e nightly container with the following configuration in K8s: ```yaml apiVersion: apps/v1 kind: Deployment metadata: name: mistral-large-3-vllm spec: replicas: 1 selector: matchLabels: app: mistral-large-3-vllm template:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: mountPath: /root/.cache/huggingface resources: requests: nvidia.com/gpu: 8 memory: "500Gi" cpu: "32" limits: nvidia.com/gpu: 8 memory: "500Gi" env: - name: HF_HOME value:
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
