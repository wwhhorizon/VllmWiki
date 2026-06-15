# vllm-project/vllm#21498: [Bug]: vllm start gemma3 fail: NotImplementedError: Vlm do not work with prefix caching yet rank=6

| 字段 | 值 |
| --- | --- |
| Issue | [#21498](https://github.com/vllm-project/vllm/issues/21498) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm start gemma3 fail: NotImplementedError: Vlm do not work with prefix caching yet rank=6

### Issue 正文摘录

### Your current environment Here is configure: ``` apiVersion: serving.kserve.io/v1beta1 kind: InferenceService metadata: name: gemma-tgi namespace: onecloud-dev spec: predictor: containers: - name: kserve-container image: ghcr.io/huggingface/text-generation-inference:latest args: - "--model-id=google/gemma-3-27b-it" - "--port=8000" - "--max-batch-prefill-tokens=8192" - "--max-total-tokens=8192" - "--max-concurrent-requests=4" - "--quantize=bitsandbytes" ports: - containerPort: 8000 name: http env: - name: HUGGING_FACE_HUB_TOKEN value: "zxxxxxxx" resources: limits: cpu: "180" memory: "636Gi" nvidia.com/gpu: 8 requests: cpu: "180" memory: "636Gi" nvidia.com/gpu: 8 readinessProbe: httpGet: path: /health port: 8000 initialDelaySeconds: 720 # 12 minutes periodSeconds: 10 livenessProbe: httpGet: path: /health port: 8000 initialDelaySeconds: 720 periodSeconds: 10 volumeMounts: - name: dshm mountPath: /dev/shm volumes: - name: dshm emptyDir: medium: Memory ``` ### 🐛 Describe the bug ``` # kubectl logs -n onecloud-dev gemma-tgi-predictor-6866f644c8-wl56l -f 2025-07-24T04:40:27.376225Z INFO text_generation_launcher: Args { model_id: "google/gemma-3-27b-it", revision: None, validation_work...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: vllm start gemma3 fail: NotImplementedError: Vlm do not work with prefix caching yet rank=6 bug ### Your current environment Here is configure: ``` apiVersion: serving.kserve.io/v1beta1 kind: InferenceService met...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g yet rank=6 bug ### Your current environment Here is configure: ``` apiVersion: serving.kserve.io/v1beta1 kind: InferenceService metadata: name: gemma-tgi namespace: onecloud-dev spec: predictor: containers: - name: ks...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: oogle/gemma-3-27b-it" - "--port=8000" - "--max-batch-prefill-tokens=8192" - "--max-total-tokens=8192" - "--max-concurrent-requests=4" - "--quantize=bitsandbytes" ports: - containerPort: 8000 name: http env
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: al-tokens=8192" - "--max-concurrent-requests=4" - "--quantize=bitsandbytes" ports: - containerPort: 8000 name: http env: - name: HUGGING_FACE_HUB_TOKEN value: "zxxxxxxx" resources: limits:
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: figure: ``` apiVersion: serving.kserve.io/v1beta1 kind: InferenceService metadata: name: gemma-tgi namespace: onecloud-dev spec: predictor: containers: - name: kserve-container image: ghcr.io/huggingface/text-generation...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
